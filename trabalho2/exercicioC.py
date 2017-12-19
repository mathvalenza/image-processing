import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
# -*- coding: cp1252 -*-


pil1=Image.open('aorta1.jpg')#rins1.jpg
(l,h)=pil1.size
print(l,h)

#capturando o numero de pixels com cada intensidade (0-255)
# e salvando na lista groups as intensidades com mais de 10000 pixels
intensities = list()
#groups = list()
for i, value in enumerate(pil1.histogram()):
    intensities.append(value)
    if value > 200:
        print (value, i)
        #groups.append (i)

plt.hist(range(len(intensities)), bins=len(intensities), normed = False, weights = intensities, cumulative = False, bottom = None, histtype = 'barstacked', align = 'mid', orientation = 'vertical', color='gray')
#print len(intensities)
#print (groups)

Iout=Image.new('RGB', (l,h))

#criando uma lista de cores que será associada a cada grupo (lista groups) de pixels
color = (255, 0, 0)

#associando cada pixel a uma cor, conforme o grupo que este se encaixa

for j in range(0, h):
    for i in range(0, l):
        val=pil1.getpixel((i,j))
        if val[0] >= 122 and val[0] <= 256:
            Iout.putpixel((i,j),color)
        else:
            Iout.putpixel((i,j),val)
        #RINSif val[0] <= 256 and val[0] >= 150:
        #RINS    Iout.putpixel((i,j),color)

Iout.save("saidaC_aorta.jpg","JPEG")
#Iout.save("saidaC_rins.jpg","JPEG")

plt.show()



