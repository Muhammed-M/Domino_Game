import random
import time
import ast

class Player() : 

    def __init__(self, name) : 
        self.name = name 
        self.p_set = [] 

    def __str__(self) :
        return f"PLayer : {self.name} \nYour Set : {self.p_set}" 

        


class Game() : 


    def __init__(self , domino_set) : 
        
        self.domino_set = domino_set
        self.lr = []
        self.players = []

        while True : 
            try :
                num_of_players = int(input('How Many Players ? (minimum : 2) \n ----------------------------------------- \n' ))
                if 2 <= num_of_players <= 4 : 
                    break
                else : print ('\n ----------------------------------------- \n Minimum num of players is 2 and Max num is 4 ')
            except ValueError : 
                print('\n ----------------------------------------- \n Please enter a number. ')

      
        for i in range(num_of_players) :
            name = input(f" \n Enter name for Player {i+1}: ")
            self.players.append(Player(name))
        

    
    def shuffle(self)  : 
        self.lr = self.domino_set[:]
        for player in self.players : 
            for j in range(7) : 
                x = random.choice(self.lr)
                player.p_set.append(x)
                self.lr.remove(x)




domino_set1 = [(i, j) for i in range(6, -1, -1) for j in range(i, -1, -1)]  
#[(6, 6), (6, 5), (6, 4), (6, 3), (6, 2), (6, 1), (6, 0), 
#(5, 5), (5, 4), (5, 3), (5, 2), (5, 1), (5, 0), 
#(4, 4), (4, 3), (4, 2), (4, 1), (4, 0), 
#(3, 3), (3, 2), (3, 1), (3, 0), 
#(2, 2), (2, 1), (2, 0), 
#(1, 1), (1, 0), 
#(0, 0)]



def StartGame() :
    

    print('\n Loading... \n \n ----------------------------------------- \n ')
    time.sleep(5)
    game1 = Game(domino_set1)
    game1.shuffle()
    print('\n\n\n OK Great, Lets Start \n \n ----------------------------------------- \n')
    
    gameboard = []
    while True : 
        
            
        for player in game1.players : 
            if not gameboard : 
                print(" \n ----------------------------------------- \n Game Board : [                     ] \n ----------------------------------------- \n")
                print("Play the First Move")
            else : 
                print(f'\n ----------------------------------------- \n Game Board : {gameboard} \n ----------------------------------------- \n ')
            print(f'{player.name} Turn')
            print(player)
            
                    
            while True :

                try :
                    move = input('Choose your Move or Write "D" to Draw ')
                    if str(move).lower() == "d" :
                        if not game1.lr : 
                            print("No tiles left to draw! , PASS !!! ")
                            break
                        x = random.choice(game1.lr)
                        player.p_set.append(x)
                        print(f'Your Set : {player.p_set}')
                        game1.lr.remove(x)
                        continue
                    else : 
                        move = ast.literal_eval(move)
                        reversed_move = (move[1], move[0])
                    if not move in player.p_set : 
                        print(f'Please Choose From Your Set |^|^|^| ')
                        continue
                except :
                    print('\n ----------------------------------------- \n Please enter a Valid Move from your set or Write "D" to Draw. ')
                    continue
                
                    
                    
                
                if not gameboard : 
                    gameboard.append(move)
                    player.p_set.remove(move)
                    break
                

                location = input('Left (<--)  or  Right (-->)  __write L or R__' )
                if location.lower() == "l" :
                    if move[1] == gameboard[0][0] :
                        gameboard.insert(0,move)
                        player.p_set.remove(move)
                        break
                    elif reversed_move[1] == gameboard[0][0] :
                        gameboard.insert(0,reversed_move)
                        player.p_set.remove(move)
                        break
                    else : 
                        print("invalid move") 
                        
                elif location.lower() == "r" :
                    if move[0] == gameboard[-1][1] :
                        gameboard.append(move)
                        player.p_set.remove(move)
                        break
                    elif reversed_move[0] == gameboard[-1][1] :
                        gameboard.append(reversed_move)
                        player.p_set.remove(move)
                        break
                    else : 
                        print("invalid move")
                              
                else : 
                    print('Please Write L or R')

                    
                    
            print(f'\n ----------------------------------------- \n Game Board : {gameboard} \n ----------------------------------------- \n ')
            print('\n ----------------------------------------- \n')
            if not player.p_set : 
                print(f"Congratulations 🎉 \n Winner is {player.name}!")
                return "EndGame" 
            
            
            
        


StartGame()


