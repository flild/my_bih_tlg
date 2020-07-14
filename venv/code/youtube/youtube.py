import json
import re
import requests
import sys
import sys

from pytube import YouTube
from .config import token_yt


class YouTube_downloader:
    def __init__(self, send_url):
        self.video_id = send_url.rsplit("/", 1)[1]
        self.url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={self.video_id}&key={token_yt}"
        self.json_url = requests.get(self.url)
        self.data = json.loads(self.json_url.text)

    def print_data(self):
        print(self.data)

    def get_video_title(self):
        return self.data["items"][0]["snippet"]["title"]

    def download_video(self, send_url: str):
        title = self.get_video_title()
        YouTube(send_url).streams.first().download(filename=title)
        return title
