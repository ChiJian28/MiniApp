"""Shared user lookup for the profile service."""

from profileapp.store import load_users


def get_user(user_id):
    """Return a copy of the directory record for this id."""
    return dict(load_users()[user_id])


if __name__ == "__main__":
    user = get_user(1)
    print(f"user {user['id']}: id={user['id']} name={user['name']}")
