import datetime
import backtrader as bt
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

#python -m pip          para instalar

# --- 1. Definición de la Estrategia (La Lógica del Bot) ---
class SMACrossover(bt.Strategy):
    params = dict(
        period1=5,  # Periodo para la SMA rápida
        period2=10,  # Periodo para la SMA lenta
    )

    def __init__(self):
        # Referencias a los indicadores
        self.dataclose = self.datas[0].close
        self.order = None  # Para rastrear órdenes pendientes

        # Calcular las Medias Móviles Simples (SMA)
        # 0=línea actual, -1=línea anterior
        sma1 = bt.indicators.SMA(self.datas[0], period=self.p.period1)
        sma2 = bt.indicators.SMA(self.datas[0], period=self.p.period2)

        # Indicador de cruce: 'crossover' es positivo si sma1 > sma2
        self.crossover = bt.indicators.CrossOver(sma1, sma2)

    def next(self):
        # Lógica principal que se ejecuta en cada barra de datos (cada día)

        if self.order:
            return  # Si ya hay una orden pendiente, no hacemos nada más

        # Si no estamos dentro del mercado (no tenemos acciones compradas)
        if not self.position:
            # Si la línea de cruce es positiva (rápida cruza por encima de lenta)
            if self.crossover > 0:
                print(f'[{self.datas[0].datetime.date(0)}] COMPRA: Cruce alcista detectado.')
                # Ejecutar orden de compra (compramos 10 unidades)
                self.order = self.buy(size=10)

        # Si ya estamos dentro del mercado (tenemos acciones compradas)
        else:
            # Si la línea de cruce es negativa (rápida cruza por debajo de lenta)
            if self.crossover < 0:
                print(f'[{self.datas[0].datetime.date(0)}] VENTA: Cruce bajista detectado.')
                # Ejecutar orden de venta (vendemos todas nuestras unidades)
                self.order = self.sell(size=10)
    
    def notify_order(self, order):
        # Función para manejar notificaciones de órdenes (ejecutadas, canceladas, etc.)
        if order.status in [order.Submitted, order.Accepted]:
            # La orden está pendiente, no hacemos nada
            return

        if order.status in [order.Completed]:
            if order.isbuy():
                print(f'--- ORDEN EJECUTADA COMPRA --- Precio: {order.executed.price:.2f}, Costo: {order.executed.value:.2f}, Comisión: {order.executed.comm:.2f}')
            elif order.issell():
                print(f'--- ORDEN EJECUTADA VENTA --- Precio: {order.executed.price:.2f}, Costo: {order.executed.value:.2f}, Comisión: {order.executed.comm:.2f}')
            self.order = None

        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            print('¡Orden Cancelada/Rechazada/Margen Insuficiente!')
            self.order = None


# --- 2. Preparación y Ejecución del Backtesting ---
if __name__ == '__main__':
    # Inicializar el cerebro de backtrader
    cerebro = bt.Cerebro()

    # Añadir nuestra estrategia al cerebro
    cerebro.addstrategy(SMACrossover)

    # Cargar datos de ejemplo (usando pandas para crear un DataFrame simple)
    # En un bot real, usarías yfinance o la API del bróker
    
    # Creamos datos ficticios de 300 días
    ticker = 'BTC-USD' 
    start_date = '2019-01-01'
    end_date = '2021-01-01'

    # Descargar los datos usando yfinance
    data_df = yf.download(ticker, start=start_date, end=end_date, progress=False)

    # *** CÓDIGO AÑADIDO PARA APLANAR Y RENOMBRAR COLUMNAS DE FORMA ROBUSTA ***
    # Si las columnas son multi-nivel (como tuplas), las aplanamos
    if isinstance(data_df.columns, pd.MultiIndex):
        data_df.columns = ['_'.join(col).strip() for col in data_df.columns.values]
    
    # Renombramos explícitamente las columnas al formato esperado por backtrader (minúsculas)
    data_df.rename(columns={
        'Open': 'open',
        'High': 'high',
        'Low': 'low',
        'Close': 'close',
        'Adj Close': 'adj close',
        'Volume': 'volume'
    }, inplace=True)
    
    # Convertir el DataFrame de pandas al formato de datos de backtrader
    # backtrader espera las columnas en minúsculas: 'open', 'high', 'low', 'close', 'volume'
    datafeed = bt.feeds.PandasData(dataname=data_df)

    # Añadir los datos al cerebro
    cerebro.adddata(datafeed)
    # Establecer la cantidad inicial de efectivo (capital)
    cerebro.broker.setcash(10000.0)

    # Establecer una comisión global (0.1%)
    cerebro.broker.setcommission(commission=0.001)

    # *** AÑADE ESTAS DOS LÍNEAS ***
    # Configurar el sistema para manejar el valor final correctamente
    cerebro.broker.set_coo(True)
    cerebro.addobserver(bt.observers.Value) # Añade un observador de valor para forzar el cálculo

    # Imprimir el valor inicial de la cartera
    print(f'Valor inicial de la cartera: {cerebro.broker.getvalue():.2f}')

    # --- 3. Ejecutar el Backtesting ---
    strategies = cerebro.run()
    first_strategy = strategies[0] # Tomamos la primera estrategia ejecutada

    # Imprimir el valor final de la cartera usando el valor de la estrategia
    print(f'Valor final de la cartera: {first_strategy.broker.getvalue():.2f}')
    # Opcional: Graficar los resultados (requiere matplotlib)
    # cerebro.plot(style='candlestick')
