# Stahovani videi z Youtube a prevod do mp3

> Tento skript umi stahovat a konvertovat videa a playlisty do samostatných MP3 souborů pomocí yt-dlp, přeskakovat blokovaná videa a
> pokračovat ve stahování dalších.


## Po instalaci dle OS uz je doinstalujeme v terminalu na windows i linux:

> ``` pip3 install pip pytube pydub yt-dlp ffmpeg ffprobe --upgrade --break-system-packages ```
>

## Pripadne vyresit 

## Na windows:

>> ``` do C:\Windows\System32 nakopirovat po rozbaleni z webu [Ffmpeg binaries](https://ffbinaries.com/downloads) ffmpeg.exe, ffprobe.exe ```
>>
> 
## Pokud nepujde tak

[Návod ffmpeg](https://www.redswitches.com/blog/install-ffmpeg-on-windows/)

[Environment variables](https://www.computerhope.com/issues/ch000549.htm)

Ujistěte se, že máte nainstalovaný [Ffmpeg binaries](https://ffbinaries.com/downloads), [Ffmpeg](https://www.ffmpeg.org/download.html), [Python](https://www.python.org/downloads/) a yt-dlp používá pro konverzi videí.

## Na linuxu: 

> ```sudo apt install python3-pip ffmpeg python3-full```
>



## Skripty

1) staci spustit ```python download_songs.py``` - skript stahne a prevede z youtube, prohledava jiz vytvorene mp3 

2) pridavat URL z youtube do ```songs.txt``` - jediny soubor na editaci,  s URL pisnicek i s playlistu, kazdy odkaz vzdy v novem radku

*napr.*

> https://www.youtube.com/watch?v=8mYd2X_9rrs&pp=ygUJcGVuZHVsdW0g
> 
> https://www.youtube.com/watch?v=__Swm8c_AeI&list=PLXV0L61pV8hfX-GFEKvwgjdk4f3BRE5qK
> 


3) adresar downloaded_songs - automaticky vytvoreny adresar se stazenymi mp3, vytvoreny vzdy tam kde se spousti python skript

