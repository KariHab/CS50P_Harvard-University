from validator_collection import validators

try:
    if validators.email(input("Email: ")):
        print("Valid")
except Exception:
    print("Invalid")