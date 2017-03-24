Python 3.6 script.
Converts -9999 to NaN in single-column .dat files for SCOPE input data.

To apply to single file, use:
	python nines_to_nans.py filename.dat

To apply to whole folder of .dat files, use:
	for /r %f in (*.dat) do (python nines_to_nans.py "%f")
