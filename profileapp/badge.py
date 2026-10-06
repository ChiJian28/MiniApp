"""Badge line using the original function name."""

import profileapp.users as users


def badge_line(user_id):
    user = users.get_user(user_id)
    return f"{user['id']}: {user['name']}"
