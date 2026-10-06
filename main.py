"""Load one user through the shared lookup."""

from users import get_user


def main():
    user = get_user(1)
    print(f"Loads user {user['name']} (ID {user['id']})")


if __name__ == "__main__":
    main()
