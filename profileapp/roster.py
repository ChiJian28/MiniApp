"""Team groupings built through the shared user lookup."""

from profileapp.store import load_users
from profileapp.users import fetch_user


def member_profile(user_id):
    """Return the directory profile for one person."""
    return fetch_user(user_id)


def team_roster(team):
    """Return profiles for everyone on a team, in id order."""
    ids = sorted(
        record["id"]
        for record in load_users().values()
        if record["team"] == team
    )
    return [fetch_user(user_id) for user_id in ids]
