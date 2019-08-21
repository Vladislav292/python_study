from pytube import YouTube
mode = input("v for video, a for audio")
list = input("輸入要下載的youtube影片網址")
yt = YouTube(list)
print(yt.streams.all())
if mode == 'v':
    i = input("選擇要的解析度")
    j = input("選擇要的格式")
    stream = yt.streams.filter(res = i,subtype = j).first()
    path=input("請指定位子")
    stream.download(path)
elif mode == 'a':
    i = input("選擇要的kbps")
    stream = yt.streams.filter(abr = i + 'kbps').first()
    path=input("請指定位子")
    stream.download(path)
else:
    input('input v or a')


