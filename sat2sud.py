import sys
def backfromBase9(n):
	return (n-1)%9+1


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
			solved.append(int(backfromBase9(int(num))))
	
	
	print(str(solved[0])+" "+str(solved[1])+" "+str(solved[2])+" | "+str(solved[3])+" "+ str(solved[4])+" "+str(solved[5])+" | "+ str(solved[6])+" "+ str(solved[7])+" "+ str(solved[8])+" | ")
	print(str(solved[9])+" "+str(solved[10])+" "+str(solved[11])+" | "+str(solved[12])+" "+ str(solved[13])+" "+str(solved[14])+" | "+ str(solved[15])+" "+ str(solved[16])+" "+ str(solved[17])+" | ")
	print(str(solved[18])+" "+str(solved[19])+" "+str(solved[20])+" | "+str(solved[21])+" "+ str(solved[22])+" "+str(solved[23])+" | "+ str(solved[24])+" "+ str(solved[25])+" "+ str(solved[26])+" | ")
	print("-------+-------+-------")
	print(str(solved[27])+" "+str(solved[28])+" "+str(solved[29])+" | "+str(solved[30])+" "+ str(solved[31])+" "+str(solved[32])+" | "+ str(solved[33])+" "+ str(solved[34])+" "+ str(solved[35])+" | ")
	print(str(solved[36])+" "+str(solved[37])+" "+str(solved[38])+" | "+str(solved[39])+" "+ str(solved[40])+" "+str(solved[41])+" | "+ str(solved[42])+" "+ str(solved[43])+" "+ str(solved[44])+" | ")
	print(str(solved[45])+" "+str(solved[46])+" "+str(solved[47])+" | "+str(solved[48])+" "+ str(solved[49])+" "+str(solved[50])+" | "+ str(solved[51])+" "+ str(solved[52])+" "+ str(solved[53])+" | ")
	print("-------+-------+-------")
	print(str(solved[54])+" "+str(solved[55])+" "+str(solved[56])+" | "+str(solved[57])+" "+ str(solved[58])+" "+str(solved[59])+" | "+ str(solved[60])+" "+ str(solved[61])+" "+ str(solved[62])+" | ")
	print(str(solved[63])+" "+str(solved[64])+" "+str(solved[65])+" | "+str(solved[66])+" "+ str(solved[67])+" "+str(solved[68])+" | "+ str(solved[69])+" "+ str(solved[70])+" "+ str(solved[71])+" | ")
	print(str(solved[72])+" "+str(solved[73])+" "+str(solved[74])+" | "+str(solved[75])+" "+ str(solved[76])+" "+str(solved[77])+" | "+ str(solved[78])+" "+ str(solved[79])+" "+ str(solved[80])+" | ")
	
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
