import math

def calcular_longitud(x, y):
    lam = math.atan2(y, x)
    return lam

# Solicitar al usuario que ingrese los valores
a = float(input("Ingrese el valor del semieje mayor (en metros): "))
f = float(input("Ingrese el valor de aplanamiento f: "))
x = float(input("Ingrese la coordenada x: "))
y = float(input("Ingrese la coordenada y: "))
z = float(input("Ingrese la coordenada z: "))

# Calcular la raíz cuadrada de x^2 + y^2
p = math.sqrt(x ** 2 + y ** 2)

# Estimación inicial de la latitud geodésica (phi_0)
phi_prev = math.atan(z / (p * (1 - 2 * f + f ** 2))) * (1 + f ** 2 / (1 - f ** 2))

# Inicializar N usando la misma estimación inicial de phi
N_prev = a / math.sqrt(1 - (2 * f - f ** 2) * math.sin(phi_prev) ** 2)

# Iterar para mejorar la estimación de la latitud
for _ in range(5):
    tan_phi1 = (z + (2 * f - f ** 2) * N_prev * math.sin(phi_prev)) / p
    phi = math.atan(tan_phi1)
    
    # Calcular N usando la misma iteración de phi
    N = a / math.sqrt(1 - (2 * f - f ** 2) * math.sin(phi) ** 2)
    
    if abs(phi - phi_prev) < 1e-12:
        break
    
    phi_prev = phi
    N_prev = N

# Calcular la longitud geodésica (lambda)
lam = calcular_longitud(x, y)

# Calcular la altura sobre la superficie de referencia (h)
h = math.sqrt(x ** 2 + y ** 2) / math.cos(phi) - N

# Convertir las coordenadas a grados
phi_deg = math.degrees(phi)
lam_deg = math.degrees(lam)

# Mostrar resultados
print("Latitud geodésica (phi):", phi_deg)
print("Longitud geodésica (lambda):", lam_deg)
print("Altura sobre la superficie de referencia (h):", h)
6378388