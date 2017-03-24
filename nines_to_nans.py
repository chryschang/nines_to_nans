#python 3.6
import sys
import os

infile = sys.argv[1]
print(infile)
outfile = os.path.splitext(infile)[0] + "_nan.dat" #this strips existing file extension from infile and recreates new filename.
print(outfile)

with open(infile, "r") as f_in:
    content = f_in.readlines()

f_out = open(outfile, "w+")

for line in content:
    if line == "-9999\n":
        f_out.write("NaN\n")
    else:
        f_out.write(line)
