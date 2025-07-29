from pytube import YouTube

url = input("Enter YouTube URL: ")
yt = YouTube(url)
stream = yt.streams.get_highest_resolution()
stream.download()
print("Downloaded!")
