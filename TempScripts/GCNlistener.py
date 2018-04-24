import gcn
import sys
import subprocess as sp
from amonParser import loadAMON

#------------- Listen
# See syntax for pygcn listen
#------------- Alert
# When alert is received, parse GCN and pass to Plot.py 
# GCN alert delivers amonfile. We parse it with amonParser.py. Call loadAMON(amonfile) to
# Test amon #
amonfile = '17569642_130214.amon'
#amonfile = '34032434_130171.amon' 

RASC, DRAHI, DRALO, DEC, DDECHI, DDECLO, BOX, EVNUM, RUN = loadAMON(amonfile) 

# When loadAMON is called, we run Plot.py and supply arguments
# python Plot.py  -ra RASC -rh  DRAHI -rl DRALO -d DEC -dh DDECHI -dl DDECLO -b BOX"
bashcmd = 'python Plot.py -ra %d -rh %d -rl %d -d %d -dh %d -dl %d -g %s_%s' %(RASC, DRAHI, DRALO, DEC, DDECHI, DDECLO, EVNUM, RUN) # leave out box in dev stage
process = sp.Popen(bashcmd.split(), stdout=sp.PIPE)
output, error = process.communicate()

# end Plot.py. Continuously listen to GCN
