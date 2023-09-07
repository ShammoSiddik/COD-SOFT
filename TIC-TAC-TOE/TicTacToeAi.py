import math

class Board:
    def __init__(self):
        self.board = [' ' for _ in range(9)]

    def is_full(self):
        return ' ' not in self.board

    def Winner(self, player):
        win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for combo in win_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] == player:
                return True
        return False

    def get_empty_cells(self):
        return [i for i, cell in enumerate(self.board) if cell == ' ']

    def make_move(self, move, player):
        self.board[move] = player

    def print_board(self):
        for i in range(0, 9, 3):
            print(' | '.join(self.board[i:i+3]))
            if i < 6:
                print('-' * 9)

def minimax_alpha_beta(board, depth, alpha, beta, maximizing_player, ai_player, human_player):
    if board.Winner(ai_player):
        return 1
    if board.Winner(human_player):
        return -1
    if board.is_full():
        return 0

    if maximizing_player:
        max_eval = -math.inf
        for move in board.get_empty_cells():
            board.make_move(move, ai_player)
            eval = minimax_alpha_beta(board, depth + 1, alpha, beta, False, ai_player, human_player)
            board.make_move(move, ' ')
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for move in board.get_empty_cells():
            board.make_move(move, human_player)
            eval = minimax_alpha_beta(board, depth + 1, alpha, beta, True, ai_player, human_player)
            board.make_move(move, ' ')
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def get_best_move(board, ai_player, human_player):
    best_move = None
    best_eval = -math.inf
    for move in board.get_empty_cells():
        board.make_move(move, ai_player)
        eval = minimax_alpha_beta(board, 0, -math.inf, math.inf, False, ai_player, human_player)
        board.make_move(move, ' ')
        if eval > best_eval:
            best_eval = eval
            best_move = move
    return best_move

def TicTacToe():
    ai_player = 'X'
    human_player = 'O'
    current_player = ai_player
    board = Board()

    while not board.is_full() and not board.Winner(ai_player) and not board.Winner(human_player):
        board.print_board()

        if current_player == ai_player:
            print("AI's turn:")
            move = get_best_move(board, ai_player, human_player)
        else:
            print("Your turn (0-8):")
            move = int(input())

        if move in board.get_empty_cells():
            board.make_move(move, current_player)
            current_player = human_player if current_player == ai_player else ai_player
        else:
            print("Invalid move. Try again.")

    board.print_board()
    if board.Winner(ai_player):
        print("AI wins!")
    elif board.Winner(human_player):
        print("You win!")
    else:
        print("It's a draw!")

TicTacToe()
