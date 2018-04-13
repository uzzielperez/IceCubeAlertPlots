import gcn
import sys
import subprocess
from amonParser import loadAMON
#------------- Listen
# See syntax for pygcn listen
#------------- Alert
# When alert is received, parse GCN and pass to Plot.py 
#######################################################################
#usage: Plot.py [-h] [-ra RASC] [-rh DRAHI] [-rl DRALO] [-d DEC] [-dh DDECHI]
#               [-dl DDECLO] [-b BOX]
#
#GCN variables.
#
#optional arguments:
#  -h, --help            show this help message and exit
#  -ra RASC, --RAsc RASC
#                        Right Ascension
#  -rh DRAHI, --dRAhi DRAHI
#                        Delta Right Ascension high
#  -rl DRALO, --dRAlo DRALO
#                        Delta Right Ascension low
#  -d DEC, --Dec DEC     Declination
#  -dh DDECHI, --dDechi DDECHI
#                        Delta Declination high
#  -dl DDECLO, --dDeclo DDECLO
#                        Delta Declination low
#  -b BOX, --Box BOX     Box
#########################################################################

#-------------- 
#```bash 
#  
#  condapython Plot.py -ra RASC -rh  DRAHI -rl DRALO -d DEC -dh DDECHI -dl DDECLO -b BOX 
#
#```
## Goes like  
## condapython is an alias to miniconda python3
#--------------
# GCN alert delivers amonfile 
RASC, DRAHI, DRALO, DEC, DDECHI, DDECLO, BOX = loadAMON(amonfile) 

bashcmd = "/path/to/python Plot.py  -ra RASC -rh  DRAHI -rl DRALO -d DEC -dh DDECHI -dl DDECLO -b BOX"
process = subproces.Popen(bashcmd.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
#--------------

# end Plot.py. Continuously listen to GCN
