import os
from pytube import YouTube
import requests
from tqdm import tqdm
import math

# Input video url
video_url = input("Enter video url: ")
if(YouTube(video_url).title())
def download_video(video_url):
    yt = YouTube(video_url)
    stream = yt.streams.filter(file_extension='mp4').first()
    response = requests.get(stream.url, stream=True)

    total_size = int(response.headers.get("Content-Length", 0))
    block_size = 1024
    wrote = 0 

    filename = yt.title + ".mp4"
    file_path = os.path.join("Video/", filename)

    with open(file_path, "wb") as f:
        for data in tqdm(response.iter_content(block_size), total=math.ceil(total_size//block_size), unit="KB", unit_scale=True):
            wrote = wrote  + len(data)
            f.write(data)
    if total_size != 0 and wrote != total_size:
        print("ERROR, something went wrong")

download_video(video_url)

