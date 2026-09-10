import sys
import argparse


class Repository:
    def __init__(self, path="."):
        self.path = Path(path).resolve()
        self.git_dir = self.path / ".git"

        # .git/objects
        self.objects_dir = self.git_dir / "objects"

        # .git/refs
        self.ref_dir = self.git_dir / "refs"
        self.heads_dir = self.ref_dir / "heads"

        # HEAD file
        self.head_file = self.git_dir / "HEAD"

        # .git/index
        self.index_file = self.git_dir / "index"

    def init(self) -> bool:
        if self.git_dir.exists():
            return False

        # create directories
        self.git_dir.mkdir()
        self.objects_dir.mkdir()
        self.ref_dir.mkdir()
        self.heads_dir.mkdir()

        # create initial HEAD pointing to a branch
        self.head_file.write_text("ref: refs/heads/master\n")

        self.save_index({})

        print(f"Initialized empty Git repository in {self.git_dir}")

        return True

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
