def sum(a,b,c):
    return a+b+c

def display_board():
    print("   0  |   1   |   2 ")
    print("------|-------|------")
    print("   3  |   4   |   5 ")
    print("------|-------|------")
    print("   6  |   7   |   8 ")

    
def print_board():
    zero= {'X' if xState[0] else ('O' if yState[0] else ' ')}
    one= {'X' if xState[1] else ('O' if yState[1] else ' ')}
    two= {'X' if xState[2] else ('O' if yState[2] else ' ')}
    three= {'X' if xState[3] else ('O' if yState[3] else ' ')}
    four= {'X' if xState[4] else ('O' if yState[4] else ' ')}
    five = {'X' if xState[5] else ('O' if yState[5] else ' ')}
    six= {'X' if xState[6] else ('O' if yState[6] else ' ')}
    seven= {'X' if xState[7] else ('O' if yState[7] else ' ')}
    eig= {'X' if xState[8] else ('O' if yState[8] else ' ')}


    print(f"{zero} | {one} | {two}")
    print('------|-------|------')
    print(f"{three} | {four} | {five}")
    print('------|-------|------')
    print(f"{six} | {seven} | {eig}")

def check_wins(xState,yState):
    wins=[[0,3,6],[1,4,7],[2,5,8],[0,1,2],[3,4,5],[6,7,8],[0,4,8],[2,4,6]]
    for win in wins:
      if (sum(xState[win[0]],xState[win[1]],xState[win[2]]) == 3):
        print('X won the match!')
        return 1
        
      if (sum(yState[win[0]],yState[win[1]],yState[win[2]]) == 3): 
        print('O won the match!')
        return 0
    return -1

if __name__ =='__main__':
     xState=[0,0,0,0,0,0,0,0,0]
     yState=[0,0,0,0,0,0,0,0,0]
     turn= 1
     print('Welcome to Tic-Tac-Toe')
     while(True):
        display_board()
        print_board()
        if(turn == 1):
            print("X\'s Chance")
            value= int(input("Please enter a value:"))
            xState[value]=1
        else:
            print("O\'s Chance")
            value= int(input("Please enter a value:"))
            yState[value]=1
        cwin= check_wins(xState,yState)
        if(cwin !=-1):
            break
        turn = 1- turn
        
        
     
        print_board()