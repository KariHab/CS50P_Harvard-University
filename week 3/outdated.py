month_year = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
for _ in month_year:
    try:
        date = input("Date: ")
        if date.__contains__("/"):
            date = date.strip().split("/")
            m, d, y = date
            m = int(m)
            d = int(d)
            if d <= 31 and m <= 12:
                print(f"{y}-{m:02}-{d:02}")
                break

        else:
            if date.__contains__(","):
                date = date.title().replace(",", ""). split(" ")
                m, d, y = date
                m = month_year.index(m)+1
                d = int(d)
                if d <= 31 and m <= 12:
                    print(f"{y}-{m:02}-{d:02}")
                    break

    except(KeyError, ValueError):
        pass
