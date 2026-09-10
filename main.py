import argparse
def main():
    parser = argparse.ArgumentParser(
        description="Git from Scratch",
        
    )
    subparsers = parser.add_subparsers(
        dest="command",
        help="Available Commands"
    )
    #init command
    init_parser = subparsers.add_parser("init", help="This allows us to initialize a new repository")

    args=parser.parse_args()
    print(args)

main()
