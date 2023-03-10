from tkinter import * 				#для графического отображения
import random 						#для генерации интервала появления автомобилей
from classes import * 				#импорт классов из отдельного файла
from drawer import * 				#импорт классов из отдельного файла
from ticker import * 				#импорт классов из отдельного файла
from game import * 					#импорт классов из отдельного файла
import time 						#для регулирования скорости течения времени

root = Tk()										#создание графического окна
c = Canvas(width=800, height=600, bg='white')	#создание холста
c.pack()

g = Game()
										#функция жизненного цикла модели
def lifecycle():						#включает:
	g.tick()							#функцию изменения модели за единицу времени
	Drawer.draw(c, g.roads)				#функцию отображения модели
	root.after(20, lifecycle)			#таймер, отвечающий за скорость течения времени в модели
	
lifecycle()		 	#запуск жизненного цикла модели

root.mainloop()		#запуск окна