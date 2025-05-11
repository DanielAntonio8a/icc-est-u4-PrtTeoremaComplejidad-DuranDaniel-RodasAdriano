import time
import random
import matplotlib.pyplot as plt

from sortmethods import SortMethods 

# Bro con esa madre mi pc Explota xD
sizes = [5000, 10000, 30000, 50000, 100000]


base_array = [random.randint(1, 100000) for _ in range(sizes[-1])]
results = {
    "bubble": [],
    "bubbleMejorado": [],
    "seleccion": [],
    "insercion": [],
    "shell": []
}


algorithms = {
    "bubble": SortMethods.bubble_sort,
    "bubbleMejorado": SortMethods.bubble_improved_sort,
    "seleccion": SortMethods.selection_sort,
    "insercion": SortMethods.insertion_sort,
    "shell": SortMethods.shell_sort
}


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

# Con esto genera la grafia, la clase que faltaste
for name, times in results.items():
    plt.plot(sizes, times, label=name)

plt.title("Comparación de Algoritmos de Ordenamiento")
plt.xlabel("Cantidad de valores")
plt.ylabel("Tiempo (s)")
plt.legend()
plt.grid(True)
plt.savefig("grafico_resultados.png")
plt.show()
