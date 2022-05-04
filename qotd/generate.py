from client import get_quote


def generate_readme():
    s = get_quote()
    print("quote of the day: " + s)
    with open("../readme.md", "w+") as f:
        f.write(s)


if __name__ == "__main__":
    generate_readme()
