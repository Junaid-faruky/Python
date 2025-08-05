from pytube import YouTube

link = input("Enter YouTube URL: ")
yt = YouTube(link)
yt.streams.get_highest_resolution().download()
print("Download completed!")
