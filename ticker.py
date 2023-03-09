from classes import *
class Ticker:
	def tick(self, game):		#функция, отвечающая за все физические изменения за единичный промежуток времени
		for road in game.roads:
			if road.kd > 0:  #на круговой и на выходящих дорогах интервал не отмеряется
				road.kd -= 1
			if road.kd == 0: 																			#если прошел интервал, 
				road.cars.append(Car(road.id, game.minspeed, game.maxspeed))							#то настало время появиться новому автомобилю
				road.kd = random.randint(game.intervalmin[int(road.id/2)-1], game.intervalmax[int(road.id/2)-1])	#и начать новый интервал
			
			for car in road.cars:
				if car.speed < car.normalspeed:						 #автомобили имеют свойство не ехать медленно когда можно ехать быстро
					car.speed += 10
				for anothercar in road.cars:
					if anothercar.place.m - car.place.m < 300 and anothercar.place.m - car.place.m > 1: #если впереди на расстоянии менее 200 метров другой автомобиль,
						car.speed = anothercar.speed													#то надо снизить скорость до скорости впередиедущего автомобиля
						break
					elif anothercar.place.m - car.place.m < 3300 and anothercar.place.m - car.place.m > 3001: 	#на круговой дороге сложно обойтись 
						car.speed = anothercar.speed															#без модульных координат.
						break																					#модуль = длина = +-3000 метров
					elif anothercar.place.m - car.place.m < -2700 and anothercar.place.m - car.place.m > -2999:
						car.speed = anothercar.speed
						break
				
				
				if road.linkids[0] == 0:																#если авто собирается заехать на круговую дорогу,
						if car.place.m + 350 > road.linkms[0] and car.place.m + 100 < road.linkms[0]:	#надо постараться избежать аварии
							for car0 in game.roads[0].cars:													#для этого при обнаружении авто, едущего 
								if car0.place.m < road.linkstarts[0] + 300 and car0.place.m > road.linkstarts[0] - 750:	#по круговой дороге близко к текущему авто
									car.speed = 0																		#надо затормозить
									break
								elif car0.place.m < road.linkstarts[0] + 3300 and car0.place.m > road.linkstarts[0] + 2250:	#снова координаты по модулю 3000
									car.speed = 0
									break
								elif car0.place.m < road.linkstarts[0] - 2700 and car0.place.m > road.linkstarts[0] - 3750:
									car.speed = 0
									break
				
				car.place.m += car.speed			#после рассчета скорости, её необходимо применить
				
				if road.id == 0:												#если машина едет по круговой
					if car.place.m > road.linkms[int((car.destination-1)/2)]:	#и проезжает перед своим поворотом
						car.place.roadid = car.destination						#надо свернуть
						car.place.m = 0											#для этого меняем координаты автомобиля
						road.cars.remove(car)									#убираем машину с прошлой дороги
						game.roads[car.destination].cars.append(car)			#и добавляем на текущую
						
				else:																			#если машина едет по прямой дороге
					if car.place.m > road.linkms[0]:											#и доезжает до своего поворота
						if road.linkids[0] == 0:												# 1) если это поворот на круговую
							car.place.roadid = 0												#то сворачиваем
							if road.linkstarts[0] > game.roads[0].linkms[int((car.destination-1)/2)]:#если позиция места назначения меньше текущей позиции авто
								car.place.m = road.linkstarts[0] - 3000							#то применяем модульные координаты
							else:
								car.place.m = road.linkstarts[0]
							road.cars.remove(car)					#убираем машину с прошлой дороги
							game.roads[0].cars.append(car)				#и добавляем на текущую
						else:																	# 2) если это выезд за пределы модели
							road.cars.remove(car)												#то удаляем машину
