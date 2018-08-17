import time
def hack(name = "null"):
	if name == "null":
		print('введите имя беседы')
	else:
		time.sleep(5)
		print('Взламываю админку в ' + name)

hack(name = "мыш")