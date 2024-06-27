import os
import yt_dlp as youtube_dl
from yt_dlp.utils import DownloadError

def download_video_as_mp3(url, output_path, song_title):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_path, song_title + '.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'noplaylist': True,  # Ensure that individual video URLs don't download the whole playlist
        'ignoreerrors': True  # Skip errors and continue downloading
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
        except DownloadError as e:
            print(f"Failed to download {url}: {e}")

def search_youtube(query):
    ydl_opts = {
        'format': 'bestaudio/best',
        'noplaylist': True,  # Ensure that individual video URLs don't download the whole playlist
        'ignoreerrors': True  # Skip errors and continue downloading
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            result = ydl.extract_info(f"ytsearch:{query}", download=False)['entries'][0]
            return result['webpage_url'], result['title']
        except Exception as e:
            print(f"Failed to search for {query}: {e}")
            return None, None

def process_playlist(playlist_url, output_path):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'ignoreerrors': True
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            playlist_info = ydl.extract_info(playlist_url, download=False)
            if playlist_info is None:
                print(f"Failed to extract playlist info {playlist_url}")
                return
            for entry in playlist_info['entries']:
                if entry is None:
                    continue
                video_url = f"https://www.youtube.com/watch?v={entry['id']}"
                song_title = entry['title']
                print(f"Downloading '{song_title}' from playlist...")
                try:
                    download_video_as_mp3(video_url, output_path, song_title)
                    print(f"Downloaded and converted: {os.path.join(output_path, song_title + '.mp3')}")
                except Exception as e:
                    print(f"Failed to download/convert {song_title}: {e}")
        except DownloadError as e:
            print(f"Failed to download playlist {playlist_url}: {e}")

def process_url(url, output_path):
    try:
        yt = youtube_dl.YoutubeDL({'ignoreerrors': True}).extract_info(url, download=False)
        if yt is None:
            print(f"Failed to extract info for {url}")
            return
        song_title = yt['title']
        print(f"Downloading '{song_title}' from URL...")
        download_video_as_mp3(url, output_path, song_title)
        print(f"Downloaded and converted: {os.path.join(output_path, song_title + '.mp3')}")
    except DownloadError as e:
        print(f"Failed to download/convert {url}: {e}")

def process_song(song, output_path):
    url, title = search_youtube(song)
    if url and title:
        print(f"Found '{title}' for '{song}'. Downloading...")
        download_video_as_mp3(url, output_path, title)
    else:
        print(f"Failed to find or download '{song}'.")

def main(input_file, output_path):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    for line in lines:
        line = line.strip()
        if not line:
            continue

        if 'youtube.com/playlist?list=' in line:
            process_playlist(line, output_path)
        elif 'youtube.com/watch?v=' in line:
            process_url(line, output_path)
        else:
            process_song(line, output_path)

if __name__ == '__main__':
    input_file = 'songs.txt'  # Path to the input file with song names, URLs, or playlist URLs
    output_path = 'downloaded_songs'  # Directory to save the MP3 files
    main(input_file, output_path)
