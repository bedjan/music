# Stahovani z Youtube

> Tento skript by měl správně vyhledávat názvy písní, stahovat a konvertovat videa a playlisty do samostatných MP3 souborů pomocí yt-dlp, přeskakovat blokovaná videa a
> pokračovat ve stahování dalších. Ujistěte se, že máte nainstalovaný ffmpeg, který yt-dlp používá pro konverzi videí.

sudo apt install python3-pip ffmpeg python3-full

pip3 install pip pytube pydub yt-dlp --upgrade --break-system-packages 


[Ffmpeg](https://www.ffmpeg.org/download.html)

[Python](https://www.python.org/downloads/)

# Skripty

1) download_songs.py  - skript stahne a prevede z youtube, prohledava jiz vytvorene mp3 

2) songs.txt - jediny soubor na editaci,  s URL pisnicek i s playlistu, kazdy odkaz vzdy v novem radku

*napr.*

> https://www.youtube.com/watch?v=8mYd2X_9rrs&pp=ygUJcGVuZHVsdW0g
> 
> https://www.youtube.com/watch?v=__Swm8c_AeI&list=PLXV0L61pV8hfX-GFEKvwgjdk4f3BRE5qK
> 


 adresar downloaded_songs - automaticky vytvoreny adresar se stazenymi mp3, vytvoreny vzdy tam kde se spousti python skript

