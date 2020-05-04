EMPTY = "-"
ROOK = "ROOK"
board = []
PAWN = "Pawn"
KING= "King"
QUEEN="Queen"
BISHOP="Bishop"
KNIGHT="Knight"
for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)
#rooks
board[0][0] = ROOK
board[0][7] = ROOK
board[7][0] = ROOK
board[7][7] = ROOK
#Pawns
board[1]= [PAWN for i in range(8)]
board[6]= [PAWN for i in range(8)]
#Kings
board[0][3]= KING
board[7][4]= KING
#Queens
board[0][4]= QUEEN
board[7][3]= QUEEN
#Bishops
board[0][2]= BISHOP
board[0][5]= BISHOP
board[7][2]= BISHOP
board[7][5]= BISHOP
#Knights
board[0][1]=KNIGHT
board[0][6]=KNIGHT
board[7][1]=KNIGHT
board[7][6]=KNIGHT

#Print the board
print(board[0],board[1],board[2],board[3],board[4],board[5],board[6],board[7],sep="\n")
