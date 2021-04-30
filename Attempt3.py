import random 
first = ["Today is perfect for new endeavors.", "The tensions of this week will feel heavier today than yesterday.",
         "Making yourself useful is a main component of a successful day. ", "Today, exercise caution when crossing the street. ",]
second = ["Remember that good things come to those who work hard.", "Don't let the circumstances bring you down."
          "Patience is key, but sometimes a little push can get the job done. ", "A smile can get you a long way. "]
third = ["looking ahead may seem like a waste of time, but it pays off in the end.", "Luck favors those who mind the risks and take them. ",
         "Today is the day for that thing you always wanted to do. ",
         "Luck is on your side today, so seize it! ", "Things are looking up for you! "]
zodiacname = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print("1 — Aries")
print("2 — Taurus")
print("3 — Gemini")
print("4 — Cancer")
print("5 — Leo")
print("6 — Virgo")
print("7 — Libra")
print("8 — Scorpio")
print("9 — Sagittarius")
print("10 — Capricorn") 
print("11 — Aquarius")
print("12 — Pisces")
zodiacname.append(int(input("Pick your sign by typing a number and pressing Enter: ")))
for s in range(1):
    if zodiacname [s] > 13:
        zodiacname.append(s)
    print (random.choice(first))
    print (random.choice(second))
    print (random.choice(second))
    print (random.choice(third))
        
