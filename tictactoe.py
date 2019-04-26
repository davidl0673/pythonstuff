class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token

    def __repr__(self):
        return f"Player(name={self.name}, token={self.token})"

class Board:
    def __init__(self):
        self.board = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]


    def __repr__(self):
        board_str = ''
        for row in self.board:
            board_str += f"{row[0] or ' '}|{row[1] or ' '}|{row[2] or ' '}\n"
        return board_str

    def move(self, x, y, player):
        if self.board[y][x] is not None:
            return False
        
        self.board[y][x] = player.token
        return True

    def check_vertical(self, player, column_number):
        counter = 0
        for column in self.board:
            if column[column_number] == player.token:
                counter += 1
        
        return counter == 3

    def check_horizontal(self, player, row_number):
        counter = 0
        for row in self.board[row_number]:
            if row == player.token:
                counter += 1
        
        return counter == 3

    def check_diagonal(self, player, downwards):

        counter = 0

        if downwards:
            for i in range(3):
                if self.board[i][i] == player.token:
                    counter += 1
        else:
            for i in range(2, -1, -1):
                if self.board[2 - i][i] == player.token:
                    counter += 1

        return counter == 3


    def calculate_winner(self, player):
        results = []

        for i in range(3):
            results.append(self.check_horizontal(player, i))

        for i in range(3):
            results.append(self.check_vertical(player, i))

        results.append(self.check_diagonal(player, True))
        results.append(self.check_diagonal(player, False))

        return True in results

player_1 = Player('Zack', 'X')

board = Board()
board.move(0, 2, player_1)
board.move(1, 1, player_1)
board.move(2, 0, player_1)

winner = board.calculate_winner(player_1)

print(board, winner)