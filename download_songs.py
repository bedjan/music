import os
import subprocess

def download_playlist(playlist_url, output_path):
    command = [
        'yt-dlp', '--ignore-errors', '--format', 'bestaudio', '--extract-audio',
        '--audio-format', 'mp3', '--audio-quality', '160K',
        '--output', os.path.join(output_path, '%(title)s.%(ext)s'), '--yes-playlist',
        playlist_url
    ]
    subprocess.run(command)

def main(input_file, output_path):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    for line in lines:
        line = line.strip()
        if line:
            print(f"Processing {line}...")
            download_playlist(line, output_path)

if __name__ == '__main__':
    input_file = 'songs.txt'  # Path to the input file with playlist URLs
    output_path = 'downloaded_songs'  # Directory to save the MP3 files
    main(input_file, output_path)
