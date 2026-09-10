import sys
import argparse


class Repository:
    def __init__(self, path="."):
        self.path = Path(path).resolve()
        self.git_dir = self.path / ".git"

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

    if not args.command:
        parser.print_help()
        print("\nError: Please provide a valid command")
        return

    try:
        if args.command == "init":
    except Exception as e:
        print(f"Error:{e}")
        sys.exit(1)
    

main()
