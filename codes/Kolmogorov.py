# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from scipy.stats import norm
import scipy.stats as stats
import matplotlib.pyplot as plt
from numpy.random import normal
import matplotlib.mlab as mlab
from numpy.random import randn
import math

#On prend les lignes, fait un tableau pour chaque ram et chaque nombre d'acces
currentFirstColVal = 10
data = [[0 for x in range(4)] for x in range(1000)]
i = 0
with open("../donnees/Q12_donnee.dat") as f:
    for line in f:
        split_line = line.split()
        data[i][0] = split_line[0]
        data[i][1] = split_line[1]
        data[i][2] = split_line[2]
        data[i][3] = split_line[3]
        i+=1

techno = 0
taille = 0
dataToPlot = []
n = 100 # Pour la moyenne (on a 100 données)

i = 1 #On va de 1 à 11 (10 itérations) pour les 10 tailles de mem
while(i <= 10):
    j = 1 #On fait trois technologies (1 à 3) j est aussi l'indice dans le tableau qui donne la technologie 
    while (j <= 3):
        iterationNbr = 0 #On a 100 données par techno
        while (iterationNbr < 100):
            dataToPlot.append(float(data[iterationNbr+100*(i-1)][j]))
            iterationNbr+=1
        (mu, sigma) = norm.fit(dataToPlot)
        value=stats.kstest(dataToPlot,'norm',(mu, sigma),len(dataToPlot))[0]
        dalpha=0.134
        print (str(value)+" & "+str(dalpha)+"&"),
        dataToPlot = []
        j+=1
    print("\\"+"\\"+"\n")
    i+=1