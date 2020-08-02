def Print():
    for i in range(8):
        for j in range(8):
            print(puzzle[i][j],end=' ');
        print("\n");
def Count():
    global black,white
    black,white = 0,0
    for i in range(8):
        for j in range(8):
            if(puzzle[i][j] == 'W'):
                white += 1
            elif(puzzle[i][j] == 'B'):
                black += 1
    count = white+black
    return count
def White():
    global m
    m,leg=0,0
    li.append('W')
    x,y=0,0
    p=0
    v=0
    legal=[]
    print("Legal moves for {}".format(player2))
    for i in range(8) :
        for j in range(8) :
            if puzzle[i][j] == 'W'and i>0 and j < 8:
                v=0
                x = i-1
                while(puzzle[x][j] == 'B' and x>0 and j < 8 ):
                    x -= 1;
                    if(puzzle[x][j] == '-'):
                        p=1
                        v=0
                        if(legal != []):
                            for r in legal:
                                if(v == 0):
                                    if(r == [x+1,j+1]):
                                        v = 1
                            if(v==0):
                                legal.append([x+1,j+1])
                                print("({},{})".format(x+1,j+1),end = ' ')
                        else:
                            legal.append([x+1,j+1])
                            print("({},{})".format(x+1,j+1),end = ' ')
            if puzzle[i][j] == 'W' and i<7 and j<8 :
                x = i+1
                v=0
                while(puzzle[x][j] == 'B'and x<7 and j<8):
                    x += 1
                    if(puzzle[x][j] == '-'):
                        p=1
                        v=0
                        if(legal != []):
                            for r in legal:
                                if(v == 0):
                                    if(r == [x+1,j+1]):
                                        v = 1
                            if(v==0):
                                legal.append([x+1,j+1])
                                print("({},{})".format(x+1,j+1),end = ' ')
                        else:
                            legal.append([x+1,j+1])
                            print("({},{})".format(x+1,j+1),end = ' ')
            if puzzle[i][j] == 'W' and j > 0 and i<8:
                x = j-1
                v=0
                while(puzzle[i][x] == 'B' and x > 0 and i<8):
                    x -= 1
                    if(puzzle[i][x] == '-'):
                        p=1
                        v=0
                        if(legal != []):
                                for r in legal:
                                    if(v == 0):
                                        if(r == [i+1,x+1]):
                                            v = 1
                                if(v==0):
                                    legal.append([i+1,x+1])
                                    print("({},{})".format(i+1,x+1),end = ' ')
                        else:   
                            legal.append([i+1,x+1])
                            print("({},{})".format(i+1,x+1),end = ' ')
            if puzzle[i][j] == 'W' and j < 7 and i<8:
                x = j+1
                v=0
                while(puzzle[i][x] == 'B'  and x < 7 and i<8):
                    x += 1
                    if(puzzle[i][x] == '-'):
                        p=1
                        v=0
                        if(legal != []):
                            for r in legal:
                                if(v == 0):
                                    if(r == [i+1,x+1]):
                                        v = 1
                            if(v==0):
                                legal.append([i+1,x+1])
                                print("({},{})".format(i+1,x+1),end = ' ')
                        else:
                            legal.append([i+1,x+1])
                            print("({},{})".format(i+1,x+1),end = ' ')
            if puzzle[i][j] == 'W'and i>1 and j>1:
                x = i-1
                y = j-1
                v=0
                while(puzzle[x][y] == 'B'and x>0 and y>0 and x<8 and y<8):
                    x -= 1
                    y -= 1
                    if(puzzle[x][y] == '-'):
                        p=1
                        v=0
                        if(legal != []):
                            for r in legal:
                                if(v == 0):
                                    if(r == [x+1,y+1]):
                                        v = 1
                            if(v==0):
                                legal.append([x+1,y+1])
                                print("({},{})".format(x+1,y+1),end = ' ')
                        else:
                            legal.append([x+1,y+1])
                            print("({},{})".format(x+1,y+1),end = ' ')
            if puzzle[i][j] == 'W'and i<6 and j<6:
                x = i+1
                y = j+1
                v=0
                while(puzzle[x][y] == 'B'and x>0 and y>0 and x<7 and y<7):
                    x += 1
                    y += 1
                    if(puzzle[x][y] == '-'):
                        p=1
                        v=0
                        if(legal != []):
                            for r in legal:
                                
                                if(v == 0):
                                    if(r == [x+1,y+1]):
                                        v = 1
                            if(v==0):
                                legal.append([x+1,y+1])
                                print("({},{})".format(x+1,y+1),end = ' ')
                        else:
                            legal.append([x+1,y+1])
                            print("({},{})".format(x+1,y+1),end = ' ')

            if puzzle[i][j] == 'W' and i>0 and j<7:
                x = i-1
                y = j+1
                v=0
                while(puzzle[x][y] == 'B' and x>0 and y>0 and x<8 and y<7):
                    x -= 1
                    y += 1
                    if(puzzle[x][y] == '-'):
                        p=1
                        v=0
                        if(legal != []):
                            for r in legal:
                                if(v == 0):
                                    if(r == [x+1,y+1]):
                                        v = 1
                            if(v==0):
                                legal.append([x+1,y+1])
                                print("({},{})".format(x+1,y+1),end = ' ')
                        else:
                            legal.append([x+1,y+1])
                            print("({},{})".format(x+1,y+1),end = ' ')

            if puzzle[i][j] == 'W'and j>1 and i<6:
                x = i+1
                y = j-1
                v=0
                while(puzzle[x][y] == 'B'and x>0 and y>0 and x<7 and y<8):
                    x += 1
                    y -= 1
                    if(puzzle[x][y] == '-'):
                        p=1
                        v=0
                        if(legal != []):
                            for r in legal:
                                if(v == 0):
                                    if(r == [x+1,y+1]):
                                        v = 1
                            if(v==0):
                                legal.append([x+1,y+1])
                                print("({},{})".format(x+1,y+1),end = ' ')
                        else:
                            legal.append([x+1,y+1])
                            print("({},{})".format(x+1,y+1),end = ' ')

    if(p==0):
        print("No Legal move.")
        print("Turn goes to {}".format(player1))
        m=1
        return ;
    print()
    r = int(input("select r"))-1
    print()
    c = int(input("select c"))-1
    for i in legal:
        if(i == [r+1,c+1]):
            break;
        else:
            leg += 1
    if(leg == len(legal)):
        print("Invalid move")
        print("Turn goes to {}".format(player1))
        return ;
    puzzle[r][c] = 'W'
    k=0
    if puzzle[r][c] == 'W' and c<7:
        k=0
        x = c+1
        while(puzzle[r][x] == 'B' and x<7):
            k += 1
            x += 1
            if(puzzle[r][x] == 'W'):
                while(k>=0):
                    puzzle[r][x] = 'W'
                    k -= 1
                    x -= 1
           
    if puzzle[r][c] == 'W' and c>0:
        k=0
        x = c-1
        while(puzzle[r][x] == 'B' and x>0):
            k += 1
            x -= 1
            if(puzzle[r][x] == 'W'):
                while(k>=0):
                    puzzle[r][x] = 'W'
                    k -= 1
                    x += 1
               
    if puzzle[r][c] == 'W' and r<7 :
        k=0
        x = r+1
        while(puzzle[x][c] == 'B' and x<7):
            k += 1
            x += 1
            if(puzzle[x][c] == 'W'):
                while(k>=0):
                    puzzle[x][c] = 'W'
                    k -= 1
                    x -= 1
    if puzzle[r][c] == 'W' and r>0:
        k=0
        x = r-1
        while(puzzle[x][c] == 'B' and x>0):
            k += 1
            x -= 1
            if(puzzle[x][c] == 'W'):
                while(k>=0):
                    puzzle[x][c] = 'W'
                    k -= 1
                    x += 1
    if puzzle[r][c] == 'W' and r<6 and c<6:
        k=0
        x = r+1
        y=c+1
        while(puzzle[x][y] == 'B' and x<7 and y<7):
            k += 1
            x += 1
            y += 1
            if(puzzle[x][y] == 'W'):
                while(k>=0):
                    puzzle[x][y] = 'W'
                    k -= 1
                    x -= 1
                    y -= 1
    if puzzle[r][c] == 'W' and r>0 and c>0:
        k=0
        x = r-1
        y = c-1
        while(puzzle[x][y] == 'B' and x>0 and y>0):
            k += 1
            x -= 1
            y -= 1
            if(puzzle[x][y] == 'W'):
                while(k>=0):
                    k -= 1
                    x += 1
                    y += 1
                    puzzle[x][y] = 'W'
                    
    if puzzle[r][c] == 'W' and r>0 and c<7:
        k=0
        x = r-1
        y = c+1
        while(puzzle[x][y] == 'B' and x>0 and y<7):
            k += 1
            x -= 1
            y += 1
            if(puzzle[x][y] == 'W'):
                while(k>=0):
                    puzzle[x][y] = 'W'
                    k -= 1
                    x += 1
                    y -= 1
    if puzzle[r][c] == 'W' and r<6 and c>0:
        k=0
        x = r+1
        y = c-1
        while(puzzle[x][y] == 'B' and x<7 and y>0 ):
            k += 1
            x += 1
            y -= 1
            if(puzzle[x][y] == 'W'):
                while(k>=0):
                    puzzle[x][y] = 'W'
                    k -= 1
                    x -= 1
                    y += 1
    Print();
    
def Black():
    legal = []
    leg=0
    global l
    l=0
    li.append('B')
    x=0
    y=0
    p=0
    v=0
    r=0
    print("Legal moves for {}".format(player1))
    for i in range(8) :
        for j in range(8) :
            if puzzle[i][j] == 'B'and i>0 and j < 8:
                x = i-1
                v=0
                while(puzzle[x][j] == 'W' and x>0 and j<8):
                    x -= 1;
                    if(puzzle[x][j] == '-'):
                        v=0
                        p=1
                        if(legal != []):
                            for r in legal:
                                if(v == 0):
                                    if(r == [x+1,j+1]):
                                        v = 1
                            if(v==0):
                                legal.append([x+1,j+1])
                                print("({},{})".format(x+1,j+1),end = ' ')
                        else:
                            legal.append([x+1,j+1])
                            print("({},{})".format(x+1,j+1),end = ' ')
                            
            if puzzle[i][j] == 'B'  and i<7 and j<8:
                x = i+1
                v=0
                while(puzzle[x][j] == 'W' and x<7 and j<8):
                    x += 1;
                    if(puzzle[x][j] == '-'):
                        v=0
                        p=1
                        
                        if(legal!=[]):
                            for r in legal:
                                if(v==0):
                                    if(r == [x+1,j+1]):
                                        v=1
                            if(v==0):
                                legal.append([x+1,j+1])
                                print("({},{})".format(x+1,j+1),end = ' ')
                        else:
                            legal.append([x+1,j+1])
                            print("({},{})".format(x+1,j+1),end = ' ')

            if puzzle[i][j] == 'B' and j>0 and i<8:
                x = j-1
                v=0
                while(puzzle[i][x] == 'W' and x>0 and i<8):
                    x -= 1;
                    if(puzzle[i][x] == '-'):
                        p=1
                        v=0
                        if(legal!=[]):
                            for r in legal:
                                if(v==0):
                                    if(r == [i+1,x+1]):
                                        v=1
                            if(v==0):
                                legal.append([i+1,x+1])
                                print("({},{})".format(i+1,x+1),end = ' ')
                        else:
                            legal.append([i+1,x+1])
                            print("({},{})".format(i+1,x+1),end = ' ')

            if puzzle[i][j] == 'B' and i<8 and j<7:
                x = j+1
                v=0
                while(puzzle[i][x] == 'W' and x<7 and i<8):
                    x += 1;
                    if(puzzle[i][x] == '-'):
                        p=1
                        v=0
                        if(legal!=[]):
                            for r in legal:
                                if(v==0):
                                    if(r == [i+1,x+1]):
                                        v=1
                            if(v==0):
                                legal.append([i+1,x+1])
                                print("({},{})".format(i+1,x+1),end = ' ')
                        else:
                            legal.append([i+1,x+1])
                            print("({},{})".format(i+1,x+1),end = ' ')

            if puzzle[i][j] == 'B' and i>1 and j>1:
                x = i-1
                y = j-1
                v=0
                while(puzzle[x][y] == 'W' and x>0 and y>0 and x<8 and y<8):
                    x -= 1
                    y -= 1
                    if(puzzle[x][y] == '-'):
                        v=0
                        p=1
                        if(legal!=[]):
                            for r in legal:
                                if(v==0):
                                    if(r == [x+1,y+1]):
                                        v=1
                            if(v==0):
                                legal.append([x+1,y+1])
                                print("({},{})".format(x+1,y+1),end = ' ')
                        else:
                            legal.append([x+1,y+1])
                            print("({},{})".format(x+1,y+1),end = ' ')

            if puzzle[i][j] == 'B' and i<6 and j<6:
                x = i+1
                y = j+1
                v=0
                while(puzzle[x][y] == 'W' and x>0 and y>0 and x<7 and y<7):
                    x += 1
                    y += 1
                    if(puzzle[x][y] == '-'):
                        p=1
                        v=0
                        if(legal!=[]):
                            for r in legal:
                                if(v==0):
                                    if(r == [x+1,y+1]):
                                        v=1
                            if(v==0):
                                legal.append([x+1,y+1])
                                print("({},{})".format(x+1,y+1),end = ' ')
                        else:
                            legal.append([x+1,y+1])
                            print("({},{})".format(x+1,y+1),end = ' ')

            if puzzle[i][j] == 'B' and i>1 and j<6:
                x = i-1
                y = j+1
                v=0
                while(puzzle[x][y] == 'W' and x>0 and y>0 and x<8 and y<7):
                    x -= 1
                    y += 1
                    if(puzzle[x][y] == '-'):
                        p=1
                        v=0
                        if(legal!=[]):
                            for r in legal:
                                if(v==0):
                                    if(r == [x+1,y+1]):
                                        v=1
                            if(v==0):
                                legal.append([x+1,y+1])
                                print("({},{})".format(x+1,y+1),end = ' ')
                        else:
                            legal.append([x+1,y+1])
                            print("({},{})".format(x+1,y+1),end = ' ')

            if puzzle[i][j] == 'B' and i<6 and j>1:
                x = i+1
                y = j-1
                v=0
                while(puzzle[x][y] == 'W' and  x>0 and y>0 and x<7 and y<8):
                    x += 1
                    y -= 1
                    if(puzzle[x][y] == '-'):
                        p=1
                        v=0
                        if(legal!=[]):
                            for r in legal:
                                if(v==0):
                                    if(r == [x+1,y+1]):
                                        v=1
                            if(v==0):
                                legal.append([x+1,y+1])
                                print("({},{})".format(x+1,y+1),end = ' ')
                    else:
                        legal.append([x+1,y+1])
                        print("({},{})".format(x+1,y+1),end = ' ')

    if(p==0):
        print("No legal move.")
        print("Turn goes to {}".format(player2))
        l=1
        return ;
    print()     
    r = int(input("select r"))-1
    print()
    c = int(input("select c"))-1
    for i in legal:
        if(i == [r+1,c+1]):
            v=1
        if(v!=1):
            leg += 1
    if(leg == len(legal)):
        print("Invalid move")
        print("Turn goes to {}".format(player2))
        return ;

    puzzle[r][c] = 'B'
    k=0
    v=0
    if puzzle[r][c] == 'B' and c<7:
        x = c+1
        k=0
        while(puzzle[r][x] == 'W' and x<7):
            k += 1
            x += 1
            if(puzzle[r][x] == 'B'):
                while(k>=0):
                    puzzle[r][x] = 'B'
                    k -= 1
                    x -= 1
    if puzzle[r][c] == 'B' and c>0:
        k=0
        x = c-1
        while(puzzle[r][x] == 'W' and x>0):
            k += 1
            x -= 1
            if(puzzle[r][x] == 'B'):
                while(k>=0):
                    puzzle[r][x] = 'B'
                    k -= 1
                    x += 1
               
    if puzzle[r][c] == 'B' and r<7:
        k=0
        x = r+1
        while(puzzle[x][c] == 'W' and x<7):
            k += 1
            x += 1
            if(puzzle[x][c] == 'B'):
                while(k>=0):
                    puzzle[x][c] = 'B'
                    k -= 1
                    x -= 1
    if puzzle[r][c] == 'B' and r>0:
        k=0
        x = r-1
        while(puzzle[x][c] == 'W' and x>0):
            k += 1
            x -= 1
            if(puzzle[x][c] == 'B'):
                while(k>=0):
                    puzzle[x][c] = 'B'
                    k -= 1
                    x += 1
    if puzzle[r][c] == 'B' and r<7 and c<7:
        k=0
        x = r+1
        y=c+1
        while(puzzle[x][y] == 'W' and x<7 and y<7):
            k += 1
            x += 1
            y += 1
            if(puzzle[x][y] == 'B'):
                while(k>=0):
                    puzzle[x][y] = 'B'
                    k -= 1
                    x -= 1
                    y -= 1
    if puzzle[r][c] == 'B' and r>0 and c>0:
        k=0
        x = r-1
        y = c-1
        while(puzzle[x][y] == 'W' and x>0 and y>0):
            k += 1
            x -= 1
            y -= 1
            if(puzzle[x][y] == 'B'):
                while(k>=0):
                    puzzle[x][y] = 'B'
                    k -= 1
                    x += 1
                    y += 1
    if puzzle[r][c] == 'B' and r>0 and c<7:
        k=0
        x = r-1
        y = c+1
        while(puzzle[x][y] == 'W' and x>0 and y<7):
            k += 1
            x -= 1
            y += 1
            if(puzzle[x][y] == 'B'):
                while(k>=0):
                    puzzle[x][y] = 'B'
                    k -= 1
                    x += 1
                    y -= 1
    if puzzle[r][c] == 'B' and r<7 and c>0:
        k=0
        x = r+1
        y = c-1
        while(puzzle[x][y] == 'W' and y>0 and x<7):
            k += 1
            x += 1
            y -= 1
            if(puzzle[x][y] == 'B'):
                while(k>=0):
                    puzzle[x][y] = 'B'
                    k -= 1
                    x -= 1
                    y += 1
    Print();
    
puzzle = [['-' for j in range(8)]for i in range(8)] 
puzzle[3][3] = 'W'
puzzle[4][4] = 'W'
puzzle[3][4] = 'B'
puzzle[4][3] = 'B'
Print();
legal = []
black,white = 0,0
l,m = 0,0
li = []
player1 = input("Enter player1 name : ")
player2 = input("Enter player2 name : ")
print()
Black()
while(Count() != 64):
    if(l==1 and  m==1):
        break
    elif(li[-1] == 'W'):
        Black()
    elif(li[-1]=='B'):
        White()
print("number of {} coins (black) : {}".format(player1,black))
print("number of {} coins (white) : {}".format(player2,white))
if(black>white):
    print("{} won the game".format(player1))
elif(white>black):
    print("{} won the game".format(player2))
else:
    print("game was tie!")
