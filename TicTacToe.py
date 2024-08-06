#! python 3
# TicTacToe.py - Un programma per giocare a tris con tre modalità 

import TwoTicTacToe as TicTwo
import EasyTicTacToe as TicEasy
import HardTicTacToe as TicHard
from tkinter import *

def main():
  mainscreen = Tk()
  mainscreen.geometry("500x530")
  mainscreen.resizable(False, False)
  mainscreen.title("TicTacToe")
  
  two_pl = Button(mainscreen, text = "2 Players", command = lambda: TicTwo.main(), width = 20)
  easyai = Button(mainscreen, text = "Vs AI (Easy)", command = lambda: TicEasy.main(), width = 20)
  hardai = Button(mainscreen, text = "Vs AI (Hard)", command = lambda: TicHard.main(), width = 20)
  
  Label(mainscreen, text = "Tris", font = ("consolas", 25)).pack(pady = 10)
  two_pl.pack(pady = 30)
  easyai.pack(pady = 30)
  hardai.pack(pady = 30)
  
  mainscreen.mainloop()

main()