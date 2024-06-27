# Stahovani z Youtube

> Tento skript by měl správně vyhledávat názvy písní, stahovat a konvertovat videa a playlisty do samostatných MP3 souborů pomocí yt-dlp, přeskakovat blokovaná videa a
> pokračovat ve stahování dalších. Ujistěte se, že máte nainstalovaný ffmpeg, který yt-dlp používá pro konverzi videí.

sudo apt install python3-pip ffmpeg python3-full

pip3 install pip pytube pydub yt-dlp --upgrade --break-system-packages 


[Ffmpeg](https://www.ffmpeg.org/download.html)

[Python](https://www.python.org/downloads/)

# Skripty

download_songs.py  - skript stahne a prevede z youtube, prohledava jiz vytvorene mp3 

songs.txt - soubor s nazvy pisnicek

> Unique II - Break My Stride
> https://www.youtube.com/watch?v=nZXRV4MezEw&list=PLmXxqSJJq-yUvMWKuZQAB_8yxnjZaOZUp
>
> 

adresar downloaded_songs - automaticky vytvoreny adresar se stazenymi mp3, vytvoreny vzdy tam kde se spousti python skript

