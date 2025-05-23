from decimal import Decimal

def vat_faktura(lista):
    suma = 0
    for elem in lista:
        suma += elem
    return round(suma * 23) / 100
    
def vat_paragon(lista):
    suma = 0
    for elem in lista:
        suma += elem * 0.23
    return round(suma * 100) / 100

# czemu nie tak?
# def vat_paragon(lista):
#     suma = 0
#     for elem in lista:
#         suma += round(elem * 23) /100
#     return suma

zakupy = (3.14, 2.78, 1.68, 4.69, 0.57, 9.86, 6.61, 29.4, 6.02, 1.38, 0.00)
# zakupy2 = (Decimal('3.14'), Decimal('2.78'), Decimal('1.68'), Decimal('4.69'),Decimal('0.57'), Decimal('9.86'), Decimal('6.61'), Decimal('29.4'), Decimal('6.02'), Decimal('1.38'), Decimal('0.00'))

print(vat_faktura(zakupy) == vat_paragon(zakupy))
# print(vat_faktura(zakupy2) == vat_paragon(zakupy2))

