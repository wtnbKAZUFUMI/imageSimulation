#!/bin/bash
cat ../../conf.py
python convVer3.py
python ImageToMatrixForGnuPlot.py
gnuplot ForGnuPlot.plt
echo plot succesfully finished
convert -delay 0.5 -loop 0 ../results/png/_*_ForGnuPlot.png ../results/plot.gif
echo gif file generated
python LongExposure.py
