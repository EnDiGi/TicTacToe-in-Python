#! python3
# HardTicTacToe.py - A program to play tic-tac-toe against a really strong AI

from tkinter import *
from random import choice, shuffle

i = 0 # i is used to keep track of the current turn
PLAYERS = ["X", "O"]
shuffle(PLAYERS)
BTNS = []

def restart():
  global BTNS, turn, i

  i = 0
  shuffle(PLAYERS)
  for button in BTNS:
    button.config(command = lambda b = button: next_turn(b))
    button["text"] = ""
  turn.config(text = f"{PLAYERS[0]}'s turn")

def next_turn(btn):
  global i, turn
  
  current_player = PLAYERS[i % 2]
  
  btn.config(text = current_player, command = lambda: 1 + 1)
  btn.config(fg = "red")
  turn.config(text = f"{PLAYERS[1]}'s turn")
  
  i += 1 
  if current_player == PLAYERS[0] and check_winner() is not True:
    window.after(1000, ai_move)
  
def check_winner():
  global window
  
  winning_combos = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 4, 8), (2, 4, 6), (0, 3, 6), (1, 4, 7), (2, 5, 8)]
  
  for combo in winning_combos:
    if BTNS[combo[0]]["text"] == BTNS[combo[1]]["text"] == BTNS[combo[2]]["text"] != "":
      winner = BTNS[combo[0]]["text"]
      turn.config(text = f"{winner} wins!")
      for btn in BTNS:
        btn.config(command = lambda: 1 + 1)
      return

  if BTNS[0]["text"] != "" and BTNS[1]["text"] != "" and BTNS[2]["text"] != "" and BTNS[3]["text"] != "" and BTNS[4]["text"] != "" and BTNS[5]["text"] != "" and BTNS[6]["text"] != "" and BTNS[7]["text"] != "" and BTNS[8]["text"] != "":
      turn.config(text = "Tie!")
      return
  return None

def ai_move():
  global i, best
  best_score = float('-inf')
  best_move = None
  for idx in range(9):
    if BTNS[idx]["text"] == "":
      BTNS[idx]["text"] = PLAYERS[1]
      score = minimax(False)
      BTNS[idx]["text"] = ""
      if score > best_score:
        best_score = score
        best_move = idx
  
  if best_move is not None:
    BTNS[best_move].config(text = PLAYERS[1], command = lambda: None, fg = "blue")
    i += 1
    turn.config(text = f"{PLAYERS[0]}'s turn")
    check_winner()
    
def minimax(is_max):
  result = check_winner_minimax()
  if result is not None:
    return result
  
  if is_max:
    best_score = float("-inf")
    for idx in range(9):
      if BTNS[idx]["text"] == "":
        BTNS[idx]["text"] = PLAYERS[1]
        score = minimax(False)
        BTNS[idx]["text"] = ""
        best_score = max(best_score, score)
    return best_score
  else:
    best_score = float("inf")
    for idx in range(9):
      if BTNS[idx]["text"] == "":
        BTNS[idx]["text"] = PLAYERS[0]
        score = minimax(True)
        BTNS[idx]["text"] = ""
        best_score = min(score, best_score)
    return best_score
          
def check_winner_minimax():
  winning_combos = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 4, 8), (2, 4, 6), (0, 3, 6), (1, 4, 7), (2, 5, 8)]
  
  for combo in winning_combos:
    if BTNS[combo[0]]["text"] == BTNS[combo[1]]["text"] == BTNS[combo[2]]["text"] != "":
      return 1 if BTNS[combo[1]]["text"] == PLAYERS[1] else - 1

  if BTNS[0]["text"] != "" and BTNS[1]["text"] != "" and BTNS[2]["text"] != "" and BTNS[3]["text"] != "" and BTNS[4]["text"] != "" and BTNS[5]["text"] != "" and BTNS[6]["text"] != "" and BTNS[7]["text"] != "" and BTNS[8]["text"] != "":
      return 0
  return None

def game(window):
  global turn
  
  title = Label(window, text = "TicTaToe", font = ("consolas", 25), bg = "#D9D9D9")
  title.pack(pady = 10)
  restartbtn = Button(window, text = "Restart", font = ("consolas", 10), command = restart, padx = 184)
  turn = Label(window, text = f"{PLAYERS[0]}'s turn", font = ("consolas", 25), bg = "#D9D9D9")
  turn.pack(pady = 10)
  restartbtn.place(x = 17, y = 880)
  
  current_player = PLAYERS[i % 2]
    
  frame = Frame(window)
  frame.place(x = 15, y = 290)
  
  for idx in range(9):
    button = Button(frame, width = 3, height = 2, text = "", font = ("consolas", 18), activebackground = "#ACACAC", activeforeground = "black", foreground = "black")
    button.config(command = lambda b = button: next_turn(b))
    BTNS.append(button)
    button.grid(row = idx // 3, column = idx % 3, padx = 3, pady = 3)

def main():
  global window
  window = Tk()
  window.geometry("600x955")
  window.title("TicTacToe - Hard AI")
  window.resizable(False, False)
  
  game(window)
  window.mainloop()