# YT-Channel-Downloader
- Download all videos from a youtube channel and upload in a telegram channel.
- Re-run to get newly uploaded videos.
---
## Dependency
- `ffmpeg` and `python3` are required along with the following python libraries:
`pyrogram`, `tgcrypto`, `youtube-search-python`, `yt-dlp`, `python-decouple`
---
## Installation
- `sudo bash installer.sh`
---
## Variables
- `API_ID` - Get it from https://my.telegram.org
- `API_HASH` - Get it from https://my.telegram.org
- `BOT_TOKEN` - Get it from [botfather](t.me/botfather)
- `TG_CHANNEL_ID` - Telegram Channel ID where the videos should be sent.
- `YT_CHANNEL_LINK` - Youtube Channel link from where the videos should be downloaded.
---
## Run
- `python backup.py`
---
## Using GitHub Actions
- Click [this](https://github.com/buddhhu/Yt-Channel-Downloader/generate).
- Edit line 7 of `.github/workflows/run.yml` with your GitHub username.
- Add `GIT_EMAIL` with your email used in GitHub account, in secrets.
- Add [variables](#variables) in secrets.
