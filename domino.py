import random
import time
import ast




#------------------ Game Structure --------------------------------------





class Player() : 

    def __init__(self, name) : 
        self.name = name 
        self.p_set = [] 

    def __str__(self) :
        return f"Player : {self.name} \nYour Set : {self.p_set}"




domino_set1 = [(i, j) for i in range(6, -1, -1) for j in range(i, -1, -1)] 
#[(6, 6), (6, 5), (6, 4), (6, 3), (6, 2), (6, 1), (6, 0), 
#(5, 5), (5, 4), (5, 3), (5, 2), (5, 1), (5, 0), 
#(4, 4), (4, 3), (4, 2), (4, 1), (4, 0), 
#(3, 3), (3, 2), (3, 1), (3, 0), 
#(2, 2), (2, 1), (2, 0), 
#(1, 1), (1, 0), 
#(0, 0)]      


class Computer(Player) :

    def machine_play(self,game1,gameboard) : 
        
        while True : 
            time.sleep(3)    
            for move in self.p_set : 
                reversed_move = (move[1],move[0])
                if move[1] == gameboard[-1][1] :
                    gameboard.append(reversed_move)
                    self.p_set.remove(move)
                    print(f'Choose your Move or Write "D" to Draw {move}')
                    time.sleep(3)
                    print('Left (<--)  or  Right (-->)  __write L or R__--> R')
                    time.sleep(3)
                    return None
                elif move[1] == gameboard[0][0] :
                    gameboard.insert(0,move)
                    self.p_set.remove(move)
                    print(f'Choose your Move or Write "D" to Draw {move}')
                    time.sleep(3)
                    print('Left (<--)  or  Right (-->)  __write L or R__--> L')
                    time.sleep(3)
                    return None
                elif move[0] == gameboard[-1][1] :
                    gameboard.append(move)
                    self.p_set.remove(move)
                    print(f'Choose your Move or Write "D" to Draw {move}')
                    time.sleep(3)
                    print('Left (<--)  or  Right (-->)  __write L or R__--> R') 
                    time.sleep(3)
                    return None
                elif move[0] == gameboard[0][0] :
                    gameboard.insert(0,reversed_move)
                    self.p_set.remove(move)
                    print(f'Choose your Move or Write "D" to Draw {move}')
                    time.sleep(3)
                    print('Left (<--)  or  Right (-->)  __write L or R__--> L')
                    time.sleep(3)
                    return None
            if not game1.lr : 
                print("No tiles left to draw! , PASS !!! ")
                return None
            x = random.choice(game1.lr)
            self.p_set.append(x)
            game1.lr.remove(x)
            print('Choose your Move or Write "D" to Draw --> D')
            time.sleep(3)    
            print(f'Your Set : {self.p_set}')
            time.sleep(3)
            continue
                    
            



class Game() : 


    def __init__(self , domino_set) : 
        
        self.domino_set = domino_set
        self.lr = []
        self.players = []


    def create_players(self) :
    
        while True : 
            try :
                num_of_players = int(input(f'How Many Players ? (minimum : 2) \n {"-" * 40} \n' ))
                if 1 <= num_of_players <= 4 : 
                    break
                else : print (f'\n {"-" * 40} \n Minimum num of players is 2 and Max num is 4 ')
            except ValueError : 
                print(f'\n {"-" * 40} \n Please enter a number. ')

      
        for i in range(num_of_players) :
            name = input(f" \n Enter name for Player {i+1}: ")
            self.players.append(Player(name))
        if num_of_players == 1 : 
            self.players.append(Computer("Computer"))
        

    
    def shuffle(self)  : 
        self.lr = self.domino_set[:]
        for player in self.players : 
            for j in range(7) : 
                x = random.choice(self.lr)
                player.p_set.append(x)
                self.lr.remove(x)




                

            
#------------------ Game Logic --------------------------------------




def StartGame() :
    

    print(f'\n Loading... \n \n {"-" * 40} \n ')
    time.sleep(5)
    game1 = Game(domino_set1)
    game1.create_players()
    game1.shuffle()
    print(f'\n\n\n OK Great, Lets Start \n \n {"-" * 40} \n')
    
    gameboard = []
    while True : 
        
        play = True    
        for player in game1.players : 
            if not gameboard : 
                print(f" \n {"-" * 40} \n Game Board : [                     ] \n {"-" * 40} \n")
                print("Play the First Move")
            else : 
                print(f'\n {"-" * 50} \n Game Board : {gameboard} \n {"-" * 40} \n ')
            print(f'{player.name} Turn')
            print(player)
            
            if player.name == "Computer" : 
                player.machine_play(game1,gameboard)
                play = False
                


            
            while play :

                try :
                    
                    move = input('Choose your Move or Write "D" to Draw ')
                    if str(move).lower() == "d" :
                        if not game1.lr : 
                            print("No tiles left to draw! , PASS !!! ")
                            break
                        x = random.choice(game1.lr)
                        player.p_set.append(x)
                        game1.lr.remove(x)
                        print(f'Your Set : {player.p_set}')
                        continue
                    else : 
                        move = ast.literal_eval(move)
                        reversed_move = (move[1], move[0])
                    if not move in player.p_set : 
                        print(f'Please Choose From Your Set |^|^|^| ')
                        continue
                    
                except :
                    print(f'\n {"-" * 40} \n Please enter a Valid Move from your set or Write "D" to Draw. ')
                    continue
                
                    
                    
                
                if not gameboard : 
                    gameboard.append(move)
                    player.p_set.remove(move)
                    break
                

                location = input('Left (<--)  or  Right (-->)  __write L or R__--> ' )
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

                    
                    
            
            if not player.p_set :
                print(f'\n \n {"-" * 40} \n \n')
                print(f"Congratulations 🎉 \n Winner is {player.name}!")
                return "EndGame" 





#------------------ Game Start --------------------------------------


StartGame()
