import numpy as np
import matplotlib.pyplot as plt
import math as m
from PIL import Image
from decimal import Decimal
# -*- coding: cp1252 -*-


pil1=Image.open('baixoContraste.jpg')
(l,h)=pil1.size
print(l,h)

#capturando o nÃºmero de pixels com cada intensidade (0-255)
# e salvando na lista groups as intensidades com mais de 10000 pixels
intensities = list()
newIntensities = list()
pr = list()
#groups = list()
for intensidade, quantidade in enumerate(pil1.histogram()):
    intensities.append(quantidade)
    print (intensidade, quantidade)
    #aux = Decimal (0.7777777777)
    aux = (float (quantidade) / (l*h))

    pr.append(aux)
    #novaIntensidade = ((768 - 1) / (l*h))
    #print m.fsum(pr)
    aux2 = (float(768 - 1) / (l*h) * (m.fsum(pr)))
    #print aux2
    newIntensities.append(aux2)
    #if value > 10000:
    #    groups.append (i)

plt.hist(range(len(intensities)), bins = len(intensities), normed = False, weights = intensities, cumulative = False, bottom = None, histtype = 'barstacked', align = 'mid', orientation = 'vertical', color='gray')
#print len(intensities)

#print (groups)

Iout=Image.new('RGB', (l,h))

#criando uma lista de cores que será associada a cada grupo (lista groups) de pixels
color = [(255, 255, 50), (252, 152, 23), (123, 228, 180), (20, 20, 20)]

#associando cada pixel a uma cor, conforme o grupo que este se encaixa
#obs: o limite entre dois grupos é dado pela média entre os valores de intensidades
#ex: se grupo1 = 250 e grupo 2 = 0, pixels com intensidade menor que 125
#serão coloridos como parte do grupo 2
for i in intensities:
    {}.fromkeys(newIntensities[i], i)

for j in range(0, h):
    for i in range(0, l):
        val=pil1.getpixel((i,j))
        if val[0] > 256:
            print val
#        if val < np.mean(groups[0:2]):
        temp = 256 * newIntensities[val[0]]
        print temp
        #cor = (0, 0, newIntensities[100])
        #Iout.putpixel((i,j),cor)
#        elif val >= np.mean(groups[0:2]) and val < np.mean(groups[1:3]):
#            Iout.putpixel((i,j),color[1])
#        elif val >= np.mean(groups[1:3]) and val < np.mean(groups[2:]):
#            Iout.putpixel((i,j),color[2])
#        else:
#            Iout.putpixel((i,j),color[3])

Iout.save("saida.jpg","JPEG")

plt.show()



