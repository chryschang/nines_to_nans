#python 3.6
import decimal
import sys
import os

infile = sys.argv[1]
print("Scanning", infile)
outfile = os.path.splitext(infile)[0] + "_nan.dat" #this strips existing file extension from infile and recreates new filename.

with open(infile, "r") as f_in:
    content = f_in.readlines()

f_out = open(outfile, "w+")

for line in content:
    if line == "-9999\n":
        f_out.write("NaN\n")
    else:
        f_out.write('%.7E' % decimal.Decimal(line)+'\n')
f_out.close()
print("Printing", outfile)
