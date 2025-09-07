import random
import os.path
import json
random.seed()

def draw_board(board):
   """Draws the noughts and crosses board."""
   for row in board:
        print("|".join(row))
        print("-" * 5)
    

def welcome(board):
    """Prints the welcome message and displays the board."""
    print("Welcome to Noughts and Crosses!")
    draw_board(board)
    

def initialise_board(board):
     """Sets all elements of the board to one space ' '."""
    for i in range(3):
        for j in range(3):
            board[i][j] = ' '
    return board

    
def get_player_move(board):
    """Ask the user for the cell to put the X in, and return row and col."""
    while True:
        try:
            row = int(input("Enter the row number (1-3): ")) - 1
            col = int(input("Enter the column number (1-3): ")) - 1
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
                return row, col
            else:
                print("Invalid move. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    return row, col

def choose_computer_move(board):
   """Let the computer choose a cell to put a nought in and return row and col."""
    available_moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    return random.choice(available_moves)
    return row, col


def check_for_win(board, mark):
    """Check if either the player or the computer has won."""
    
    for row in board:
        if all(cell == mark for cell in row):
            return True
    
    for col in range(3):
        if all(board[row][col] == mark for row in range(3)):
            return True
    
    if all(board[i][i] == mark for i in range(3)) or \
       all(board[i][2-i] == mark for i in range(3)):
        return True
    return False

def check_for_draw(board):
   """Check if all cells are occupied."""
    for row in board:
        if ' ' in row:
            return False
    return True
        
def play_game(board):
   """Play the game."""
    initialise_board(board)
    welcome(board)
    while True:
        
        print("Player's turn (X):")
        player_row, player_col = get_player_move(board)
        board[player_row][player_col] = 'X'
        draw_board(board)
        if check_for_win(board, 'X'):
            print("Congratulations! You win!")
            return 1
        if check_for_draw(board):
            print("It's a draw!")
            return 0
        
        
        print("Computer's turn (O):")
        computer_row, computer_col = choose_computer_move(board)
        board[computer_row][computer_col] = 'O'
        draw_board(board)
        if check_for_win(board, 'O'):
            print("Computer wins! Better luck next time.")
            return -1
        if check_for_draw(board):
            print("It's a draw!")
    return 0
                    
                
def menu():
     """Get user input of either '1', '2', '3' or 'q'."""
    print("Menu:")
    print("1. Play game")
    print("2. Save score in file 'leaderboard.txt'")
    print("3. Load and display the scores from the 'leaderboard.txt'")
    print("q. End the program")
    choice = input("Enter your choice (1, 2, 3, or q): ")
    return choice


def load_scores():
     """Load the leaderboard scores from the file 'leaderboard.txt'."""
    if os.path.exists('leaderboard.txt'):
        with open('leaderboard.txt', 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return {}
    else:
        return {}
    return leaders
    
def save_score(score):
    """Ask the player for their name and then save the current score to the file 'leaderboard.txt'."""
    name = input("Enter your name: ")
    scores = load_scores()
    scores[name] = score
    with open('leaderboard.txt', 'w') as file:
        json.dump(scores, file)
    return


def display_leaderboard(leaders):
    """Display the leaderboard scores."""
    if leaders:
        print("Leaderboard:")
        for name, score in leaders.items():
            print(f"{name}: {score}")
    else:
        print("Leaderboard is empty.")
