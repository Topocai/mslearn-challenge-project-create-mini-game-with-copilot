import random



displayPicks = {"p": "papers", "r": "rock", "s": "scissors"}
picks = ["p", "s", "r"]

gamePick = random.choice(picks)
userPick = input("🎮 Pick papers, rock or scissors (p, r, s): or type 'q' to quit: ")

gameScore = 0
userScore = 0
draws = 0

while userPick != 'q':
    while userPick not in picks:
        print("❌ Invalid pick. Please choose from (p, r, s) or type 'q' to quit:")
        userPick = input("🎮 Pick papers, rock or scissors (p, r, s): or type 'q' to quit: ")

    if userPick == gamePick:
        print(f"🤝 It's a Draw! You picked {displayPicks[userPick]} and the game picked {displayPicks[gamePick]}. 🤝")
        draws += 1
    elif (userPick == "p" and gamePick == "r") or (userPick == "s" and gamePick == "p") or (userPick == "r" and gamePick == "s"):
        userScore += 1
        print(f"🎉 You Win! You picked {displayPicks[userPick]} and the game picked {displayPicks[gamePick]}. 🎉")
    else:
        gameScore += 1
        print(f"😢 You Lose! You picked {displayPicks[userPick]} and the game picked {displayPicks[gamePick]}. 😢")

    gamePick = random.choice(picks)
    userPick = input("🎮 Pick papers, rock or scissors (p, r, s): or type 'q' to quit: ")


if gameScore > userScore:
    print(f"Game Over! You lost {gameScore} times, won {userScore} times, and drew {draws} times. 😢")
else:
    print(f"Game Over! You won {userScore} times, lost {gameScore} times, and drew {draws} times. 🎉")
