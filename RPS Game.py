from tkinter import *
import random
from tkinter import messagebox

window = Tk()
# Tkinter is a python GUI
window.geometry("300x350")
window.title("Rock, Paper & Scissors")
window.config(bg="#158D9C")

game_values = ["Rock", "Paper", "Scissors"]
user_score = 0
computer_score = 0


# a global variable is used cos of the variables(user_score and computer_score) outside each function of the button
# Reset Game Function
def reset_button():
    button1["state"] = "active"
    button2["state"] = "active"
    button3["state"] = "active"
    player.config(text="Player")
    computer.config(text="Computer")
    display.config(text=" ")
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    user_score_display.config(text=user_score, bg="#158D9C", fg="white")
    computer_score_display.config(text=computer_score, bg="#158D9C", fg="white")


# Exit Game Function
def exit_button():
    quitting = messagebox.askokcancel(title="Exit", message="Are you sure?")
    if quitting:
        exit_game.quit()
    else:
        reset_button()


# if player select rock
def rock():
    computer_choice = random.choice(game_values)
    if computer_choice == "Rock":
        result = "It's a tie"
        global user_score, computer_score
        user_score += 0
        computer_score += 0
        user_score_display.config(text=user_score, bg="#158D9C", fg="white")
        computer_score_display.config(text=computer_score, bg="#158D9C", fg="white")
    elif computer_choice == "Paper":
        result = "Paper covers rock! You lose"
        user_score += 0
        computer_score += 1
        user_score_display.config(text=user_score)
        computer_score_display.config(text=computer_score)
    else:
        result = "Rock smashes scissors! You win!"
        user_score += 1
        computer_score += 0
        user_score_display.config(text=user_score)
        computer_score_display.config(text=computer_score)
    display.config(text=result)
    player.config(text="Rock        ")
    computer.config(text=f"     {computer_choice}")
    if user_score == 5:
        messagebox.showinfo(title="Result", message="You won!")
        user_score = 0
        computer_score = 0
        user_score_display.config(text=user_score)
        computer_score_display.config(text=computer_score)
        reset_button()
    elif computer_score == 5:
        messagebox.showinfo(title="Result", message="Computer won!")
        user_score = 0
        computer_score = 0
        user_score_display.config(text=user_score)
        computer_score_display.config(text=computer_score)
        reset_button()


# if player select paper
def paper():
    computer_choice = random.choice(game_values)
    if computer_choice == "Paper":
        result = "It's a tie"
        global user_score, computer_score
        user_score += 0
        computer_score += 0
        user_score_display.config(text=user_score)
        computer_score_display.config(text=computer_score)
    elif computer_choice == "Scissors":
        result = "Scissors cut paper! You lose"
        user_score += 0
        computer_score += 1
        user_score_display.config(text=user_score)
        computer_score_display.config(text=computer_score)
    else:
        result = "Paper covers rock! You win!"
        user_score += 1
        computer_score += 0
        user_score_display.config(text=user_score)
        computer_score_display.config(text=computer_score)
    display.config(text=result)
    player.config(text="Paper        ")
    computer.config(text=f"     {computer_choice}")
    if user_score == 5:
        messagebox.showinfo(title="Result", message="You won!")
        user_score = 0
        computer_score = 0
        user_score_display.config(text=user_score)
        computer_score_display.config(text=computer_score)
        reset_button()
    elif computer_score == 5:
        messagebox.showinfo(title="Result", message="Computer won!")
        user_score = 0
        computer_score = 0
        user_score_display.config(text=user_score)
        computer_score_display.config(text=computer_score)
        reset_button()


# if player select scissors
def scissors():
    computer_choice = random.choice(game_values)
    if computer_choice == "Scissors":
        result = "It's a tie"
        global user_score, computer_score
        user_score += 0
        computer_score += 0
        user_score_display.config(text=user_score)
        computer_score_display.config(text=computer_score)
    elif computer_choice == "Paper":
        result = "Scissors cut paper! You win"
        user_score += 1
        computer_score += 0
        user_score_display.config(text=user_score)
        computer_score_display.config(text=computer_score)
    else:
        result = "Rock smashes scissors! You lose!"
        user_score += 0
        computer_score += 1
        user_score_display.config(text=user_score)
        computer_score_display.config(text=computer_score)
    display.config(text=result)
    player.config(text="Scissors        ")
    computer.config(text=f"     {computer_choice}")
    if user_score == 5:
        messagebox.showinfo(title="Result", message="You won!")
        user_score = 0
        computer_score = 0
        user_score_display.config(text=user_score)
        computer_score_display.config(text=computer_score)
        reset_button()
    elif computer_score == 5:
        messagebox.showinfo(title="Result", message="Computer won!")
        user_score = 0
        computer_score = 0
        user_score_display.config(text=user_score)
        computer_score_display.config(text=computer_score)
        reset_button()


# adding Label, Frame, Button from tkinter

game_label = Label(text="ROCK PAPER SCISSORS", font=("courier", 15, "bold"), bg="#158D9C", fg="white")
game_label.pack(pady=20)

frame = Frame(window, bg="#158D9C")
frame.pack()
player = Label(frame, text="Player", font=("normal", 10, "bold"), bg="#158D9C", fg="white")
player.pack(side=LEFT)
versus = Label(frame, text="VS", font=("normal", 10, "bold"), bg="#158D9C")
versus.pack(side=LEFT)
computer = Label(frame, text="Computer", font=("normal", 10, "bold"), bg="#158D9C", fg="white")
computer.pack()

display = Label(text="Outcome", font=("normal", 10, "bold"), bg="#158D9C", fg="white", width=30, borderwidth=1,
                relief="solid")
display.pack(pady=20)

frame3 = Frame(window, bg="#158D9C")
frame3.pack()
user_score_display = Label(frame3, text=user_score, font=10, bg="#158D9C", fg="white")
user_score_display.pack(side=LEFT)
diff = Label(frame3, text=":", font=10, bg="#158D9C")
diff.pack(side=LEFT)
computer_score_display = Label(frame3, text=computer_score, font=10, bg="#158D9C", fg="white")
computer_score_display.pack()

frame2 = Frame(window, bg="#158D9C")
frame2.pack()
button1 = Button(frame2, text="Rock", font=10, bg="white", fg="#964B00", command=rock)
button1.pack(side=LEFT, padx=10)
button2 = Button(frame2, text="Paper", font=10, bg="#158D9C", fg="white", command=paper)
button2.pack(side=LEFT, padx=10)
button3 = Button(frame2, text="Scissors", font=10, bg="white", fg="blue", command=scissors)
button3.pack(side=LEFT, padx=10)

frame3 = Frame(window, bg="#158D9C")
frame3.pack()
reset = Button(frame3, text="Reset ", font=10, fg="black", bg="white", command=reset_button)
reset.pack(side=LEFT)
exit_game = Button(frame3, text=" Exit  ", font=10, fg="red", bg="white", command=exit_button)
exit_game.pack(side=RIGHT, padx=20, pady=30)

window.mainloop()
