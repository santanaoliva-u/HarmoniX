# main.py
import os
import time
import downloader
import converter
import config
from utils import mostrar_menu

def main():
    while True:
        opcion = mostrar_menu()
        if opcion == "1":
            artista = input("\n🎤 Ingresa el nombre del artista: ").strip()
            if artista:
                downloader.descargar_musica(artista)
            else:
                print("❌ No ingresaste ningún artista.")

        elif opcion == "2":
            ruta = input("\n📂 Ingresa la ruta del archivo de video: ").strip()
            if os.path.exists(ruta):
                converter.convertir_a_mp3(ruta)
            else:
                print("❌ El archivo no existe.")

        elif opcion == "3":
            print("\n🚀 Saliendo del programa...")
            time.sleep(1)
            break

if __name__ == "__main__":
    main()

