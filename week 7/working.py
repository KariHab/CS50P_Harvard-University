import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"^(\d\d?[:\s][0-5]?\d?\s?[APM]+)\sto\s(\d\d?[:\s][0-5]?\d?\s?(?:AM|PM))$", s):
        return f"{change_in24h(matches.group(1))} to {change_in24h(matches.group(2))}"
    raise ValueError

def change_in24h(time):
    minutes = "00"
    if ":" in time:
        #split the time into hour AM or PM based on whitespace
        hour, am_pm = time.split(" ")
        #split the time into hour and minutes bases on :
        hour, minutes = hour.split(":")
    else:
        #if no minutes, split the time into hour and AM or PM
        hour, am_pm = time.split(" ")
    if int(hour) > 12:
        raise ValueError
#for an AM hour
    if am_pm == "AM":
        if hour == "12":
            return '00' + ':' + minutes
        else:
#zfill()returns a copy of the string with ‘0’ characters padded to the leftside of the given string.
            return hour.zfill(2) + ':' + minutes
        #for a PM hour
    elif am_pm == "PM":
        if hour == "12":
            return hour.zfill(2) + ':' + minutes
        else:
            return str(int(hour) + 12) + ':' + minutes


if __name__ == "__main__":
    main()