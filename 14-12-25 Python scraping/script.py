#python -m pip    
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/aphrodite"
#url = input("You write the web page")
#part = input("write the part that you want found")
part = "text"
searched = {}

if part == "text":
    searched = {"start":"<title>", "end":"</title>"}
if part == "h1":
    searched = {"start":"<h1>", "end":"</h1>"}
if part == "h2":
    searched = {"start":"<h2>", "end":"</h2>"}       

page = urlopen(url)
print(searched)

htmlbytes = page.read()  #sequence of bytes
html = htmlbytes.decode("utf-8")   #decode bytes to string
#startindex = html.find("<title>")
#endindex = html.find("</title>")
startindex = html.find(searched["start"])
endindex = html.find(searched["end"])
search = html[startindex:endindex]
print(search)