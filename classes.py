import random							#для генерации начальной скорости автомобилей

class Road:
	def __init__(self, id, kd, linkids, linkms, linkstarts):
		self.cars = []					#массив всех автомобилей на дороге в данный момент
		self.id = id					#0-круговая, нечетные - выходящие, нечетные+1 - соответствующие входяшие (см roadnomenc.png)
		self.kd = kd					#количество времени до появления нового автомобиля (у выходящих дорог всегда равен -1)
		self.linkids = linkids			#id дорог, на которые можно попасть из текущей
		self.linkms = linkms			#координата дороги, с которой можно съехать на соответствующую дорогу
		self.linkstarts = linkstarts	#на какой координате окажется автомобиль на новой дороги
		
class Place:							#координата относительно дорожных полос
	def __init__(self, roadid, m):
		self.roadid = roadid			#дорога, на которой находется автомобиль
		self.m = m						#метр, на котором находится автомобиль

class Car:
	def __init__(self, roadid, minspeed, maxspeed):				
		self.normalspeed = random.randint(minspeed,maxspeed)	#максимальная скорость автомобиля, скорость к которой он стремится
		self.speed = self.normalspeed							#текущая скорость автомобиля
		self.place = Place(roadid, 0)							#координата автомобиля
		
		seq = [1,3,5,7]											#все выходящие дороги
		seq.remove(roadid-1)									#кроме начальной
		self.destination = random.choice(seq)					#пункт назначения - случайная дорога, кроме начальной