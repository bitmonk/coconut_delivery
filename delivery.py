#!/usr/bin/env python

import sys, logging

DEFAULT_FILENAME = 'flight_paths.txt'

if len(sys.argv) > 1:
  infilename = sys.argv[1]
else:
  infilename = DEFAULT_FILENAME

logger = logging.getLogger('coconut_delivery')
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())

pathfile = open(infilename)

const_energy = None

jet_streams = []

for line in pathfile:
  if not const_energy:
    const_energy = int(line)
  else:
    jet_streams.append([ int(i) for i in line.split(' ')])

logger.info("Constant Energy required to fly one mile: %s" % const_energy)
logger.info("Jet Streams: %s" % jet_streams)

