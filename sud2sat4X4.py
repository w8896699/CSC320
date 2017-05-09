#this is the case of 4by4 puzzle
#reads Sudoku puzzle and covert it to a CNF suitable for input to the miniSAT SAT solver

import sys
import math

def goBase4(x, y, z):
	return (16*(y - 1) + 4*(x - 1) + z)
	
def backfromBase9(n):
	n = n - 1
	x = ((n % 16) / 4) + 1
	y = (n / 16) + 1
	z = (n % 4) + 1
	return [x, y, z]

def createcnf(filename,puzzle,dimacs):
	global sudokuFile
	#filename: 4X4cnf.txt
	file = open(filename, "w+")
	file.write('c The minimal encoding for 4 by 4 puzzle\n')
	file.write('p cnf 64 135\n')

	#each cell contains at least one number
	for y in range(1, 5):
		for x in range(1, 5):
			for z in range(1, 5):
				file.write(str(goBase4(x, y, z)) + " ")    
			file.write("0\n")

	#one num row			
	for y in range(1, 5):
		for z in range(1, 5):
			for x in range(1, 5):
				for i in range ((x+1), 5):
					file.write("-" + str(goBase4(x, y, z)) + " -" + str(goBase4(i, y, z)) + " 0\n")   
	#one num col	
	for x in range(1, 5):
		for z in range(1, 5):
			for y in range(1, 5):
				for i in range ((y+1), 5):
					file.write("-" + str(goBase4(x, y, z)) + " -" + str(goBase4(x, i, z)) + " 0\n")    
 	#one num block
	for z in range(1, 5):
		for i in range(0, 2):
			for j in range(0, 2):
				for x in range(1, 3):
					for y in range(1, 2):
						for k in range((y+1), 3):
							file.write("-" + str(goBase4((2*i+x), (2*j+y), z)) + " -" + str(goBase4((2*i+x),(2*j+k), z)) + " 0\n")    
	for z in range(1, 5):
		for i in range(0, 2):
			for j in range(0, 2):
				for x in range(1, 2):
					for y in range(1, 3):
						for k in range((x+1), 3):
							for l in range(1, 3):
								file.write("-" + str(goBase4((2*i+x), (2*j+y), z)) + " -" + str(goBase4((2*i+k),(2*j+l), z)) + " 0\n") 
	file.close()		
	encodingFile = open(filename, "r+")
	CNFFile = open("CNF.txt", "w+")
	
	minimalEncodingBuffer = encodingFile.readline()
	CNFFile.write(minimalEncodingBuffer)
	minimalEncodingBuffer = encodingFile.readline()

	# Split the input into 4 pieces 
	minimalEncodingBuffer = minimalEncodingBuffer.split()
	clauses = int(minimalEncodingBuffer[3])
	clauses = clauses + len(dimacs)
	
	# Cast the number of clauses back into a str and write to file
	minimalEncodingBuffer[3] = str(clauses)
	minimalEncodingBuffer = " ".join(minimalEncodingBuffer)
	CNFFile.write(minimalEncodingBuffer + "\n")

	# Copy all the existing clauses as is
	while 1:
		minimalEncodingBuffer = encodingFile.readline()
		if minimalEncodingBuffer == "":
			break
		CNFFile.write(minimalEncodingBuffer)

	# Write the sudoku truth clauses as clauses in the minimal encoding
	for number in dimacs:
		CNFFile.write(str(number) + " 0\n")
	encodingFile.close()
	CNFFile.close()
	

def main():
	global sudokuFile
	dimacs=[]	

	#check input
	if len(sys.argv) != 3:
		print ("Missing input components")
		print ("input example: python sud2sat.py input.txt cnf.txt")
		#sample input: python sud2sat.py input.txt cnf.txt
		#			  0	    1	      2
		return 0

	#open puzzle txt file
	try:
		sudokuFile = open(sys.argv[1], "r")
		puzzle = sudokuFile.read().replace('\n', '')
	except IndexError: 	# read from stdin if no file
		sudokuFile = sys.stdin
	except IOError:		
		print("File specified does not exist!")

	
	print ("PUZZLE:")
	print (puzzle)
	if len(puzzle) != 16:
		print ("input puzzle file is of incorrect format")
	else:
		x = y = 1
		for i in range(0, 16):
			if puzzle[i].isdigit() and int(puzzle[i]) > 0:
				dimacs.append(goBase4(x, y, int(puzzle[i])))
			x += 1
			if (x == 5):
				x = 1
				y += 1
	print(dimacs)	
	outfilename=sys.argv[2]
	createcnf(outfilename, puzzle,dimacs)
	sudokuFile.close()

main()

