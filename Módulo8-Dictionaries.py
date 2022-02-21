planet_moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}
# Añade el código para determinar el número de lunas.

# Obtenemos la lista de las lunas
# Almacenamos los resultados en una variable moons
moons = planet_moons.values()
print(moons)
# Obtenemos el total de planetas
# Almacenamos los resultados en una variable llamada years
planets = len(planet_moons.keys())
print(planets)
# Calcula el total_moons agregando todas las lunas
# Almacena su valor en una variable llamada total_moons

total_moons = 0
for moon in moons:
    total_moons = total_moons + moon

print(total_moons)

# Calcula el promedio dividiendo el total_moons por el número de planetas
average = total_moons / planets

# Muestra el promedio
print(average)

