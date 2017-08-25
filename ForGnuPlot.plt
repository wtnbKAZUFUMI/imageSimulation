#usually "st" = 0, and "to" is the end of picture number
#offset is usually 1
set pm3d map
st = 0
to = 46655
offset = 1
do for[i = st : to : offset]{
    input = sprintf("../results/txt/%d_ForGnuPlot.txt", i)
    set term png
    set output sprintf("../results/png/_%03d_ForGnuPlot.png", i)
    set cbrange[0.0:60.0]
    splot input
    set output
}

