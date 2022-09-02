year = int(input("Input demanding year:"))
if len(str(year)) == 4:
    C = year // 100
    epact = (8 + (C // 4) - C + ((8 * C + 13) // 25) + 11 * (year % 19)) % 30
    print(f'Epakta: {epact}')
else:
    print("Are you stupid?")