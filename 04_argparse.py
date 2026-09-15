import argparse, requests, json, os

base_url = os.getenv("BASE_URL")


def parse_json(value):
    required_fields = {"title", "excitement", "proficiency"}

    try:
        data = json.loads(value)
    except json.JSONDecodeError:
        raise argparse.ArgumentTypeError("Must be valid JSON")

    if not isinstance(data, dict):
        raise argparse.ArgumentTypeError("Must be a JSON object")

    if set(data) != required_fields:
        raise argparse.ArgumentTypeError(
            'Must contain exactly "title", "excitement" and "proficiency"'
        )

    for field in required_fields:
        if not data[field]:
            raise argparse.ArgumentTypeError(f'"{field}" cannot be empty')

    return data


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()

    group.add_argument(
        "--add",
        type=parse_json,
        metavar="Add skill",
        help='Adds a new skill, e. g. { "title" : "Active Directory", "excitement" : "low", "proficiency" : "beginner" }',
    )

    group.add_argument(
        "--delete",
        type=int,
        nargs="+",
        metavar="Delete skill",
        help="Deletes one or more skills by id",
    )

    args = parser.parse_args()

    if not base_url:
        parser.error("BASE_URL needs to be set as an environment variable")

    if args.add:
        requests.post(base_url, json=args.add)

    if args.delete:
        for id in args.delete:
            requests.delete(f"{base_url}/{id}")


if __name__ == "__main__":
    main()
