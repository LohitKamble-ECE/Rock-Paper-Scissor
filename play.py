import random
import command
import sanitised_input


def play():
    """Get choices of both player and opponent and return True when player won, False when player lost or None if it is tie"""
    # Get user response until its correct.
    while True:
        try:
            player = sanitised_input.sanitised_input(
                prompt="Enter your response:\nr for rock\np for paper\ns for scissor\n",
                type_expected=str.lower,
                choices=("r", "p", "s"),
            )
        except ValueError as e:
            print(e)
            continue
        except TypeError as e:
            print(e)
            continue
        else:
            break
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
