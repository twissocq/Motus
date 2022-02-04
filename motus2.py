
tofind = 'leopard'
print('Number of letters: ' + str(len(tofind)))
display = ' '
for i in range(len(tofind)):
	display += '-'
print(display)
print()

found = False

while not found :

	guessed = tofind[0] + input(" " + tofind[0])
	guessed_list = [guessed[i] for i in range(len(guessed))]
	tofind_list = [tofind[i] for i in range(len(tofind))]
	result = ['-' for i in range(len(tofind))]

	for il, letter in enumerate(tofind):

		if guessed_list[il] == tofind[il]:
			result[il] = 'o'
			guessed_list[il] = '?'
			tofind_list[il] = '?'

		else:
			for il_guessed in range(len(guessed_list)):
				if guessed_list[il_guessed] == tofind_list[il]:
					result[il_guessed] = 'x'
					guessed_list[il_guessed] = '?'
					tofind_list[il] = '?'


	display = ' '
	for i in range(len(result)):
		display += result[i]
	print(display)
	print()

	if guessed == tofind :
		found = True
		print (" Bien joué !")
