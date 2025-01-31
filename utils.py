# utils.py
def mostrar_menu():
    """Muestra el menú principal decorado y solicita una opción."""
    print("\n" + "="*40)
    print("🎵  Bienvenido al Music Downloader  🎵")
    print("="*40)
    print("1️⃣  Descargar música de YouTube")
    print("2️⃣  Convertir video a MP3")
    print("3️⃣  Salir")
    print("="*40)
    return input("👉  Selecciona una opción: ").strip()

