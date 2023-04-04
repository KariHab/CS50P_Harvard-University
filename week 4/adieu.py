import inflect
p = inflect.engine()


name_list = []
while True:
    try:
        user_names = input("Name: ")
        name_list.append(user_names)
    except EOFError:
        print()
        break
name_list = p.join(name_list)
print('Adieu, adieu, to', name_list)