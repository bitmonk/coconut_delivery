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

position = 0
old_position = None
energy_consumed = 0
for stream in jet_streams:
  start = stream[0]
  end = stream[1]
  energy_required = stream[2]
  if start == position:
    old_position = position
    position = end
    energy_consumed += energy_required
    logger.info("Moved from %s to %s using %s energy" % (old_position, position, energy_required))
  elif start > position:
    energy_consumed += (start - position) * const_energy
  else:
    logger.info("Did not move from %s to %s using %s energy" % (position, end, energy_required))

logger.info("Moved %s positions using %s total energy" % (position, energy_consumed))


