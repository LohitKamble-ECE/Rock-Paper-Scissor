import argparse

def command_parser():
    """Parse the command line and return the argument passed."""
    args = argparse.ArgumentParser()
    args.add_argument("-t", "--turns", metavar="<n>", type=int, default=1, help="number of turns to play")
    return args.parse_args()