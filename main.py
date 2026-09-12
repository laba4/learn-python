import math


def get_distance(a, b):
    return math.sqrt(a**2 + b**2)


def main():
    print(round(get_distance(3, 5), 2))


if __name__ == "__main__":
    main()
