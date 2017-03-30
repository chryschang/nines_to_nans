#python 3.6
import decimal
import sys
import os

infile = sys.argv[1]
print("Scanning", infile)
#outfile = os.path.splitext(infile)[0] + "_nan.dat" #this strips existing file extension from infile and recreates new filename.

with open(infile, "r") as f_in:
    content = f_in.readlines()

count = 0
	
for line in content:
    if line == "0\n":
        print(count)
    count += 1