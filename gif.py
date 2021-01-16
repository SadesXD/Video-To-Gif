from tkinter.filedialog import *
from moviepy.editor import VideoFileClip
import os
import time

spliter = "\n-----------------------------"
ts = time.localtime()
fileTimeName = f'{ts[0]}-{ts[1]}-{ts[2]} {ts[3]}-{ts[4]}-{ts[5]}'

def cls():
    try:
        os.system('cls')
    except:
        os.system('clear')

def back():
    print(spliter)
    print('\n[1] -> Back to main menu\n[2] -> Exit / Close the program\n')
    pilih = input("Select the number: ")
    if pilih == "1":
        main()
    elif pilih == "2":
        quit()
    else:
        cls()
        print("Can't find your selection\n")
        back()

def main():
    cls()
    print("[ Video to gif converter ]\n\n[1] -> Start Convert The Video\n[2] -> Show guide for using the program\n[3] -> Exit\n")
    pilih = input("Select the number: ")
    if pilih == "1" or pilih.lower() == "start":
        cls()
        run()
    elif pilih == "2" or pilih.lower() == "guide":
        cls()
        guide()
    elif pilih == "3" or pilih.lower() == "exit":
        quit()
    else:
        cls()
        print("Can't find your selection\n")
        back()

def run():
    cls()
    print("Prepare for open the file directory...")
    time.sleep(2)
    print("Please wait 3 seconds for open the file directory...")
    time.sleep(3)
    print("Starting open the file directory...")
    time.sleep(1)
    vid = askopenfilename()
    clip = VideoFileClip(vid)
    cls()
    nama = input("What's file name will you set as a gif file: ")
    if not nama:
        nama = "VidToGif"
    print(f"\nStarting convert your video file into gif file as [ {nama} {fileTimeName}.gif ]...\n")
    clip.write_gif(f'{nama} {fileTimeName}.gif', fps= 10)
    cls()
    print("\nSuccess convert video file into gif file")
    back()

def guide():
    teks = f'[ GUIDE ]\n\n[$] -> select number 1 in main menu for start converting video file into gif file\n[$] -> you will got question while converting a video\n[$] -> Done\n{spliter}\n\n[!] Our Discord Server: https://discord.gg/8rUvTYhFqK\n[!] Github: https://github.com/SadesXD/Video-To-Gif'
    print(teks)
    back()
    
main()
