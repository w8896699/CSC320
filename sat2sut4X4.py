import sys
def backfromBase4(n):
	return (n-1)%4+1


def trysolvedfile():
	global handlefile
	sat = handlefile.readline()
	print(sat)
	if( sat == "SAT\n"):
		print("CNF was satisfiable")
	else:
		print ("CNF was unsatisfiable")
	solved = []
	
	for num in handlefile.read().split():
		if num.isdigit() and int(num) > 0:
			solved.append(int(backfromBase4(int(num))))
		
	print(str(solved[0])+" | "+str(solved[1])+" | "+str(solved[2])+" | "+str(solved[3]))
	print("-------------")
	print(str(solved[4])+" | "+str(solved[5])+" | "+str(solved[6])+" | "+str(solved[7]))
	print("-------------")
	print(str(solved[8])+" | "+str(solved[9])+" | "+str(solved[10])+" | "+str(solved[11]))
	print("-------------")
	print(str(solved[12])+" | "+str(solved[13])+" | "+str(solved[14])+" | "+str(solved[15]))


def main():
	global handlefile
	if len(sys.argv) != 2:
		print ("Missing filename of MiniSAT output")
		return 0
	try:
		handlefile = open(sys.argv[1], "r")
	except:
		print ("Can't open file to write!")
		return
	trysolvedfile()
main()
