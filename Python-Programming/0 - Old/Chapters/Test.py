alt = ['car', 'girl', 'tofu', 'rca', 'bad', 'adb','sara', 'raas']
elem = []
for i in alt:
    for j in range(len(alt)):
        if sorted(i) == sorted(alt[j]) and j != alt.index(i):
           elem.append(i)
print (elem)

alt1 = [2, 4, -12, 6, 3, 4]

print (alt1)


elem1 = []

for i in alt1:
    for j in range(len(alt1)):
        if abs(alt1[j]+i) == 6 and j != alt1.index(i):
           elem1.append((alt1.index(i),j))
print(elem1)
