import instaloader

username = input("Enter Instagram username: ")
instaloader.Instaloader().download_profile(username, profile_pic_only=True)
print("Downloaded profile picture!")
