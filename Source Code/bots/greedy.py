import random
from bots.evaluation import Evaluation

class GreedyBot(Evaluation):
    def __init__(self, bot_piece):
        super().__init__(bot_piece)

    def get_move(self, board):
        valid_moves = board.get_valid_locations()

        move_scores = []

        for move in valid_moves:
            temp_board = board.copy_board()
            temp_board.drop_piece(move, self.bot_piece)
            move_score = super().score_position(temp_board)
            move_scores.append((move, move_score))

        best_move = max(move_scores, key=lambda x: x[1])[0]
        return best_move
