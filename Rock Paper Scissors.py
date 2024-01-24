def rps(p1, p2):
    beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock',}
   
    if beats[p1] == p2:
        print( "Player 1 won!")
    if beats[p2] == p1:
        print( "Player 2 won!")
    if beats[p2] == [p1]:
        print( "Draw!")
 
rps('rock', 'scissors')
 
#player 1 won!