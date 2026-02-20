#!/usr/bin/env python

apparentMagnitude = float(input("Please enter the apparent magnitude: "))
absoluteMagnitude = float(input("Please enter the absolute magnitude: "))

# The distance is related to the magnitudes as m-M=5.Log(d/10)
# 1 Parsec = 3.26164 ly

m = apparentMagnitude
M = absoluteMagnitude

d = 10.0 * pow( 10.0, (m-M)/5.0 ) * 3.26164
dl = d * 3.26164
print(f"The distance to sirius is {dl} lightyears, or {d} parsecs.")




