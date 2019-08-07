reset
n=10 #number of intervals
max=100. #max value
min=0. #min value
width=1

set term png #output terminal and file
set output "TesteWithout.png"
set xrange [min:max]
set yrange [0:100]

set xlabel "Number of nodes"
set ylabel "Latency (ms)"
set key right bottom 

plot "datafileLatencyNoCCANoAckDoubleN.dat" using 1:2  title "Dois Caminhos" with lines lt 1, "" using 1:2:3:4 with yerrorbars lt 1, \
 "datafileLatencyNoCCANoAckDoubleNS.dat" using 1:2  title "Minimiza Latencia" with lines lt 2, "" using 1:2:3:4 with yerrorbars lt 2,
