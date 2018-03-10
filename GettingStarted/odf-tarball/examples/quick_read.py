#!/usr/bin/env python

from event import Event
from fileio import read

f = open("test.odf","rb")

ev = read(f)

print ev

