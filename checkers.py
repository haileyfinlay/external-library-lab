from numpy import random
def build_board(board_size):
    board = random.choice(['Empty','Red','Black'],
                          (board_size,board_size))
    return board

def get_count(board, cell):
    cell_color = (board == cell)
    return cell_color.sum()

if __name__ == "__main__":
    print("No")