# find the number of days in a month
def verificare(luna, an):
    if luna =="aprilie" or luna == "iunie" or luna == "august" or luna == "octombrie" or luna == "decembrie":
        print(f'{luna.capitalize()} {an} are 31 zile')
    elif (luna == "februarie" and an % 400 == 0) or (luna == "februarie" and an % 4 ==0 and an % 100 !=0):
        print(f'{luna.capitalize()} {an} are 29 zile')
    elif luna == "februarie":
        print(f'{luna.capitalize()} {an} are 28 zile')
    else:
        print(f'{luna.capitalize()} {an} are 30 zile')

# def luna(luna, year):
    # month_31 = ["december", "august"]
    # month_30 = ["november", "january"]
    # if month in month_31:
    #     print("month has 31 days")
    # elif month in month_30:
    #     print("month has 30 days")
    # elif (luna == "februarie" and an % 400 == 0) or (luna == "februarie" and an % 4 == 0 and an % 100 != 0):
    #     print(f'{luna.capitalize()} {an} are 29 zile')
    # else
    #     print("month has 29 days")

luna = input("care este luna? ")
an = int(input("care este anul? "))
verificare(luna, an)

# find the zodiacal sign when you have the day and the month of birth
def zodie(zi, luna):
    if luna == "martie" and zi >= 21 or luna == "aprilie" and zi <= 20:
        print("Semnul tau zodiacal este: Berbec")
    if luna == "aprilie" and zi >= 21 or luna == "mai" and zi <= 21:
        print("Semnul tau zodiacal este: Taur")
    if luna == "mai"  and zi >= 22 or luna == "iunie" and zi <= 21:
        print("Semnul tau zodiacal este: Gemeni")
    if luna == "iunie" and zi >= 22 or luna =="iulie" and zi <=21:
        print("Semnul tau zodiacal este: Rac")
    if luna == "iulie" and zi >=22 or luna == "august" and zi <=22:
        print("Semnul tau zodiacal este: Leu")
    if luna == "august" and zi >=23 or luna == "septembrie" and zi <=22:
        print("Semnul tau zodiacal este: Fecioara")
    if luna == "septembrie" and zi >= 23 or luna == "octombrie" and zi <=22:
        print("Semnul tau zodiacal este: Balanta")
    if luna == "octombrie" and zi >= 23 or luna == "noiembrie" and zi <21:
        print("Semnul tau zodiacal este: Scorpion")
    if luna == "noiembrie" and zi >= 22 or luna == "decembrie" and zi <=21:
        print("Semnul tau zodiacal este: Sagetator")
    if luna == "decembrie" and zi >= 22 or luna == "ianuarie" and zi <=19:
        print("Semnul tau zodiacal este: Capricorn")
    if luna == "ianuarie" and zi >= 20 or luna == "februarie" and zi <=18:
        print("Semnul tau zodiacal este: Varsator")
    if luna == "februarie" and zi >= 19 or luna == "martie" and zi <=20:
        print("Semnul tau zodiacal este: Pesti")

luna = input("care este luna? ")
zi = int(input("care este ziua? "))
zodie(zi, luna)

# display the first 10 natural numbers
def first_10_nat_numb():
    for i in range(0,10):
        print(i)

first_10_nat_numb()

# sum and average for number between 200 to 450
sum = 0
for i in range(200, 450):
    sum = sum + i
print("the sum is", sum)
print("the average number is ", sum/(450-200+1))

