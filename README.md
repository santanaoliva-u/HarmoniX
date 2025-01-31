---
## **README.md Mejorado**  

```md
# 🎵 HarmoniX - Descarga y Convierte Música Fácilmente 🎧  

HarmoniX es una herramienta poderosa y fácil de usar que te permite **descargar música de YouTube** y **convertir videos a MP3** de manera rápida y eficiente. Perfecto para los amantes de la música que quieren su colección en formato de audio.  

---

## 🚀 Características  
✅ **Descarga música** desde YouTube en formato MP3  
✅ **Convierte videos** a MP3 con alta calidad  
✅ **Interfaz de terminal intuitiva y decorada**  
✅ **Compatible con Windows, Linux (Ubuntu, Kali, Arch)**  
✅ **Código modular y optimizado**  

---

## 📌 **Requisitos**  
Antes de instalar **HarmoniX**, asegúrate de tener:  
- **Python 3.7 o superior** (`python --version`)  
- **pip (gestor de paquetes de Python)**  
- **ffmpeg** (para la conversión de audio)  
- **yt-dlp** (para la descarga de música)  

---

## 🛠 **Instalación**  

### 🐧 **Linux (Ubuntu, Kali, Arch)**  
Ejecuta los siguientes comandos en la terminal:  

```bash
# 1️⃣ Clona el repositorio
git clone https://github.com/santanaoliva-u/HarmoniX.git
cd HarmoniX

# 2️⃣ Instala dependencias
pip install -r requirements.txt

# 3️⃣ Instala ffmpeg (según tu sistema)
# Ubuntu / Debian / Kali
sudo apt install ffmpeg -y

# Arch Linux
sudo pacman -S ffmpeg

# 4️⃣ Ejecuta la aplicación
python3 main.py
```

### 🖥 **Windows**  
1️⃣ Descarga e instala [Python](https://www.python.org/downloads/)  
2️⃣ Descarga e instala [ffmpeg](https://ffmpeg.org/download.html)  
3️⃣ Abre **CMD** y ejecuta:  

```bash
# 1️⃣ Clona el repositorio
git clone https://github.com/santanaoliva-u/HarmoniX.git
cd HarmoniX

# 2️⃣ Instala dependencias
pip install -r requirements.txt

# 3️⃣ Ejecuta la aplicación
python main.py
```

---

## 🎮 **¿Cómo Usar HarmoniX?**  
1️⃣ Ejecuta `python main.py`  
2️⃣ **Selecciona una opción** en el menú:  
   - **1️⃣ Descargar Música**: Ingresa el nombre del artista  
   - **2️⃣ Convertir Video a MP3**: Especifica la ruta del archivo  
   - **3️⃣ Salir**  

---

## 💡 **Contribuir al Proyecto**  
¿Quieres mejorar **HarmoniX**? Sigue estos pasos:  

1️⃣ **Haz un Fork** en [GitHub](https://github.com/santanaoliva-u/HarmoniX)  
2️⃣ Clona tu fork:  
   ```bash
   git clone https://github.com/TU-USUARIO/HarmoniX.git
   cd HarmoniX
   ```  
3️⃣ Crea una nueva rama para tu contribución:  
   ```bash
   git checkout -b mi-nueva-funcion
   ```  
4️⃣ Realiza tus cambios y súbelos:  
   ```bash
   git add .
   git commit -m "Añadida nueva función"
   git push origin mi-nueva-funcion
   ```  
5️⃣ **Crea un Pull Request** en GitHub  

---

## 📝 **Licencia**  
HarmoniX es un proyecto de código abierto bajo la licencia **MIT**. ¡Úsalo y mejoralo libremente!  

---

🎶 **Disfruta tu música con HarmoniX** 🚀  
🔗 GitHub: [santanaoliva-u/HarmoniX](https://github.com/santanaoliva-u/HarmoniX)  
```

---

## **`requirements.txt`**  

```txt
yt-dlp
ffmpeg-python
colorama
```

---

