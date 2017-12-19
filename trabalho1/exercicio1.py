import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
# -*- coding: cp1252 -*-


pil1=Image.open('mapaEUA.jpg')
(l,h)=pil1.size
print(l,h)

#capturando o nÃºmero de pixels com cada intensidade (0-255)
# e salvando na lista groups as intensidades com mais de 10000 pixels
intensities = list()
groups = list()
for i, value in enumerate(pil1.histogram()):
    intensities.append(value)
    if value > 10000:
        groups.append (i)

plt.hist(range(256), bins=256, normed = False, weights = intensities, cumulative = False, bottom = None, histtype = 'barstacked', align = 'mid', orientation = 'vertical', color='gray')
print len(intensities)
print (groups)

Iout=Image.new('RGB', (l,h))

#criando uma lista de cores que será associada a cada grupo (lista groups) de pixels
color = [(255, 255, 50), (252, 152, 23), (123, 228, 180), (20, 20, 20)]

#associando cada pixel a uma cor, conforme o grupo que este se encaixa
#obs: o limite entre dois grupos é dado pela média entre os valores de intensidades
#ex: se grupo1 = 250 e grupo 2 = 0, pixels com intensidade menor que 125
#serão coloridos como parte do grupo 2
for j in range(0, h):
    for i in range(0, l):
        val=pil1.getpixel((i,j))
        if val < np.mean(groups[0:2]):
            Iout.putpixel((i,j),color[0])
        elif val >= np.mean(groups[0:2]) and val < np.mean(groups[1:3]):
            Iout.putpixel((i,j),color[1])
        elif val >= np.mean(groups[1:3]) and val < np.mean(groups[2:]):
            Iout.putpixel((i,j),color[2])
        else:
            Iout.putpixel((i,j),color[3])

Iout.save("Iout.jpg","JPEG")

plt.show()



