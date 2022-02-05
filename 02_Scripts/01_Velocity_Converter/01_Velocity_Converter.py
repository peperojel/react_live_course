# 1. Pedirme el input de velocidad
input_velocity = float(input("Ingrese la velocidad a convertir: "))

# 2. Imprima las opciones de unidades del input y que se la pregunte al usuario
print("Indique las unidades de la velocidad de entrada")
print("Opcion 1: [Km/Hr]")
print("Opcion 2: [m/s]")
input_units = int(input("Indique su opción: "))

if input_units == 1:
    input_units_text = "[Km/Hr]"
elif input_units == 2:
    input_units_text = "[m/s]"

# 3. Que me pregunte la unidad de salidad deseada
print("Indique las unidades de la velocidad de salida")
print("Opcion 1: [Km/Hr]")
print("Opcion 2: [m/s]")
output_units = int(input("Indique su opción: "))

if output_units == 1:
    output_units_text = "[Km/Hr]"
elif output_units == 2:
    output_units_text = "[m/s]"

# 4. Calcular la velocidad de salid
if input_units == 2 and output_units == 1:
    output_velocity = input_velocity*3.6
# Opción 2
elif input_units == 1 and output_units == 2:
    output_velocity = input_velocity/3.6
# Opción 3
else:
    output_velocity = input_velocity

# 5. Imprimir el resultado deseado en pantalla
print(f"{input_velocity}{input_units_text} es equivalente a {output_velocity}{output_units_text}")