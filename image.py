
# Descarga de imágenes
# ==============================================================================
from urllib.request import urlretrieve

# Imagen con una sola cara
url = ('https://github.com/JoaquinAmatRodrigo/Estadistica-machine-learning-python/' +
       'raw/master/images/phil_dunphy.jpg')
urlretrieve(url=url, filename='images/imagen_1.jpg')

# Imagen con múltiples caras
url = ('https://github.com/JoaquinAmatRodrigo/Estadistica-machine-learning-python/'
       'raw/master/images/modernfamily.jpg')
urlretrieve(url=url, filename='images/imagen_2.png');

