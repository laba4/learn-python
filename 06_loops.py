import requests, asyncio, random

api_url = "https://jsonplaceholder.typicode.com/users"


async def get_users():
    response = requests.get(api_url)
    await asyncio.sleep(1)
    return response.json()


def numbers_game():
    secret_number = random.randint(1, 10)

    is_guessed = False

    while not is_guessed:
        guess = input("Enter a guess")

        try:
            guess = int(guess)
        except ValueError:
            print("Guess is not a number")
            continue

        if guess < secret_number:
            print("Too low")
        if guess > secret_number:
            print("Too high")
        if guess == secret_number:
            is_guessed = True
            print(f"Congrats, you guess the number {secret_number}!")


async def main():
    users = await get_users()

    for user in users:
        print(f"User {user.get('name')}'s website is {user.get('website')}")

    numbers_game()


if __name__ == "__main__":
    asyncio.run(main())
