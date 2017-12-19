import matplotlib.pyplot as plt
from PIL import Image
# -*- coding: cp1252 -*-

pil1=Image.open('pepinos.jpg')
(l,h)=pil1.size
print(l,h)

#capturando o nÃºmero de pixels com cada intensidade (0-255)
intensities = list()
groups = list()

for i, value in enumerate(pil1.histogram()):
    #print (i, value)
    intensities.append(value)
    if value > 10000:
        groups.append (i)

#plotando o histograma
plt.hist(range(256), bins=256, weights = intensities, histtype = 'barstacked', align = 'mid', color='gray')

print (groups)

Iout=Image.new('RGB', (l,h))

# criando uma lista de cores
color = [(0, 0, 250), (0, 0, 0)]

#associando cada faixa ilegível a uma cor específica
# e transformando os tons de cinza legíveis em tons de verde
for j in range(0, h):
    for i in range(0, l):
        val=pil1.getpixel((i,j))
        if val > 7 and val < 11:
            Iout.putpixel((i,j),color[0])
        elif val > 250 and val < 254:
            Iout.putpixel((i,j),color[1])
        else:
            Iout.putpixel((i,j),(0, val, 0))

Iout.save("Iout2.jpg","JPEG")
plt.show()



