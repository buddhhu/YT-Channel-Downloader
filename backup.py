#    Copyright (c) 2022 Amit Sharma < https://github.com/buddhhu >
#
#    License can be found in < https://github.com/budhhu/YT-Channel-Downloader/blob/main/License > .


# - - - - - - - - - - Imports - - - - - - - - - -
from glob import glob
from os import system
from os.path import getsize
from re import search

from decouple import config
from pyrogram import Client
from youtubesearchpython import Playlist
from youtubesearchpython.core.utils import playlist_from_channel_id
from yt_dlp import YoutubeDL

# - - - - - - - - - - Variables - - - - - - - - - -
API_ID = config("API_ID", default=6, cast=int)
API_HASH = config("API_HASH", default="eb06d4abfb49dc3eeb1aeb98ae0f581e", cast=str)
BOT_TOKEN = config("BOT_TOKEN", default="", cast=str)
TG_CHANNEL_ID = config("TG_CHANNEL_ID", default=0, cast=int)
YT_CHANNEL_LINK = config("YT_CHANNEL_LINK", default="", cast=str)

# - - - - - - - - - - Constants - - - - - - - - - -
channel = Playlist(playlist_from_channel_id(YT_CHANNEL_LINK.split("/")[-1]))
youtube_link = "https://www.youtube.com/watch?v={}"
thumbnail_link = "https://i.ytimg.com/vi/{}/maxresdefault.jpg"
client = Client(
    name="bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    in_memory=True,
    parse_mode="md",
)
opts = {
    "quiet": True,
    "noprogress": True,
    "format": "bestvideo+bestaudio",
    "prefer_ffmpeg": True,
    "geo-bypass": True,
    "nocheckcertificate": True,
    "outtmpl": "%(id)s.%(ext)s",
    "postprocessors": [
        {"key": "FFmpegMetadata"},
        {"key": "FFmpegVideoConvertor", "preferedformat": "mp4"},
    ],
}
total_video = "0"


# - - - - - - - - Do not edit below this line - - - - - - - -

try:
    total_video = open("videos.txt", "r").read()
except FileNotFoundError:
    open("videos.txt", "w").write("0")


def write_tvideos(to_add):
    open("videos.txt", "w").write(str(to_add))


print(f"Total {len(channel.videos)} videos")


async def main():
    await client.start()
    total_videos = int(total_video)
    for vids in range(total_videos, len(channel.videos)):
        video_id = search(r"\?v=([(\w+)\-]*)", channel.videos[vids]["link"]).group(1)
        print(f"Downloading {vids+1}")
        info = YoutubeDL(opts).extract_info(youtube_link.format(video_id))
        system(f"wget -qO {info['id']}.jpg " + thumbnail_link.format(info["id"]))
        files = glob(f"{info['id']}*")
        thumb, video = "", ""
        for file in files:
            if file.endswith(".jpg"):
                thumb = file
            else:
                video = file
        if getsize(thumb) == 0:
            thumb = None
        await client.send_video(
            TG_CHANNEL_ID,
            video,
            caption=f"`{info['title']}`",
            thumb=thumb,
            duration=info["duration"],
            height=info["height"],
            width=info["width"],
            file_name=info["title"],
        )
        total_videos += 1
        system(f"rm {info['id']}*")
        print(f"Completed {total_videos}")
        write_tvideos(total_videos)
    print(f"Completed {total_videos}")
    await client.stop()


client.run(main())
