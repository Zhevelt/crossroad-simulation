from PIL import Image, ImageTk 			#для отображения изображения дороги
import math								#для рассчета положения автомобиля в двумерном пространстве
import copy

class Drawer:
	def PtoK(place):	#функция перевода координаты относительно дорожных полос в двумерные декартовы координаты
		if place.roadid == 0:	#круговая дорога
			return [int(400+math.cos((place.m+1385)/477.465)*135), int(300-math.sin((place.m+1385)/477.465)*135)]
		elif place.roadid == 1:
			return [int(265-place.m*0.3), 260]
		elif place.roadid == 2:
			return [int(place.m*0.3) - 35, 340]
		elif place.roadid == 3:
			return [360, 435+place.m*0.3]
		elif place.roadid == 4:
			return [440, 735-place.m*0.3]
		elif place.roadid == 5:
			return [int(535+place.m*0.3), 340]
		elif place.roadid == 6:
			return [int(835-place.m*0.3), 260]
		elif place.roadid == 7:
			return [440, 165-place.m*0.3]
		elif place.roadid == 8:
			return [360, -135+place.m*0.3]
			
			
	def draw(c, roads):
		c.delete("all")															#очищаем холст
		global image
		global photo
		image = Image.open("cr.png")											#открываем изображение
		photo = ImageTk.PhotoImage(image)
		image = c.create_image(400, 300, image=photo)							#рисуем его на холсте

		for road in roads:
			for car in road.cars:												#для каждого авто
				r = 20
				m = Drawer.PtoK(car.place)										#берем его декартовы координаты
				c.create_oval(m[0]-r, m[1]-r, m[0]+r, m[1]+r, fill='black')	#и рисуем на их месте кружочек
				h = copy.copy(car.place)
				h.m += 100;
				n = Drawer.PtoK(h)
				c.create_line(m[0], m[1], n[0], n[1], width='10', arrow='last', arrowshape=[15,20,15])