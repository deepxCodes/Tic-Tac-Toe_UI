import tkinter as tk
from tkinter import messagebox
import math
import time

board = [' ' for _ in range(9)]

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

def handle_click(i):
    if board[i] == ' ':
        # Player's move
        board[i] = 'X'
        buttons[i].config(text='X', state='disabled')
        status_label.config(text="Bot is making a move...", fg="red")
        root.update()

        if is_winner('X'):
            messagebox.showinfo("Game Over", "You win!")
            root.quit()
            return
        if is_full():
            messagebox.showinfo("Game Over", "It's a draw!")
            root.quit()
            return

        # Bot's turn delay
        time.sleep(1)

        move = best_move()
        board[move] = 'O'
        buttons[move].config(text='O', state='disabled')

        if is_winner('O'):
            messagebox.showinfo("Game Over", "Bot wins!")
            root.quit()
            return
        if is_full():
            messagebox.showinfo("Game Over", "It's a draw!")
            root.quit()
            return

        # Back to player's turn
        status_label.config(text="Your Turn", fg="green")
        root.update()

# Tkinter UI setup
root = tk.Tk()
root.title("Tic Tac Toe - Bot vs Player")

status_label = tk.Label(root, text="Your Turn", font=('Arial', 16), fg="green")
status_label.grid(row=0, column=0, columnspan=3, pady=10)

buttons = []
for i in range(9):
    btn = tk.Button(root, text=' ', font=('Arial', 24), width=5, height=2,
                    command=lambda i=i: handle_click(i))
    btn.grid(row=(i // 3) + 1, column=i % 3)  # Start buttons from row 1
    buttons.append(btn)

root.mainloop()
