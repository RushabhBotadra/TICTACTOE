import sys

board=[" "," "," "," "," "," "," "," "," "]
#Information of  players

a=input("enter your name")
a1=input("choose your symbol:X/O")
b=input("enter your name")
b1=input("choose your symbol:X/O")

#creation of a board
def create_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-------------")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-------------")
    print(board[6] + "|" + board[7] + "|" + board[8])


#Start the game
    
def chance_a():
    print("Turn of:",a)
    choice=int(input("enter the place number where u want to enter your symbol"))
    if(board[choice]==" "):
        board[choice]=a1
        result()
        chance_b()
        
    else:
        print("Sorry!!! place occupied")
        chance_a()

def chance_b():
    print("Turn of:",b)
    choice=int(input("enter the place number where u want to enter your symbol"))
    if(board[choice]==" "):
        board[choice]=b1
        result()
        chance_a()
        
    else:
        print("Sorry!!! place occupied")
        chance_b()
        
def result():
	if(board[0]==board[4]==board[8]==a1):
		print(a,":WON")
		sys.exit()
	elif(board[0]==board[1]==board[2]==a1):
		print(a,":WON")
		sys.exit()
	elif(board[0]==board[3]==board[6]==a1):
		print(a,":WON")
		sys.exit()
	elif(board[1]==board[4]==board[7]==a1):
		print(a,":WON")
		sys.exit()
	elif(board[2]==board[5]==board[8]==a1):
		print(a,":WON")
		sys.exit()
	elif(board[3]==board[4]==board[5]==a1):
		print(a,":WON")
		sys.exit()
	elif(board[6]==board[7]==board[8]==a1):
		print(a,":WON")
		sys.exit()
	elif(board[0]==board[4]==board[8]==b1):
		print(b,":WON")
		sys.exit()
	elif(board[0]==board[1]==board[2]==b1):
		print(b,":WON")
		sys.exit()
	elif(board[0]==board[3]==board[6]==b1):
		print(b,":WON")
		sys.exit()
	elif(board[1]==board[4]==board[7]==b1):
		print(b,":WON")
		sys.exit()
	elif(board[2]==board[5]==board[8]==b1):
		print(b,":WON")
		sys.exit()
	elif(board[3]==board[4]==board[5]==b1):
		print(b,":WON")
		sys.exit()
	elif(board[6]==board[7]==board[8]==b1):
		print(b,":WON")
		sys.exit()
	else:
		return 0

    
    
            
        
            
	
	
		


create_board()
chance_a()


    
       
    
    
