# converter.py
import os
import ffmpeg
import config

def convertir_a_mp3(video_path):
    """Convierte un archivo de video a MP3."""
    nombre_base = os.path.splitext(os.path.basename(video_path))[0]
    mp3_path = os.path.join(config.CONVERSION_FOLDER, f"{nombre_base}.mp3")

    os.makedirs(config.CONVERSION_FOLDER, exist_ok=True)

    if os.path.exists(mp3_path):
        print(f"🔹 {mp3_path} ya existe, saltando...")
        return

    print(f"🎵 Convirtiendo {video_path} -> {mp3_path} ...")
    try:
        ffmpeg.input(video_path).output(mp3_path, format='mp3', audio_bitrate='192k').run(overwrite_output=True)
        print(f"✅ Conversión completa: {mp3_path}")
    except Exception as e:
        print(f"❌ Error al convertir {video_path}: {e}")

