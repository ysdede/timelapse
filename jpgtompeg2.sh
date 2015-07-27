#!/bin/bash
mencoder mf://*.jpg -mf w=1920:h=1080:fps=25:type=jpg -of mpeg -ovc lavc -lavcopts vcodec=mpeg2video:threads=4:vbitrate=10000000 -oac copy -o output25fps.mpg -nosound
