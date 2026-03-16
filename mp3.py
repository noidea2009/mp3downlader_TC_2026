import os
from yt_dlp import YoutubeDL

def download_mp3(url):
    # Get path to user's Downloads folder
    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads", "mp3_downloads")

    # Create the folder if it doesn't exist
    os.makedirs(downloads_folder, exist_ok=True)

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": f"{downloads_folder}/%(title)s.%(ext)s",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


if __name__ == "__main__":
    link = input("Enter YouTube link: ")
    download_mp3(link)