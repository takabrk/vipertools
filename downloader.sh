#!/bin/sh
#YouTube Downloader

if [ -e /usr/local/bin/yt-dlp ]; then
    yt-dlp $1 -f "bestvideo[ext=mp4][width <=? 1920][height <=? 1080]+bestaudio[ext=m4a]/best[ext=mp4]/best" -o "~/Downloads/%(title)s.(ext)s"
   echo "Download movie"
else
    sudo wget https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -O /usr/local/bin/yt-dlp
    sudo chmod a+rx /usr/local/bin/yt-dlp
    echo "Installed yt-dlp"
fi
