# Netto na brutto
tax = int(input('Podatek VAT: ')) / 100
netto = int(input('Kwota netto: '))
amount = round(netto * tax + netto, 2)
print(f'Kwota brutto to {amount}')