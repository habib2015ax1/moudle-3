s, e = int(input("Start: ")), int(input("End: "))
sq = [i**2 for i in range(s, e + 1)]

print("Squares:", sq)
print("Even:", [n for n in sq if n % 2 == 0])
print("Odd:", [n for n in sq if n % 2 != 0])