while True:
    import os.path
    import random
    file_exists = os.path.exists("DATA")
    if file_exists != True:
        games = 0
        wins = 0
        with open("DATA", "a") as f:
            f.writelines([str(games)+"\n", str(wins)])
    else:
        None

    with open("DATA", "r") as f:
        v = f.readlines()
        games = int(v[0].strip("\n"))
        wins = int(v[1])

    def turn_input():
        while True:
            a = input("Your turn: ")
            if a.isdigit():
                a = int(a)
                break
            else:
                print("Try a number, maybe?")
        return a

    def batting(toss):
        global wins
        wins = wins
        runs = 0
        wickets = 2
        balls = 12
        while balls >= 0:
            n = random.randint(1, 6)
            l = turn_input()
            if l > 6:
                print("Don't cheat. You can only input a number between 1 and 6.")
                continue
            balls -= 1
            if l != n:
                runs += l
                print(f"runs={runs}")
            else:
                wickets = wickets-1
                print(f"OUT! {wickets} wickets remaining. ")
                if wickets == 0:
                    print(f"All your wickets are over.")
                    break
        cruns = 0
        cwickets = 2
        print(f"Target is {runs+1}.")
        print("You are now Balling.")
        for i in range(1, 12):
            n = random.randint(1, 6)
            l = turn_input()
            if l > 6:
                print("Lmao, you do realise that by giving numbers more than 6 you are just helping the computer by not letting it be possible for it to get catch out right? ")
            if l != n:
                cruns += n
                print(f"runs={cruns}")
                if cruns > runs:
                    break
            else:
                cwickets = cwickets-1
                print(f"OUT! {cwickets} wickets remaining. ")
                if cwickets == 0:
                    print(f"All wickets of computer are over.")
                    break
        if cruns > runs:
            print(
                f"You lost by {cruns-runs} runs and {cwickets-wickets} wickets. Better luck next time.")

        else:
            print(
                f"Congratulations! you beat computer by {runs-cruns} runs and {wickets-cwickets} wickets.")
            wins += 1

    def bowling(toss):
        global wins
        wins = wins
        cruns = 0
        cwickets = 2
        for i in range(1, 12):
            n = random.randint(1, 6)
            l = turn_input()
            if l > 6:
                print("Lmao, you do realise that by giving numbers more than 6 you are just helping the computer by not letting it be possible for it to get catch out right? ")
            if l != n:
                cruns += n
                print(f"runs={cruns}")
            else:
                cwickets = cwickets-1
                print(f"OUT! {cwickets} wickets remaining. ")
                if cwickets == 0:
                    print(f"All wickets of computer are over.")
                    break
        runs = 0
        wickets = 2
        balls = 12
        print(f"Target is {cruns+1}.")
        print("You are now Batting.")
        while balls >= 0:
            n = random.randint(1, 6)
            l = turn_input()
            if l > 6:
                print(
                    "Don't cheat. You can only input a number between 1 and 6.")
                continue
            balls -= 1
            if l != n:
                runs += l
                print(f"runs={runs}")
                if runs > cruns:
                    break
            else:
                wickets = wickets-1
                print(f"OUT! {wickets} wickets remaining. ")
                if wickets == 0:
                    print(f"All your wickets are over.")
                    break
        if cruns > runs:
            print(
                f"You lost by {cruns-runs} runs and {cwickets-wickets} wickets. Better luck next time.")
        else:
            print(
                f"Congratulations! you beat computer by {runs-cruns} runs and {wickets-cwickets} wickets.")
            wins += 1

    list = ["bat", "ball"]
    c = random.randint(0, 1)
    if c == 0:
        d = 1
    else:
        d = 0
    w = input("What do you want to do?\nPLAY - P\nINFO - I\nSTATS - S\n").upper()
    if w not in ["I", "P", "S"]:
        print("Invalid. Please try again")
        quit()

    elif w == "I":
        print("Hello! I am computer. Nice to meet you. This program is a simple game of cricket which you can play against me. In order to play just simply select 'PLAY' in the main menu and give a number between 1-6 when it says 'Your turn'. There is also a 'STATS' feature in the main menu which can show your number of wins, win rate etc. GOOD LUCK AND HAVE FUN!!")

    elif w == "P":
        t = input("Heads or tails? (1 for heads and 2 for tails)   ")
        if t not in ["1", "2"]:
            print("Invalid. Please try again")
            quit()
        y = random.randint(1, 2)
        if y == t:
            toss = input("You won the toss. Batting or bowling?\n").lower()
            if toss not in ["batting", "bowling"]:
                print("invalid. Please try again.")
                quit()
            elif toss == "batting":
                batting(toss)
            else:
                bowling(toss)
            games += 1
        else:
            print(f"You lost the toss. Computer has chosen to {list[c]}.")
            toss = list[d]
            if toss == "bat":
                batting(toss)
            else:
                bowling(toss)
            games += 1
    else:
        with open("DATA", "r") as f:
            v = f.readlines()
            games = int(v[0].strip("\n"))
            wins = int(v[1])
            print(f"Number of games played = {games}")
            print(f"Number of games won = {wins}")
            if games == 0:
                print("Cannot show win rate as games played is 0")
            else:
                print(f"Win rate = {(wins/games)*100}")

    with open("DATA", "r+") as f:
        f.truncate(0)
    with open("DATA", "a") as f:
        f.writelines([str(games)+"\n", str(wins)])
    print("do you want to continue? if yes press y, else the program will auto end")
    if (input().lower() == "y"):
        continue
    else:
        break
