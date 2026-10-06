"""Badge line using the original one-argument lookup."""

from profileapp.users import get_user


def badge_line(user_id):
    user = get_user(user_id)
    return f"{user['id']}: {user['name']}"
