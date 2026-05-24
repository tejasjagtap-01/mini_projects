'''
WorkFlow

1. Import Tkinter
2. Message box via Tkinter
3. Function for Winner Declaration
4. Check Element in Loop
5. Display Winner
6. Close the Window

'''

import tkinter as t
from tkinter import messagebox

def check_winner():
    for combo in [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8] [2,4,6]]:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            buttons[combo[0]].config(bg="green")
            buttons[combo[1]].config(bg="green")
            buttons[combo[2]].config(bg="green")
            messagebox.showinfo("Tic-Tac_Toe", f"Player {buttins[combo[0]]['text']} wins!")
            root.quit()