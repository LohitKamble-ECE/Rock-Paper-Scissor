import argparse

def parse():
    """Define and parse the command line and returns the arguments as dictionary."""
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--turns", metavar="<n>", type=int, default=1, help="number of turns to play")
    return vars(parser.parse_args())