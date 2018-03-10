#!/usr/bin/env python

from event import Event
from fileio import write

f = open("test.odf","wb")
ev = Event()
ev.runID = 1009322
ev.year = 2007
ev.startTime = long(10908290000809370)
ev.eventLength = 100000000.
ev.triggers = [(10000.00,"BLEH")]
ev.hits = [(1.0,1000.4,100.,-100.,255.)]

write(f,ev)

