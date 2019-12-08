# TuxTaper
TuxTaper es un reproductor de medios que soporta volcados de cinta TZX/CDT usados por emuladores de ZX Spectrum y Amstrad CPC y diversos formatos de audio.
Esta pensado para usarse con una raspberry pi mediante una pantalla hat pero se puede usar en cualquier GNU/Linux y otros sistemas.

![TuxTaper screenshot](https://raw.githubusercontent.com/cpcbegin/tuxtaper/master/graphics/tuxtaper_screenshot.png)


## Instalación
Descárgate los archivos a cualquier carpeta.
Para que funcione tienes que instalar los siguientes paquetes en tu distro:
- python3
- python3-minimal
- python3-pyqt5
- python3-tkinter
- python3-python-utils
- python3-setuptools
- python3-pyqt5.qtmultimedia

Y los siguientes mediante el comando `pip3 install paquete`:
- pygame

## Uso
Ejecuta el siguiente comando desde la carpeta donde hayas descargado:

`python3 tuxtaper.py`


## Por hacer (@TO_DO)
Es una versión preliminar por lo que puede tener muchos fallos y cosas por mejorar, en concreto:
- Soportar más formatos.
- Mejorar aspecto.
- Optimizar el código.
- Ver si hay casos en los que pasen cosas extrañas.
- Mejorar esta ayuda.
- Hacerlo adaptativo al tamaño disponible de pantalla.
- Reducir el número de librerías necesarias para reducir uso de recursos y facilitar el uso multisistema.