#!/usr/bin/env python

from event import Event
from fileio import read
import gzip

f = gzip.open("test.odf.gz","rb")

ev = read(f)

print ev

