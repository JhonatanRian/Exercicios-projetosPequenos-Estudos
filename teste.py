from pytube import YouTube
import re 


video = YouTube("https://www.youtube.com/watch?v=c0OSqBmNmuA")

stream = str(video.streams)

st = re.compile("MACACO")

print(st.search(stream))