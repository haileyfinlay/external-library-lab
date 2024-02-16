from checkers import build_board, get_count
def game():
    board_size = int(input("Enter a square board size between 4 and 16: "))
    board = build_board(board_size)
    print(board)
    print(f"Black: {get_count(board, 'Black')}")
    print(f"Red: {get_count(board, 'Red')}")
    print(f"Empty: {get_count(board, 'Empty')}")

if __name__ == "__main__":
    game()