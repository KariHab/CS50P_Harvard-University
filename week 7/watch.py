import re
import sys


def main():
    print(parse(input("HTML: ")))

def parse(s):
#check if it's the right URL format
    if s.startswith("<iframe"):
        if matches := re.search(r"https?://(?:www\.)?\w+\.(?:com)/embed/(\w+)", s):
            return f"https://youtu.be/{matches.group(1)}"


if __name__ == "__main__":
    main()