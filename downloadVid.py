import os
from pytube import YouTube
import requests
from tqdm import tqdm
import math

def download_video(video_url) -> str:
    yt = YouTube(video_url)
    
    filename = yt.title + ".mp4"
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

