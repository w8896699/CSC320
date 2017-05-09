import sys
import math

def goBase9(x, y, z):
	return (81*(y - 1) + 9*(x - 1) + z)
	
def backfromBase9(n):
	n = n - 1
	x = ((n % 81) / 9) + 1
	y = (n / 81) + 1
	z = (n % 9) + 1
	return [x, y, z]

def createcnf(filename,puzzle,dimacs):
	global sudokuFile
	file = open(filename, "w+")
	file.write('c The minimal encoding\n')
	file.write('p cnf 729 5529\n')
	for y in range(1, 10):
		for x in range(1, 10):
			for z in range(1, 10):
				file.write(str(goBase9(x, y, z)) + " ")    
			file.write("0\n")
			
	for y in range(1, 10):
		for z in range(1, 10):
			for x in range(1, 10):
				for i in range ((x+1), 10):
					file.write("-" + str(goBase9(x, y, z)) + " -" + str(goBase9(i, y, z)) + " 0\n")   
					
	for x in range(1, 10):
		for z in range(1, 10):
			for y in range(1, 10):
				for i in range ((y+1), 10):
					file.write("-" + str(goBase9(x, y, z)) + " -" + str(goBase9(x, i, z)) + " 0\n")    
 
	for z in range(1, 10):
		for i in range(0, 3):
			for j in range(0, 3):
				for x in range(1, 4):
					for y in range(1, 4):
						for k in range((y+1), 4):
							file.write("-" + str(goBase9((3*i+x), (3*j+y), z)) + " -" + str(goBase9((3*i+x),(3*j+k), z)) + " 0\n")    
	for z in range(1, 10):
		for i in range(0, 3):
			for j in range(0, 3):
				for x in range(1, 4):
					for y in range(1, 4):
						for k in range((x+1), 4):
							for l in range(1, 4):
								file.write("-" + str(goBase9((3*i+x), (3*j+y), z)) + " -" + str(goBase9((3*i+k),(3*j+l), z)) + " 0\n") 
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
	if len(sys.argv) < 3:
		print ("Missing a command-line argument: <sudoku puzzle> <CNF encoding>")
		return
	
	try:
		sudokuFile = open(sys.argv[1], "r")
		#sudokuFile.read().replace('\n', '').replace('?', '0').replace('*', '0').replace('.', '0')
		puzzle = sudokuFile.read().replace('\n', '')
	except IndexError: 	# read from stdin if no file
		sudokuFile = sys.stdin
	except IOError:		
		print("File specified does not exist!")
	print ("PUZZLE:")
	print (puzzle)
	if len(puzzle) < 81:
		print ("Sudoku file is of incorrect format")
	else:
		x = y = 1
		for i in range(0, 81):
			if puzzle[i].isdigit() and int(puzzle[i]) > 0:
				dimacs.append(goBase9(x, y, int(puzzle[i])))
			x += 1
			if (x == 10):
				x = 1
				y += 1
	print(dimacs)	
	outfilename=sys.argv[2]
	createcnf(outfilename, puzzle,dimacs)
	sudokuFile.close()
main()
#https://github.com/Vealor/SAT_sudoku/blob/master/CAT.py createcnf(ret, puzzle)   cd /cygdrive/c/Users/billy/Desktop/csc320 
#https://github.com/LloydMontgomery/CSC320_PROJECT/blob/master/src/deliverables/sudokuToCNF.py addSudokuToMinimalEncodingFile()SSSSS