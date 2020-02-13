# TuxTaper
TuxTaper es un reproductor de medios que soporta diversos formatos de volcados de cinta usados por emuladores y dispositivos especiales de ordenadores de 8 bits y algunos formatos de audio.
Esta pensado para usarse con una raspberry pi mediante una pantalla hat pero se puede usar en cualquier otro GNU/Linux.

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
- sox

Y los siguientes mediante el comando `pip3 install paquete`:
- pygame

También hay que compilar e instalar los conversores de tzx/cdt (ZX Spectrum / Amstrad CPC), tap (Commodore) y cas (MSX) que están incluidos en cpctools, ubercassette y castools respectivamente:
- ![https://github.com/cpcsdk/cpctools](https://github.com/cpcsdk/cpctools)
- ![https://github.com/DusteDdk/ubercassette](https://github.com/DusteDdk/ubercassette)
- ![https://github.com/joyrex2001/castools](https://github.com/joyrex2001/castools)


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
- Solucionar bug con rutas con espacios.
