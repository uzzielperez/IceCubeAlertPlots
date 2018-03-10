import sys
import pylab as p 
import numpy
import math
from geo_reader import read as read_geo
from fileio import read as read_event
import gzip

colormap = [(math.cos(t),math.sin(t),0) for t in numpy.arange(0,math.pi/2.0,math.pi/200.)] \
           + [(0,math.cos(t),math.sin(t)) for t in numpy.arange(0,math.pi/2.0,math.pi/200.)] \
           + [(math.sin(t),0,math.cos(t)) for t in numpy.arange(0,math.pi/4.0,math.pi/100.)]

def get_color(x,x_min,x_max,colormap):
    f = float(x - x_min)/float(x_max - x_min)
    bin = int(f * (len(colormap) - 1) )
    return colormap[bin]


class EventViewer2D:
    def __init__(self, geofn, odffn):

        geof = open(geofn,"rb")
        self.geo = read_geo(geof)

        if odffn.endswith('.gz') :
            self.odffile = gzip.open(odffn,"rb")
        else:
            self.odffile = open(odffn,"rb")

    def DrawGeometryXProj(self):
        # x projection
        x = [pos[0] for om,pos in self.geo.iteritems() if om[0] ]
        y = [pos[2] for om,pos in self.geo.iteritems() if om[0] ]
        
        p.ylabel("z(m)")
        p.xlabel("x(m)")

        p.plot(x,y,"k.",markersize=1.0)

    def DrawGeometryYProj(self):
        # y projection
        x = [pos[1] for om,pos in self.geo.iteritems() if om[0] ]
        y = [pos[2] for om,pos in self.geo.iteritems() if om[0] ]

        #p.ylabel("z(m)")
        p.xlabel("y(m)")

        p.plot(x,y,"k.",markersize=1.0)

    def NextEvent(self):
        
        ev = read_event(self.odffile)

        if not ev : return None

        min_time = min([h[1] for h in ev.hits])
        max_time = max([h[1] for h in ev.hits])
        
        p.clf()

        p.subplot(121)
        self.DrawGeometryXProj()
        for h in ev.hits :
            color = get_color(h[1],min_time,max_time,colormap)
            p.plot([h[2]],[h[4]],marker="o", c=color)

        p.subplot(122)
        self.DrawGeometryYProj()
        for h in ev.hits :
            color = get_color(h[1],min_time,max_time,colormap)
            p.plot([h[3]],[h[4]],marker="o", c=color)

        p.show()

        return ev
