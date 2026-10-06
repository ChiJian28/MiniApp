"""Public lookup API for the team directory.

The shared contract is get_user(user_id). Callers pass the directory id
and receive one record.
"""

from profileapp.store import load_users


class UnknownUser(LookupError):
    """Raised when the directory has no record for an id."""

    def __init__(self, user_id):
        self.user_id = user_id
        super().__init__(f"No user with id {user_id}")


def get_user(user_id):
    """Return a copy of the directory record for user_id."""
    try:
        key = int(user_id)
    except (TypeError, ValueError) as exc:
        raise UnknownUser(user_id) from exc

    try:
        record = load_users()[key]
    except KeyError as exc:
        raise UnknownUser(key) from exc

    return {
        "id": record["id"],
        "name": record["name"],
        "email": record["email"],
        "team": record["team"],
        "title": record["title"],
    }
