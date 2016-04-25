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
sigmas = []
mus = []
Z = 1.96
n = 100 # Pour la moyenne (on a 100 données)

i = 1 #On va de 1 à 11 (10 itérations) pour les 10 tailles de mem
while(i <= 10):
    j = 1 #On fait trois technologies (1 à 3) j est aussi l'indice dans le tableau qui donne la technologie 
    while (j <= 3):
        iterationNbr = 0 #On a 100 données par techno
        muBis = 0 #On fait la somme de tout
        sigmaBis = 0
        while (iterationNbr < 100):
            dataToPlot.append(float(data[iterationNbr+100*(i-1)][j]))
            muBis += (1.0/n)*(float(data[iterationNbr+100*(i-1)][j])) #On ajoute à la somme
            iterationNbr+=1
        iterationNbr = 0 
        while (iterationNbr < 100):
            sigmaBis += (float(data[iterationNbr+100*(i-1)][j])-muBis)*(float(data[iterationNbr+100*(i-1)][j])-muBis)
            iterationNbr+=1
        sigmaBis = (1.0/n)*sigmaBis
        (mu, sigma) = norm.fit(dataToPlot)
        sigmas.append(sigmaBis)
        mus.append(muBis)
        dataToPlot = []
        j+=1
        
    print(str(math.fabs(mus[0]-mus[1]) > Z*math.sqrt( (sigmas[0]/100) + (sigmas[1]/100) ) )),
    print(str(math.fabs(mus[1]-mus[2]) > Z*math.sqrt( (sigmas[1]/100) + (sigmas[2]/100) ) )),
    print(str(math.fabs(mus[0]-mus[2]) > Z*math.sqrt( (sigmas[0]/100) + (sigmas[2]/100) ) )),
    print("\\"+"\\"+"\n")
        
    sigmas = []
    mus = []
    i+=1