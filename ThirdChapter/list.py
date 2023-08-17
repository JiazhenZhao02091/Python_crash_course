biycile = ['a', 'b', 'c', 'd', 'e']
print(biycile[0])
print(biycile[0].title())
print(biycile)
print(biycile[-1])

print(f"My faviorate biclie is {biycile[-1].title()}.")


biycile.insert(0, "1")
m = biycile.pop(-1)
print(biycile)
print(m)


print(sorted(biycile))
biycile.reverse()
print(biycile)

print(len(biycile))


list = []
print(len(list))


for l in biycile:
    print(l)