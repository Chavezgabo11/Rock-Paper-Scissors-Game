from random import randint

# re-import our game variables
from gameComponents import gameVars, winLose, weaponChoose, Messages

while gameVars.player_choice is False:
    print(" __| |____________________________________________| |__")
    print("(__   ____________________________________________   __)")
    print("   | |                                            | |")
    print("   | |                RPS GAME                    | |")
    print("   | |           Computer Lives:", gameVars.computer_lives, "/", gameVars.total_lives, "           | |")
    print("   | |            Player Lives:", gameVars.player_lives, "/", gameVars.total_lives, "            | |")
    print("   | |                                            | |")
    print(" __| |____________________________________________| |__")
    print("(__   ____________________________________________   __)")
    print("   | |                                            | |")
    print("Choose your weapon! Or type quit to exit\n") #\n means "new line"
    gameVars.player_choice = input("Choose rock, paper, or scissors: \n")

    if gameVars.player_choice == "quit":
        print("★   You choose to quit  ★")
        Messages.GoodBye()
        exit()

    gameVars.computer_choice = gameVars.choices[randint(0, 2)]

    print("user chose: " + gameVars.player_choice)
    print("computer chose: " + gameVars.computer_choice)

    weaponChoose.weapon()

    if gameVars.player_lives == 0:
        winLose.winorlose("lost")
    elif gameVars.computer_lives == 0:
        winLose.winorlose("won")
    else:
        gameVars.player_choice = False
