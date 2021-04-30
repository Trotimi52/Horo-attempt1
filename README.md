# Horo-attempt1
First initial trial
import random 
first = ["Today is perfect for new endeavors.", "The tensions of this week will feel heavier today than yesterday."]
second = ["Remember that good things come to those who work hard.", "Don't let the circumstances bring you down."]
third = ["looking ahead may seem like a waste of time, but it pays off in the end.", "Luck is on your side today."]

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

zodiac = int(input("Pick your sign by typing a number and pressing Enter: ")))

print(random.choice(first), random.choice(second), random.choice(second_add), random.choice(third))

if 0 < zodiac > 13:
    print(random.choice(first), (second), random.choice(second_add), random.choice(third))
else:
    print("INVALID")
