ani, borya = map(int, input().split())

colors_ani = set()
colors_borya = set()

for i in range(ani):
    color = int(input())
    colors_ani.add(color)

for i in range(borya):
    color = int(input())
    colors_borya.add(color)

both_sets = colors_ani.intersection(colors_borya)

only_ani = colors_ani.difference(colors_borya)

only_borya = colors_borya.difference(colors_ani)

print(len(both_sets), *sorted(both_sets))
print(len(only_ani), *sorted(only_ani))
print(len(only_borya), *sorted(only_borya))
