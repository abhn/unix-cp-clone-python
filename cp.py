#!/usr/bin/python

# Usage: ./cp.py <source> <destination>

from sys import argv

if len(argv) == 1:
	print "Usage: ", argv[0], " <source-file> <destination-file>"
	exit(0)
	
sourceFile = open(argv[1])
sourceData = sourceFile.read()

destFile = open(argv[2], 'w')
destFile.write(sourceData)

sourceFile.close()
destFile.close()

print "Success!"
