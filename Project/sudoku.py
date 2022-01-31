from random import sample

def MakeBoard(s):
	base  = 3
	side  = base*base
	nums  = sample(range(1,side+1),side) # random numbers
	board = [[nums[(base*(r%base)+r//base+c)%side] for c in range(side) ] for r in range(side)]
	rows  = [ r for g in sample(range(base),base) for r in     sample(range(g*base,(g+1)*base),base) ] 
	cols  = [ c for g in sample(range(base),base) for c in sample(range(g*base,(g+1)*base),base) ]            
	board = [[board[r][c] for c in cols] for r in rows]
	board1=board
	squares = side*side
	if(s=="easy"):
		empties = 20
		n=20
	elif(s=="medium"):    
		empties = 40
		n=40
	elif(s=="hard"):
		empties = 60
		n=60
	for p in sample(range(squares),empties):
		board1[p//side][p%side] = 0
	return board1,side,board,n,base

def DisplayBoard(board1,side,base):
	line0  = "  ╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗"
	line1  = " ║ . │ . │ . ║ . │ . │ . ║ . │ . │ . ║"
	line2  = "  ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢"
	line3  = "  ╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣"
	line4  = "  ╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝"
	line5  = "    1   2   3   4   5   6   7   8   9"  
	symbol = " 1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	nums   = [ [""]+[symbol[n] for n in row] for row in board1 ]
	print(line5)
	print(line0)
	for r in range(1,side+1):
		print(r,end="")
		print( "".join(n+s for n,s in zip(nums[r-1],line1.split("."))) )    
		print([line2,line3,line4][(r%side==0)+(r%base==0)])

def Move():
	s=input("Pick a difficulty-Easy,Medium,Hard:")
	s=s.lower()
	board1,side,board,n,base=MakeBoard(s)
	while(n>0):
		DisplayBoard(board1,side,base)
		x=int(input("Enter x coordinate of square:"))
		y=int(input("Enter y coordinate of square:"))
		z=int(input("Enter number to enter:"))
		if(board[x-1][y-1]==0):
			board1[x-1][y-1]=z
			n-=1
		else:
			print("That cell is already occupied")
	DisplayBoard(board1,side,base)
	if(board==board1):
		print("You solved it!")
	else:
		print("Sorry,you have made an error!")
Move()
