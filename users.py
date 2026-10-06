"""Shared user lookup for the profile service."""

USERS = {
    1: {
        "id": 1,
        "name": "Alice Chen",
    },
}


def get_user(user_id):
    """Return the user with this id and print their id and name."""
    user = USERS[user_id]
    print(f"user {user['id']}: id={user['id']} name={user['name']}")
    return user


if __name__ == "__main__":
    get_user(1)
