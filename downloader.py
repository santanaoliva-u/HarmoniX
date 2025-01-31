# downloader.py
import os
import yt_dlp
import config

def descargar_musica(artista):
    """Descarga la primera canción que encuentra en YouTube del artista especificado."""
    print(f"\n🔍 Buscando música de: {artista} en YouTube...")
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'extract_audio': True,
        'audio_format': 'mp3',
        'outtmpl': os.path.join(config.OUTPUT_FOLDER, '%(title)s.%(ext)s'),
        'noplaylist': True,
        'quiet': False,
    }

    os.makedirs(config.OUTPUT_FOLDER, exist_ok=True)

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([f"ytsearch1:{artista}"])
        print(f"✅ Descarga completada: {artista}")
    except Exception as e:
        print(f"❌ Error en la descarga: {e}")

