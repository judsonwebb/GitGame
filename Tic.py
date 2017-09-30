def tic_tac_toe():
    grid= [[0,0,0],[0,0,0],[0,0,0]]
    print ("Time to play!")
    game_over=False
    display_board(grid)
    while(not game_over):

        game_over =player_one(grid,game_over)
        display_board(grid)
        if (game_over):
            break
        game_over =player_two(grid,game_over)
        display_board(grid)


def display_board(grid):
    print ("123\n456\n789\n")
    board =get_board(grid)
    for y in range(3):
        print ((board[y][0])+(board[y][1])+(board[y][2]))


def get_board(grid):
    board= [["e","e","e"],["e","e","e"],["e","e","e"]]
    for y in range(3):
        for x in range(3):
            if grid[y][x]==1:
                board[y][x]="X"
            elif grid[y][x]==2:
                board[y][x]="O"
    return board

def player_one(grid, game_over):
    print ("Player One's turn!")
    move = (int)(input("Choose an integer between 1-9 (inclusive) to make your move: "))
    if move<4:
        grid[0][(move%3)-1]=1
    elif move<7:
        grid[1][(move % 3) - 1] = 1
    elif move<10:
        grid[2][(move % 3) - 1] = 1
    game_over=check_win(grid,game_over,1)
    return game_over

def player_two(grid,game_over):
    print ("Player Two's turn!")
    move = (int)(input("Choose an integer between 1-9 (inclusive) to make your move: "))
    if move<4:
        grid[0][(move%3)-1]=2
    elif move<7:
        grid[1][(move % 3) - 1] = 2
    elif move<10:
        grid[2][(move % 3) - 1] = 2
    game_over=check_win(grid,game_over,2)
    return game_over

def check_win(grid,game_over,player):
    flag =False
    if player == 1:
        for y in range(3):
            if (grid[y][0]==1)and(grid[y][1]==1)and(grid[y][2]==1):
                flag =True
            if (grid[0][y]==1)and(grid[1][y]==1)and(grid[2][y]==1):
                flag =True
        if (grid[0][2] == 1) and (grid[1][1] == 1) and (grid[2][0] == 1):
            flag=True
        if (grid[0][0] == 1) and (grid[1][1] == 1) and (grid[2][2] == 1):
            flag=True
        if flag==True:
            print ("Player One wins!")
            game_over=True
    if player == 2:
        for y in range(3):
            if (grid[y][0]==2)and(grid[y][1]==2)and(grid[y][2]==2):
                flag =True
            if (grid[0][y]==2)and(grid[1][y]==2)and(grid[2][y]==2):
                flag =True
        if (grid[0][2] == 2) and (grid[1][1] == 2) and (grid[2][0] == 2):
            flag=True
        if (grid[0][0] == 2) and (grid[1][1] == 2) and (grid[2][2] == 2):
            flag=True
        if flag==True:
            print ("Player Two wins!")
            game_over=True
    full_count =0
    for x in range(3):
        for y in range(3):
            if grid[y][x]!=0:
                full_count=full_count+1
    if full_count==9:
        game_over=True

    return game_over
tic_tac_toe()
