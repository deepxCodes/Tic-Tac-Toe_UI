import math
import time

board = [' ' for _ in range(9)]

def print_board():
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]} |")

def is_winner(player):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def is_full():
    return ' ' not in board

def minimax(depth, is_maximizing):
    if is_winner('X'):
        return -1
    if is_winner('O'):
        return 1
    if is_full():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(depth + 1, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(depth + 1, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

def best_move():
    best_score = -math.inf
    move = 0
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

def player_move():
    try:
        move = int(input("Enter your move (1-9): ")) - 1
        if move < 0 or move > 8:
            print("Invalid input. Choose a number from 1 to 9.")
            player_move()
        elif board[move] == ' ':
            board[move] = 'X'
        else:
            print("Invalid move. Try again.")
            player_move()
    except ValueError:
        print("Please enter a number.")
        player_move()

print("Welcome to Tic Tac Toe! You are 'X' and the bot is 'O'.")
print_board()

while True:
    
    player_move()
    print_board()
    if is_winner('X'):
        print("You win!")
        break
    if is_full():
        print("It's a draw!")
        break

    
    print("Bot is making a move...")
    time.sleep(1)
    move = best_move()
    board[move] = 'O'
    print("Bot's move:")
    print_board()
    if is_winner('O'):
        print("Bot wins!")
        break
    if is_full():
        print("It's a draw!")
        break
