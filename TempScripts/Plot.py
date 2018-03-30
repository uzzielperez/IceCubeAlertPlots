import pyfits
import numpy as np
import pylab as pl
from matplotlib.patches import Ellipse

pl.rcParams['figure.figsize'] = (14.0, 12.0)
pl.rcParams['font.size'] = 15
pl.rcParams['font.family'] = 'serif'

def pol2vec(ra, dec):
    phi = (360 - ra) * np.pi / 180.
    theta = (90 - dec) * np.pi / 180.

    x = np.sin(theta) * np.cos(phi)
    y = np.sin(theta) * np.sin(phi)
    z = np.cos(theta)

    r = np.sqrt(x**2 + y**2 + z**2)

    return (x/r, y/r, z/r)

def dotprod(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

def openingAngle(lon1, lat1, lon2, lat2):
    a = pol2vec(lon1, lat1)
    b = pol2vec(lon2, lat2)

    dp = dotprod(a,b)
    return np.arccos(dp) * 180. / np.pi

def getCatPositions(filename = "gll_psch_v13.fit"):
    hdulist = pyfits.open(filename)
    h, data, columns = hdulist[1].header, hdulist[1].data, hdulist[1].columns
    try:
        return (data['RAJ2000'], data['DEJ2000'], data['ASSOC1'])
    except KeyError:
        return (data['RAJ2000'], data['DEJ2000'], data['ASSOC'])

def drawCircle(ax, ra, dec, radius, **kwargs):
    circle = pl.Circle((ra, dec), radius, **kwargs, fill=False)
    ax.add_artist(circle)

fig = pl.figure(figsize=(12,10))
ax = fig.add_subplot(111)

fermiCats = {
    '3FGL': '/Users/up/Desktop/IceCube/Fermi-Neutrino alerts/gll_psc_v16.fit',
    '2FHL': '/Users/up/Desktop/IceCube/Fermi-Neutrino alerts/gll_psch_v09.fit',
    '3FHL': '/Users/up/Desktop/IceCube/Fermi-Neutrino alerts/gll_psch_v13.fit'
}

# Plot 3FHL sources
srcs_3fhl = getCatPositions(fermiCats.get('3FHL'))
ax.scatter(srcs_3fhl[0], srcs_3fhl[1], color='crimson', label='3FHL', alpha=0.5, s=100)

for s in np.array(srcs_3fhl).T:
    if openingAngle(float(s[0]), float(s[1]), RA0, Dec0) < Box:
        ax.annotate(s[2], (float(s[0])-0.2, float(s[1])-0.3), color='crimson', horizontalalignment='left', verticalalignment='center', fontsize=12)

# Plot 2FHL sources
srcs_2fhl = getCatPositions(fermiCats.get('2FHL'))
ax.scatter(srcs_2fhl[0], srcs_2fhl[1], color='orange', marker='x', label='2FHL', s=100)

# Plot 3FGL sources
srcs_3fgl = getCatPositions(fermiCats.get('3FGL'))
ax.scatter(srcs_3fgl[0], srcs_3fgl[1], color='none', edgecolor='blue', s=300, label='3FGL', linewidth=2)

for s in np.array(srcs_3fgl).T:
    if openingAngle(float(s[0]), float(s[1]), RA0, Dec0) < Box:
        ax.annotate(s[2], (float(s[0])-0.3, float(s[1])), color='blue', horizontalalignment='left', verticalalignment='center', fontsize=12)

# Read BZCat
bzcat = np.genfromtxt("/Users/up/Desktop/IceCube/Fermi-Neutrino alerts/5bzu.dat", delimiter=',', dtype=None, names=True)

# Parse BZCat strings
def procRA(s):
    #print(s)
    l = str(s).split(' ')
    ra = 15 * (float(l[1]) + float(l[2])/60. + float(l[3])/3600.)
    return ra 

def procDec(s):
    #print(s)
    l = str(s).split(' ')
    dec = np.abs(float(l[1])) + float(l[2])/60. + float(l[3])/3600.

    if '-' in l[1]:
        return -dec
    else:
        return dec
ra_bzcat = [procRA(s) for s in bzcat['RA']]
dec_bzcat = [procDec(s) for s in bzcat['Dec']]

ax.scatter(ra_bzcat, dec_bzcat, color='#666666', label='BZCat')

for s in bzcat:
    ra = procRA(s['RA'])
    dec = procDec(s['Dec'])
    name = str(s['Source_Name']).split('\'')
    if openingAngle(ra, dec, RA0, Dec0) < Box: 
        ax.annotate(name[1], (ra-0.1, dec+0.3), color='#666666', horizontalalignment='left', verticalalignment='center', fontsize=12, clip_on=True)

# Plot neutrino position
ax.scatter(RA0, Dec0, color='crimson', marker='x', label='IC170922 - GCN', s=100)
xe = RA0 + (dRAhi - dRAlo)/2.
ye = Dec0 + (dDechi - dDeclo)/2.
e = Ellipse(xy=(xe,ye), width=dRAhi+dRAlo, height=dDechi+dDeclo, linewidth=2, edgecolor='crimson', facecolor='none')
ax.add_artist(e)
e.set_alpha(1.)

# Legend outside the plot
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

# Limits, labels and grid
ax.set_xlim(RA0+Box, RA0-Box)
ax.set_ylim(Dec0-Box, Dec0+Box)
ax.set_xlabel(r'$\alpha_{2000}$ [$^{\circ}$]')
ax.set_ylabel(r'$\delta_{2000}$ [$^{\circ}$]')
ax.grid(linestyle='--', linewidth=0.5)
