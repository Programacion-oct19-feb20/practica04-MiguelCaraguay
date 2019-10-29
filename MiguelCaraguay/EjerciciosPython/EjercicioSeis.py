""" 
	@autor: MiguelCaraguay
	nombre: EjercicioSeis.py
	descripcion:...

	Miguel Caraguay -- 17
	Su suma de notas es: 30
	Su promedio es:15
"""
# System.out.println("Ingrese su nombre");
# nombre = entrada.nextLine();

nombre = input("Ingrese su nombre:\n")

edad = input("Ingrese su edad: \n")
nota1 = input("Ingrese el valor se su nota 1:")
nota2 = input("Ingrese el valor se su nota 2:")


suma = int(nota1)  + int(nota2);
promedio = int(suma)/2

print("%s -- %s\nSu suma es: %s\n Su promedio es: %s" %
 (nombre,edad, suma,promedio))

