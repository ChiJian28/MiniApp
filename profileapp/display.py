"""Text formatting for directory records."""


def format_listing(user):
    """Return one directory line: id, name, and team."""
    return f"{user['id']}: {user['name']} ({user['team']})"


def format_profile(user):
    """Return the multi-line profile shown for one person."""
    return "\n".join(
        [
            f"Loads user {user['name']} (ID {user['id']})",
            f"Title: {user['title']}",
            f"Team: {user['team']}",
            f"Email: {user['email']}",
        ]
    )
