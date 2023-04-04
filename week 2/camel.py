camel_case = input("camelCase: ")


for c in camel_case:
    #find the capital letter
    if c.isupper():
        # corriger c dans camel_case par _+c
        camel_case = camel_case.replace(c, "_" + c.lower())


print(camel_case)
