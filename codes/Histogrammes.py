# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import matplotlib.pyplot as plt
from numpy.random import normal
from numpy.random import randn

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

i = 1 #On va de 1 à 11 (10 itérations) pour les 10 tailles de mem
while(i <= 10):
    j = 1 #On fait trois technologies (1 à 3) j est aussi l'indice dans le tableau qui donne la technologie 
    while (j <= 3):
        iterationNbr = 0 #On a 100 données par techno
        while (iterationNbr < 100):
            dataToPlot.append(float(data[iterationNbr+100*(i-1)][j]))
            iterationNbr+=1
        plt.clf()
        plt.hist(dataToPlot, bins=10)
        plt.title("Histogramme : technologie n°"+str(j)+", taille "+str(i*10))
        plt.xlabel("Temps d'attente (ms)")
        plt.ylabel("Nombre d'occurences")
        plt.savefig("../img/"+str(j)+"-"+str(i*10)+".png", bbox_inches='tight')
        dataToPlot = []
        j+=1
    i+=1