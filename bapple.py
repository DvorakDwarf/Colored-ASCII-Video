import cv2
import sys
import os
import questionary
import time
from ffpyplayer.player import MediaPlayer
from pytube import YouTube
import downloadVid #local import that download the video

#------------------------
#If you don't want to download the video, comment out 7th line 
# and change the path to the video you want to use on line 36
#------------------------

#To Add
#Multithread
#Cleanup
#Use background color as an option
#Option for flipped colors, looked cool
#Remake in rust

# ·  ·  ·  ·  #

ASPECT_RATIO = 1.5 #Ratio of height to width for font

palletes = {
    "Regular": ["#", "%", "?", "+", ":", "·", "·"],
    "Inverse": ["·", "·", ":", "+", "%", "#", "#"],
    "\"Monochrome\"": ["#", "·", "·"]
}

modes = {
    "Use max terminal space": 2,
    "Maintain aspect ratio": 1,
}

display_modes = [
    "YouTube",
    "Local file"
]

#Might still be messy
ascii_choice = questionary.select(
    "What ASCII scheme to use ? (Try the other options if video looks bad)",
    choices=list(palletes.keys()),
    ).ask()
ascii_scheme = palletes[ascii_choice]

mode_choice = questionary.select(
    "Which do you prefer ? (If one breaks, pick the other)",
    choices=list(modes.keys())
).ask()
mode = modes[mode_choice]

display_choice = questionary.select(
    "Would you like to play a video from YouTube or a local file ?",
    choices=display_modes
).ask()

path = None
if display_choice == display_modes[0]:
    # Input video url
    video_url = input("[*]Enter video URL: ")

    #Downloads video, returns path to file
    path = downloadVid.download_video(video_url)
else:
    path = questionary.text("Then what is the path to your video ?",).ask()

#Set video source
video = cv2.VideoCapture(path)
player = MediaPlayer(path)

def grayscale(rgb):
    rgb = rgb
    r = int(rgb[0])
    g = int(rgb[1])
    b = int(rgb[2])
    brightness = (r + g + b) / 3
    return brightness

def print_frame(img, frame_time):
    player.set_pause(False)
    current_time = time.time()
    #Take image, turn greyscale, resize

    #Find maximum number of characters based on terminal size
    #Check terminal size in loop to be fancy
    terminal = os.get_terminal_size()
    term_width = terminal.columns
    term_height = terminal.lines

    #Needs to be even to center neatly
    if term_width % 2 != 0:
        term_width -= 1

    height = img.shape[0]
    width = img.shape[1]
    #How much width per height for original to keep aspect ratio
    original_ratio = width / height

    width_ratio = term_width / width
    height_ratio = term_height / height

    if mode == 1:
        #Doesn't work on vertical monitor
        width_ratio = height_ratio * original_ratio * ASPECT_RATIO
        small_img = cv2.resize(img, (0, 0), fx=width_ratio, fy=height_ratio)
    elif mode == 2:
        #Doesn't work on vertical monitor
        small_img = cv2.resize(img, (0, 0), fx=width_ratio, fy=height_ratio)

    #Find how much needs to be cleared every new frame
    small_height = small_img.shape[0]
    small_width = small_img.shape[1]

    #How much of the brightness each character occupies
    magic_num = 255/(len(ascii_scheme)-1.001)
    #This does the actual job
    ascii = ""
    for col in small_img:
        size_difference = term_width - small_width

        if size_difference > 1:
            for i in range(int(size_difference/2 + 1)):
                ascii += " "

        for row in col:
            brightness = grayscale(row)
            character = ascii_scheme[int(brightness // magic_num)];
            ascii += f'\x1b[38;2;{row[2]};{row[1]};{row[0]}m{character}'
        ascii += "\n"

    print(ascii[:-1], end="")
    while True:
        if time.time() - current_time <= frame_time:
            pass
        else:
            sys.stdout.write(f"\033[{small_height + 1}F") # Cursor up n lines
            player.set_pause(True)
            break

fps = video.get(cv2.CAP_PROP_FPS)
print(f"FPS is {fps}")
frame_time = 1 / fps
# frame_time -= 0.001

audio_frame, val = player.get_frame()

while True:
    success, image = video.read()

    if success == True:
        print_frame(image, frame_time)
    else:
        break
