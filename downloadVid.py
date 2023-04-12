import os
from pytube import YouTube
import requests
from tqdm import tqdm
import math
import re


def multi_replace_regex(string, replacements):
    for pattern, replacement in replacements.items():
        string = re.sub(pattern, replacement, string)
    return string

replacements = {
    "\\\\"  :   chr(0x29F9),
    "[/]"   :   chr(0x29F8),
    "[:]"   :   chr(0xFF1A),
    "[*]"   :   chr(0xFF0A),
    "[?]"   :   chr(0xFF1F),
    '["]'   :   chr(0xFF02),
    "[|]"   :   chr(0xFF5C)
}


def download_video(video_url) -> str:
    yt = YouTube(video_url)

    filename = multi_replace_regex(yt.title, replacements) + ".mp4"
    file_path = os.path.join("Video/", filename)

    #If file already exists, don't download it again
    if os.path.isfile(file_path):
        print("Video already downloaded. Starting playback...")
        video_url = file_path
        return video_url

    stream = yt.streams.filter(file_extension='mp4').first()
    response = requests.get(stream.url, stream=True)

    total_size = int(response.headers.get("Content-Length", 0))
    block_size = 1024
    wrote = 0 
     
    with open(file_path, "wb") as f:
        for data in tqdm(response.iter_content(block_size), total=math.ceil(total_size//block_size), unit="KB", unit_scale=True):
            wrote = wrote  + len(data)
            f.write(data)
    if total_size != 0 and wrote != total_size:
        print("ERROR, something went wrong")

    return file_path

