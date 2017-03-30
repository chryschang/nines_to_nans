#python 3.6
import decimal
import sys
import os

infile = sys.argv[1]
print("Scanning", infile)

with open(infile, "r") as f_in:
	content = f_in.readlines()

count = 0
segment = 1

#convert segments to the actual year attributed to this section. confirm with year_nan_<year>.dat
def segtoyear(n):
	if n == 1:
		return 2002
	if n == 2:
		return 2003
	if n == 3:
		return 2004
	if n == 4:
		return 2005
	if n == 5:
		return 2009
	if n == 6:
		return 2010
	if n == 7:
		return 2011

for line in content:
	#get these splitpoints from find_splitpoints.py first and update the numbers.
	if count == 0 or count == 8760 or count == 17520 or count == 26304 or count == 35064 or count == 43824 or count == 52584:
		if count != 0:
			f_out.close()
		year = segtoyear(segment)
		outfile = os.path.splitext(infile)[0] + "_" + str(year) + ".dat" #split files into incrementing segments
		f_out = open(outfile, "w+")
		print(count)
		segment += 1
	f_out.write(line)
	count += 1

f_out.close()
print("Complete")