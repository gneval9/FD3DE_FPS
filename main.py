import fd3de
import time
import math as m
import keyboard as KB
import sys


cubo_load = fd3de.load("Modelos/cubo.fd3de")
pir_load = fd3de.load("Modelos/piramide.fd3de")

cubo = fd3de.spawn(cubo_load)
pir = fd3de.spawn(pir_load)

fd3de.move("z", 200, cubo)
fd3de.move("z", -300, pir)

fd3de.perspective = "up"

deg_old = 0


def orbit(obj, target, angle):
	obj["rotation"][1] += angle
	angle = m.radians(angle) * -1

	x = obj["position"][0] - target["position"][0]
	z = obj["position"][2] - target["position"][2]

	nX = x * m.cos(angle) - z * m.sin(angle)
	nZ = x * m.sin(angle) + z * m.cos(angle)

	obj["position"][0] = nX + target["position"][0]
	obj["position"][2] = nZ + target["position"][2]
		




while True:
	if KB.is_pressed("right"):
		orbit(cubo, pir, -5)

	if KB.is_pressed("left"):
		orbit(cubo, pir, 5)

	if KB.is_pressed("up"):
		cubo["position"][2] += -10
	
	if KB.is_pressed("down"):
		cubo["position"][2] += 10

	if KB.is_pressed("ctrl+right"):
		cubo["position"][0] += -10

	if KB.is_pressed("ctrl+left"):
		cubo["position"][0] += 10



	if KB.is_pressed("q"):
		sys.exit()
	


	fd3de.render(cubo, fd3de.GREEN, 0.3)

	fd3de.update()

	fd3de.clear_object(cubo, 0.3)

