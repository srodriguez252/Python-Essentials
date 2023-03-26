print('Bienvenido al sistema de citas del Bar Chulla Vida ')
nombre = input('Ingrese su Nombre: ')
apellido = input('Ingrese su Apellido: ')
dir= input('Ingrese su Dirección: ')
edad = int(input('Ingrese su Edad: '))

mensaje = 'No se puede realizar la reserva' if edad < 18 else f'La reserva ha sido creada con los siguientes datos: {nombre} {apellido} {dir} {edad}' 

print(mensaje)