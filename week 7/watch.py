import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
#check if it's the right URL format
    if s.startswith("<iframe"):

#examples of link
#http://youtube.com/embed/xvFZjo5PgG0 or https://youtube.com/embed/xvFZjo5PgG0 or https://www.youtube.com/embed/xvFZjo5PgG0
        if matches := re.search(r"https?://(?:www\.)?\w+\.(?:com)/embed/(\w+)", s):
#return the link with only the youtube format
            return f"https://youtu.be/{matches.group(1)}"


if __name__ == "__main__":
    main()