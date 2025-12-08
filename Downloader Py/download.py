import sys
from pytube import YouTube
from moviepy.editor import *
import os
import shutil

#url = sys.argv[1]
select = 'a'
type = 'MP3'
#directorio = './DescargadosYT'
#print('ver datos '+select+type)
def Download(url, select, type):
    yt = YouTube(url)

    if select == 'h':
        yt = yt.streams.get_highest_resolution()
    elif select == 'l':
        yt = yt.streams.get_lowest_resolution()
    elif select == 'a':
        yt = yt.streams.get_audio_only()
    try:
        os.mkdir('DescargadosYT')
        arch = yt.download()
        shutil.move(arch, './DescargadosYT')
    except:
        print('Error en la descarga...')
    print('El video se ha descargado correctamente...')       

def transformarMp3():
    directorio = './DescargadosYT'
    archivos = os.listdir(directorio)
    listaArchivos = []
    print(archivos)
    """""
    for item in archivos:
        listaArchivos.append(str(item))
        # Load the mp4 file
        video = VideoFileClip(str(item))
        # Extract audio from video
        video.audio.write_audiofile(str(item)+".mp3") """
    video = VideoFileClip('./DescargadosYT/Flowers.mp4')
        # Extract audio from video
    video.audio.write_audiofile('./DescargadosYT/Flowers.mp4'+".mp3")           

#Download(url, select, type)     
transformarMp3()

