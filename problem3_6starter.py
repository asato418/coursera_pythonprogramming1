# -problem3_6.py *- coding: utf-8 -*-

import sys

# add your code here
input_file_name = sys.argv[1]
output_file_name = sys.argv[2]

infile=open(input_file_name)
outfile=open(output_file_name,'w')
for line in infile
	print(line, end="")
	count=len(line)
	outfile.write(count)
	
infile.close()
outfile.close()

