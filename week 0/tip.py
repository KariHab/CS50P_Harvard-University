def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    #print(dollars, percent)
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    #accept str as input(formated as $XX.XX)
    d = str(d.strip("$"))
    d = float(d)
    #print(type(d))
    #remove the $ sign
    return d
    #return it as float




def percent_to_float(p):
    #accept str as input (formated as xx%)
    p = str(p.strip("%"))
    p = float(p)
    p = p / 100
    #print(p)
    return p
    #enlever le % sign
    #return p == float("p"//100)
    #return is as float


main()