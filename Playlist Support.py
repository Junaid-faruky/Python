from pytube import Playlist

playlist_url = input("Enter YouTube Playlist URL: ")
p = Playlist(playlist_url)

print(f"Downloading Playlist: {p.title}")
for video in p.videos:
    print(f"Downloading: {video.title}")
    video.streams.get_highest_resolution().download()
print("Download Complete!")
