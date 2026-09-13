import random


def main():
    blocked_accounts = []

    def is_admin(user):
        return user["is_admin"]

    user = {"username": "dmorgan", "is_admin": random.randint(0, 1)}

    if is_admin(user) and user["username"] not in blocked_accounts:
        print(f"{user['username']} is granted admin access")


if __name__ == "__main__":
    main()
