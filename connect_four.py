from pprint import pprint

class Player:
    def __init__(self, name, color):
        self.name = name 
        self.color = color
   
    def __repr__(self):
        return f"Player(name={self.name}, token={self.color})"

class Game:
    def __init__(self):
        self.board = [
            [],   #checking this list is backwards, going acrosss is checking down
            [],
            [],
            [],
            [],
            [],
            [],
        ]
    def get_height(self, position):
        column = self.board[position]
        return len(column)


    def move(self, player, position):
        column = self.board[position]
        column.append(player.color)

    
    def is_full(self):
        counter = 0
        for column in self.board:
            counter += len(column)

        return counter >= 42

def play_game():
    game = Game()
    player_1 = Player('david', 'r')
    player_2 = Player('bob', 'b')

    with open('moves.txt') as f:
        is_red = True 

        for line in f:
            if is_red == True:
                game.move(player_1, int(line) - 1)
            else:
                game.move(player_2, int(line) - 1)
            is_red = not is_red
        print(game.board)

        

# game = Game()
# player = Player('David', 'r')
# game.move(player,0)
# game.is_full()
# pprint(game.board)
# print(game.get_height(0))
play_game()
