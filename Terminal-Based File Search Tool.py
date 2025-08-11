import os

def search_file(keyword, path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if keyword.lower() in file.lower():
                print(os.path.join(root, file))

search_file(input("Search keyword: "), "C:/")
