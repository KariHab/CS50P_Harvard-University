#you may not use re
#do not validate whether the email address’s domain name actually exists.
#program that prompts the user for an email address via input
#prints Valid or Invalid, respectively, if the input is a syntatically valid email address

from validator_collection import validators

try:
    if validators.email(input("Email: ")):
        print("Valid")
except Exception:
    print("Invalid")