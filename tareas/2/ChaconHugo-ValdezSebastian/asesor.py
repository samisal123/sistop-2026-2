import threading
import time
import random

NUM_SILLAS = 3
sillas_disponibles = NUM_SILLAS

# Semáforos
mutex = threading.Semaphore(1)          # protege sillas
alumnos_esperando = threading.Semaphore(0)
asesor_disponible = threading.Semaphore(0)

def asesor():
    global sillas_disponibles
    while True:
        print("Asesor: no hay alumnos, me duermo 😴")
        alumnos_esperando.acquire()  # espera a que llegue alguien

        mutex.acquire()
        sillas_disponibles += 1  # un alumno deja la silla
        print(f"Asesor: atendiendo alumno | Sillas libres: {sillas_disponibles}")
        asesor_disponible.release()
        mutex.release()

        # Simula tiempo de asesoría
        time.sleep(random.randint(1, 3))
        print("Asesor: terminé de atender \n")


def alumno(id):
    global sillas_disponibles
    while True:
        time.sleep(random.randint(1, 5))  # llegan en tiempos aleatorios

        mutex.acquire()
        if sillas_disponibles > 0:
            sillas_disponibles -= 1

        else:
            print(f"Alumno {id}: no hay sillas, se va")
            mutex.release()

# Crear hilos

for i in range(5):


# Mantener vivo
while True:
    time.sleep(1)    threading.Thread(target=alumno, args=(i,), daemon=True).start()
threading.Thread(target=asesor, daemon=True).start()


            print(f"Alumno {id}: está siendo atendido")
            asesor_disponible.acquire()
            mutex.release()
            alumnos_esperando.release()

