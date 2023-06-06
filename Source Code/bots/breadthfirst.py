import random
from collections import deque

class BFS():
    def __init__(self, bot_piece):
        self.bot_piece = bot_piece
        self.opponent_piece = 1 if bot_piece == 2 else 2

    def evaluate_move(self, board, move, piece):
        bot_copy = board.copy_board()
        bot_copy.drop_piece(move, piece)

        if bot_copy.winning_move(piece):
            return True
        return False

    def get_move(self, board):
        valid_moves = board.get_valid_locations()

        # Initialize the BFS queue
        queue = deque(valid_moves)

        winning_moves = []
        blocking_moves = []

        while queue:
            move = queue.popleft()

            # Check if the move is a winning move for the bot
            if self.evaluate_move(board, move, self.bot_piece):
                winning_moves.append(move)

            # Check if the move is a winning move for the opponent
            if self.evaluate_move(board, move, self.opponent_piece):
                blocking_moves.append(move)

        # If there is a winning move, return the first one
        if winning_moves:
            return winning_moves[0]

        # If there is a move that blocks the opponent, return the first one
        if blocking_moves:
            return blocking_moves[0]

        # If no winning or blocking move is found, return a random move
        return random.choice(valid_moves)
