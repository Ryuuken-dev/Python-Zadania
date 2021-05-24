temperature = float(input('Podaj temperaturę: '))

if temperature <= 10:
    print('Zostań w domu')
elif 10 < temperature < 20:
    print('Weź kurtkę!')
else:
    print('Baw się dobrze!')