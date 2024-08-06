#! python3
#EasyTicTacToe.py - A program to play  tic-tac-toe against a very weak AI

from tkinter import *
from random import choice, shuffle

i = 0 # i is used to keep track of the current turn
PLAYERS = ["X", "O"]
shuffle(PLAYERS)
BTNS = []

def restart():
  global BTNS, turn, i

  i = 0  
  for button in BTNS:
    button.config(command = lambda b = button: next_turn(b))
    button["text"] = ""
  shuffle(PLAYERS)
  turn.config(text = f"{PLAYERS[0]}'s turn")

def ai_move():
  global i
  if check_winner() is not None: # If there isn't a winner
    return
  
  current_player = PLAYERS[i % 2]
  empty_btns = [btn for btn in BTNS if btn["text"] == ""]  
  
  move = choice(empty_btns)
  move.config(text = current_player) 
  move.config(command = lambda: 1 + 1)
  move.config(fg = "red") if current_player == PLAYERS[0] else move.config(fg = "blue")
  
  next = PLAYERS[(i + 1) % 2]
  turn.config(text = f"{next}'s turn")
  i += 1
  check_winner()

def next_turn(btn):
  global i, turn
  
  current_player = PLAYERS[i % 2]
  next = PLAYERS[(i + 1) % 2]
  
  btn.config(text = current_player, command = lambda: 1 + 1)
  btn.config(fg = "red") if current_player == PLAYERS[0] else btn.config(fg = "blue")
  
  turn.config(text = f"{next}'s turn")
  
  i += 1 
  check_winner()
  window.after(1000, ai_move)
  
def check_winner():
  global turn
  
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
      return "Tie"
  return None

def game(window):
  global turn
  
  title = Label(window, text = "TicTacToe", font = ("consolas", 25), bg = "#D9D9D9")
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
  window.title("TicTacToe - Easy AI")
  window.resizable(False, False)
  
  game(window)
  window.mainloop()