set terminal png size 800,600
f(x) = a*x + b
g(x) = c*x + d
h(x) = e*x + f
set xlabel "Taille de la mémoire"
set ylabel "Temps d'attente"
set title "Technologie 1"
set output "../img/techno1.png"
fit f(x) "../donnees/Q12_donnee.dat" using 1:2 via a, b
plot f(x) title 'fit techno1', '../donnees/Q12_donnee.dat' using 1:2 title 'Technologie 1'
stats "../donnees/Q12_donnee.dat" using 1:2 name "A"
set label 1 sprintf("r = %4.2f",A_correlation) at graph 0.1, graph 0.85

set title "Technologie 2"
set output "../img/techno2.png"
fit g(x) "../donnees/Q12_donnee.dat" using 1:3 via c,d
plot g(x) title 'fit techno2' lt rgb "red" , '../donnees/Q12_donnee.dat' using 1:3 title 'Technologie 2' lt rgb "blue"
stats "../donnees/Q12_donnee.dat" using 1:3 name "B"
set label 1 sprintf("r = %4.2f",B_correlation) at graph 0.1, graph 0.85

set title "Technologie 3"
set output "../img/techno3.png"
fit h(x) "../donnees/Q12_donnee.dat" using 1:4 via e,f
plot h(x) title 'fit techno3' lt rgb "black" , '../donnees/Q12_donnee.dat' using 1:4 title 'Technologie 3' lt rgb "orange"
stats "../donnees/Q12_donnee.dat" using 1:4 name "C"
set label 1 sprintf("r = %4.2f",C_correlation) at graph 0.1, graph 0.85

set title "Comparaison des 3 technologies"
set output "../img/RAM.png"

plot f(x) title 'Régression linéaire technologie 1', g(x) title 'Régression linéaire technologie 1', h(x) title 'Régression linéaire technologie 3'
