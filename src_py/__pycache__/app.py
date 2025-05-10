import time
import random
import matplotlib.pyplot as plt

from sortmethods import SortMethods  # Asegúrate de tener sortmethods.py con la clase definida

# Tamaños de entrada
sizes = [5000, 10000, 30000, 50000, 100000]

# Arreglo base de prueba
base_array = [random.randint(1, 100000) for _ in range(sizes[-1])]
# Diccionario de resultados
results = {
    "bubble": [],
    "bubbleMejorado": [],
    "seleccion": [],
    "insercion": [],
    "shell": []
}

# Asociación de nombres con funciones
algorithms = {
    "bubble": SortMethods.bubble_sort,
    "bubbleMejorado": SortMethods.bubble_improved_sort,
    "seleccion": SortMethods.selection_sort,
    "insercion": SortMethods.insertion_sort,
    "shell": SortMethods.shell_sort
}

# Medición de tiempos
for size in sizes:
    sub_array = base_array[:size]

    for name, func in algorithms.items():
        array_copy = sub_array.copy()
        start = time.time()
        func(array_copy)
        end = time.time()
        elapsed = round(end - start, 4)
        results[name].append(elapsed)
        print(f"Tamano: {size}, Algoritmo: {name}, Tiempo: {elapsed} segundos")

# Generar gráfica
for name, times in results.items():
    plt.plot(sizes, times, label=name)

plt.title("Comparación de Algoritmos de Ordenamiento")
plt.xlabel("Cantidad de valores")
plt.ylabel("Tiempo (s)")
plt.legend()
plt.grid(True)
plt.savefig("grafico_resultados.png")
plt.show()
