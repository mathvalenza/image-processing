import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import math as m

# -*- coding: cp1252 -*-

original=Image.open('Lua1_gray.jpg')
img = np.array(original)
(l,h)=pil1.size
#print(l,h)

passaBaixa=Image.new('RGB', (l,h))

# passo 1: atenuacao do ruido atraves do filtro passa baixa
for j in range(0, h):
    for i in range(0, l):
        val=pil1.getpixel((i,j))
        if (i > 0 and i < l-2):
            if (j > 0 and j < h-2):
                val2 = np.mean([original.getpixel((i-1,j-1)), original.getpixel((i, j-1)),
                                original.getpixel((i+1, j-1)),original.getpixel((i+1, j)),
                                original.getpixel((i+1, j+1)), original.getpixel((i, j+1)),
                                original.getpixel((i+1, j-1)), original.getpixel((i-1, j))])
                passaBaixa.putpixel((i,j),(int (val2),(int (val2)), (int (val2))))
                
        else:
            passaBaixa.putpixel((i,j),val)

passaBaixa.save("passaBaixa.jpg","JPEG")
print "salvou passaBaixa.jpg"

# passo 2.1 e 2.2: gradientes X e Y

img = []
for j in range(0, h):
    linha = []
    for i in range(0, l):
        val=passaBaixa.getpixel((i,j))
        linha.append(val[0])
    linha2 = np.array(linha, dtype=float)
    #print "linha: ",linha2
    img.append(linha2[:])

img2 = np.array(img, dtype=float)
gradX, gradY = np.gradient(img2)

gx=Image.new('RGB', (l,h))
gy = Image.new('RGB', (l,h))

for j in range(0, h):
    for i in range(0, l):
        gx.putpixel((i,j),(int (np.abs(gradX[j][i])),(int (np.abs(gradX[j][i]))), (int (np.abs(gradX[j][i])))))
        gy.putpixel((i,j),(int (np.abs(gradY[j][i])),(int (np.abs(gradY[j][i]))), (int (np.abs(gradY[j][i])))))

gx.save("gradX.jpg","JPEG")
print "salvou gradX.jpg"
gy.save("gradY.jpg","JPEG")
print "salvou gradY.jpg"

# passo 3: Magnitude (S) e Direcao (D)

S = []
D = []

for j in range(0, h-1):
    auxS = []
    auxD = []
    for i in range(0, l-1):
        tempS = m.sqrt((gradX[j][i]**2 + gradY[j][i]**2))
        tempD = m.atan2(gradY[j][i], gradX[j][i])
        auxS.append(tempS)
        auxD.append(tempD)
    S.append(auxS[:])
    D.append(auxD[:])

mag = Image.new('RGB', (l,h))
for j in range(0, h-1):
    for i in range(0, l-1):
        mag.putpixel((i,j),(int(S[j][i]), int(S[j][i]), int(S[j][i])))  

mag.save("matrizMagnitude.jpg","JPEG")
print "salvou matrizMagnitude.jpg"

# passo 5: calculo do maximo local

R = []
tempR = 0

for j in range(0, h-1):
    auxR = []
    for i in range(0, l-1):
        if (i > 0 and i < l-2):
            if (j > 0 and j < h-2):
                vizinhos = []
                angulo = D[j][i]
                angulo = m.degrees(angulo)
                #print "angulo: ",angulo
                if (angulo < 0):
                    angulo = 180 - np.abs(angulo)
                if (angulo < 45/2):
                    #vizinhos = D e F
                    vizinhos.append(S[j][i-1])
                    vizinhos.append(S[j][i+1])
                elif (angulo < 45 + 45/2):
                    #vizinhos = C e G
                    vizinhos.append(S[j-1][i+1])
                    vizinhos.append(S[j+1][i-1])
                elif (angulo < 90 + 45/2):
                    #vizinhos = B e H
                    vizinhos.append(S[j-1][i])
                    vizinhos.append(S[j+1][i])
                elif (angulo < 90 + 45 + 45/2):
                    #vizinhos = A e I
                    vizinhos.append(S[j-1][i-1])
                    vizinhos.append(S[j+1][i+1])
                else:
                    #vizinhos = D e F
                    vizinhos.append(S[j][i-1])
                    vizinhos.append(S[j][i+1])

                if (S[j][i] > max(vizinhos)):
                    #print "maximo local"
                    tempR = 1
                else:
                    tempR = 0
                
                auxR.append(tempR)
                
    R.append(auxR[:])


saida = Image.new('RGB', (l,h))
for j in range(0, h):
    for i in range(0, l):
        val=passaBaixa.getpixel((i,j))
        if (i > 0 and i < l-3 and j > 0 and j < h-2):
            if (R[j][i] == 1):
                saida.putpixel((i,j), val)
        else:
            saida.putpixel((i,j), val)

saida.save("saida.jpg","JPEG")
print "salvou saida.jpg"
