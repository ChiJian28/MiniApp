"""Command-line interface for the team directory."""

import argparse
import sys

from profileapp.display import format_listing, format_profile
from profileapp.roster import member_profile, team_roster
from profileapp.store import load_users
from profileapp.directory import UnknownUser


def build_parser():
    """Return the parser for list, show, and team."""
    parser = argparse.ArgumentParser(
        prog="profileapp",
        description="Look up people in the team directory.",
    )
    commands = parser.add_subparsers(dest="command", required=True)

    commands.add_parser("list", help="List everyone in the directory")

    show = commands.add_parser("show", help="Show one person's profile")
    show.add_argument("--id", type=int, required=True, help="Directory id")

    team = commands.add_parser("team", help="List people on one team")
    team.add_argument("name", help="Team name, for example Engineering")

    return parser


def main(argv=None):
    """Run one directory command. Return a process exit code."""
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        if args.command == "list":
            records = sorted(load_users().values(), key=lambda item: item["id"])
            for record in records:
                print(format_listing(record))
            return 0
        if args.command == "show":
            print(format_profile(member_profile(args.id)))
            return 0
        if args.command == "team":
            members = team_roster(args.name)
            if not members:
                print(f"No people on team {args.name}", file=sys.stderr)
                return 1
            for user in members:
                print(format_listing(user))
            return 0
    except UnknownUser as exc:
        print(exc, file=sys.stderr)
        return 1
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
