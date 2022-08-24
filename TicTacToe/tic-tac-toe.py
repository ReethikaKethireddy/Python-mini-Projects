squares = [' ']*9
#square is a type list

players = 'XO'
#player is a string & player[0] = X, player[1] = O

board = '''
  0   1   2
  {0} | {1} | {2}
 ------------
3 {3} | {4} | {5} 5
 ------------
  {6} | {7} | {8}
  6   7   8
'''
#board is also a string type.

win_conditions = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8), 
    (0, 3, 6), (1, 4, 7), (2, 5, 8), 
    (0, 4, 8), (2, 4, 6)             
]
#win_conditions is a list type

def check_win(player):
    for a, b, c in win_conditions:
        if {squares[a], squares[b], squares[c]} == {player}:
            return True

while True:
    print(board.format(*squares)) 
    #*squares is used to send whole squareslist as argument to the function format
    #
    if check_win(players[1]):
        print(f'{players[1]} is the winner!')
        break
    if ' ' not in squares:
        print('No game!')
        break
    move = input(f'{players[0]} to move [0-8] > ')
    #by default input takes string and only string has isdigit function
    if not move.isdigit() or not 0 <= int(move) <= 8 or squares[int(move)] != ' ':
        print('Invalid move!')
        continue
    squares[int(move)], players = players[0], players[::-1]
    
    
    #interchanging the player string for every iteration
