# ask user to answer the question
answer = input("What is the Answer to the Great Question of Life, the Universe , and Everything?")

#output yes if answer is 42 otherwise no
if answer.strip() == "42":
    print("Yes")
elif answer.lower() == "forty-two":
    print("Yes")
elif answer.lower() == "forty two":
    print("Yes")
else:
    print("No")