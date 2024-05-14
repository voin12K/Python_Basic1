def geometric_progression(start, ratio):
    current = start
    while True:
        yield current
        current *= ratio

start = -2
ratio = -5
gen = geometric_progression(start, ratio)

for _ in range(6):
    print(next(gen))
