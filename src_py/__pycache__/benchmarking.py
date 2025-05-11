import sortmethods as mo
import random
import time
class Benchmarking:

    def _init_(self):
        self.mO=mo.MetodosOrdenamiento
        print("Benchmarking instanciado")

    def medir_tiempo(self,metodo, arreglo):
        inicio=time.perf_counter()
        metodo(arreglo)
        fin=time.perf_counter()
        return fin-inicio

    def build_arreglo(self,tamano):
        arreglo=[]
        for i in range(tamano):
            numero=random.randint(0,999999)
            arreglo.append(numero)
        return arreglo

    def contar_con_current_time_milles(self,tarea):
        x=time.time()
        tarea()
        fin=time.time()
        tiempo_segundos=fin-x
        return f"Tiempo en milisegundos={tiempo_segundos}"


    def contar_con_nano_time(self,tarea):
        x=time.time_ns()
        tarea()
        fin=time.time_ns()
        tiempo_nano_segundos=(fin-x)/1_000_000_000.0
        return f"Tiempo en nanosegundos={tiempo_nano_segundos}"
