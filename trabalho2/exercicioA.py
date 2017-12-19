import numpy as np
import math as m
import matplotlib.pyplot as plt
from PIL import Image
# -*- coding: cp1252 -*-

imagem = 'marilyn.jpg'
pil1=Image.open(imagem)
(l,h)=pil1.size
print(l,h)

# capturando o numero de pixels com cada intensidade
# e salvando na lista intensities, onde intensities[i] representa
# a quantidade de pixels com a intensidade i

intensities = list()
for i, value in enumerate(pil1.histogram()):
    intensities.append(value)

# plotando o histograma
plt.hist(range(len(intensities)), bins=len(intensities), normed = False, weights = intensities, cumulative = False, bottom = None, histtype = 'barstacked', align = 'mid', orientation = 'vertical', color='gray')
titulo = "Histograma de " + imagem
plt.title(titulo)

# pegando o histograma so ate 256
intensities = intensities[0:len(intensities)/3]

# dividindo as intensidades em tres grupos de
# mesmo tamanho e printando
# para quantificar a diferenca visualizada no histograma

lowIntensities = intensities[0:len(intensities)/3]
sumLowIntensities = int (m.fsum(lowIntensities))

mediumIntensities = intensities[len(intensities)/3:2*(len(intensities)/3)]
sumMediumIntensities = int (m.fsum(mediumIntensities))

highIntensities = intensities[2*(len(intensities)/3):3*(len(intensities)/3)]
sumHighIntensities = int (m.fsum(highIntensities))

print (sumLowIntensities, sumMediumIntensities, sumHighIntensities)

plt.show()



