from playsound import playsound
import os

input1 = input("music: ")

folder = os.path.join("musics/")

musics = []

for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".mp3"):
                file_path = os.path.join(file)
                musics.append(file_path)

playsound(folder + musics[int(input1)])
print(folder + musics[int(input1)])