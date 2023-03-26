edad = int(input('Ingrese su edad: '))

if(edad >= 0 and edad <= 5):
    mn = 'Se encuentra en la primera infancia'
elif(edad >= 6 and edad <= 11):
    mn = 'Se encuentra  en la infancia'
elif(edad >= 12 and edad <= 18):
    mn = 'Se en cuentra en la adolescencia'
elif(edad >= 14 and edad <= 26):
    mn = 'Se encuentra en la juventud'
elif(edad >= 27 and edad <= 59):
    mn = 'Se encuentra en la adultez'
elif(edad >= 60):
    mn = 'Usted es una persona mayor'
else:
    mn = 'ingrese una edad correcta'
 
print(mn)