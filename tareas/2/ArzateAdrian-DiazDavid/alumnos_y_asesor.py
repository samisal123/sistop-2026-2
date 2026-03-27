#!/usr/bin/env python3

import threading as th
import random
import time

numero_sillas = 10



class Alumno(th.Thread):
	def __init__(self, id, sillas, mutex):
		super().__init__()
		self.id = id
		self.silla = sillas
		self.mutex = mutex
		self.numero_dudas = random.randint(1, 10)

	def run(self):
		self.silla.acquire()
		print(f"El alumno {self.id} entró al cubiculo")

		self.resolver_dudas()

		self.silla.release()
		print(f"El alumno {self.id} salió del cubiculo")

	def resolver_dudas(self):
		while self.numero_dudas != 0:
			
			self.mutex.acquire()
			
			print(f"El alumno {self.id} está relaizando resolviendo una duda")
			self.numero_dudas -= 1
			
			self.mutex.release()
			
			time.sleep(1)

		print(f"El alumno {self.id} resolvio todas sus dudas") 

