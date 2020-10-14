import pafy
from pathlib import Path
import os

path = str(os.path.join(Path.home(), "Downloads"))


def download_audio(video_url):
    video = pafy.new(video_url)
    audio_stream = video.getbestaudio(preftype='m4a')
    audio_stream.download(filepath=path)
