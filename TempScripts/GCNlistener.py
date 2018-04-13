import gcn
import sys
import subprocess as sp
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

# GCN alert delivers amonfile. We parse it with amonParser.py. Call loadAMON(amonfile) to
# Test #
amonfile = '17569642_130214.amon'
#amonfile = '34032434_130171.amon' 

RASC, DRAHI, DRALO, DEC, DDECHI, DDECLO, BOX, EVNUM, RUN = loadAMON(amonfile) 

# When loadAMON is called, we run Plot.py and supply arguments
# python Plot.py  -ra RASC -rh  DRAHI -rl DRALO -d DEC -dh DDECHI -dl DDECLO -b BOX"
bashcmd = 'python Plot.py -ra %d -rh %d -rl %d -d %d -dh %d -dl %d -g %s_%s' %(RASC, DRAHI, DRALO, DEC, DDECHI, DDECLO, EVNUM, RUN) # leave out box in dev stage
process = sp.Popen(bashcmd.split(), stdout=sp.PIPE)
output, error = process.communicate()
#status = sp.Popen.poll(process) # status should be 'None'
#sp.Popen.terminate(process) #closes the process
#status = sp.Popen.poll(process) # status not 'None'
#--------------

# end Plot.py. Continuously listen to GCN
