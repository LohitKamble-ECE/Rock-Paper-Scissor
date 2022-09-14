import random
import command


def play():
    """Get choices of both player and opponent and return True when player won, False when player lost or None if it is tie"""
    player = input("r for rock\np for paper\ns for scissor\n").lower()
    opponent = random.choice(["r", "p", "s"])
    print(opponent)

    if player == opponent:
        return

    if (
        (player == "r" and opponent == "s")
        or (player == "p" and opponent == "r")
        or (player == "s" and opponent == "p")
    ):
        return True

    return False


def main():
    """Start the play"""
    args = command.parse()
    player_win_count = 0
    opponent_win_count = 0
    for _ in range(args["turns"]):
        status = play()
        if status is True:
            player_win_count += 1
        elif status is False:
            opponent_win_count += 1
    
    difference = player_win_count - opponent_win_count
    if difference == 0:
        print("It's tie")
    else:
        who_won = "You" if difference > 0 else "Computer"
        print(f"{who_won} won by {abs(difference)} game point.")

        
if __name__ == "__main__":
    main()
