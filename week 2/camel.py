camel_case = input("camelCase: ")
for c in camel_case:
    if c.isupper():
        camel_case = camel_case.replace(c, "_" + c.lower())
print(camel_case)
