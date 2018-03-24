def x_to_dec(num, base_num):
	if base_num < 2:
		return False

	num = str(num)
	index = 0
	dec_number = 0

	if base_num == 16:
		num = num.upper()
		
		hex_digit = {
			'A' : 10,
			'B' : 11,
			'C' : 12,
			'D' : 13,
			'E' : 14,
			'F' : 15
		}
		
		for digit in num[::-1]:
			if digit in hex_digit:
				dec_number += hex_digit[digit] * base_num ** index
			else:
				dec_number += int(digit) * base_num ** index
			index += 1
			
	else:
		for digit in num[::-1]:
			dec_number += int(digit) * base_num ** index
			index += 1

	return dec_number


def dec_to_x(num, x_base):
	if x_base < 2:
		return False
	
	max_algarism = x_base - 1
	rests = list()
	base_x_num = str()

	if (num <= max_algarism and x_base != 16) or x_base == 10:
		return num

	while num > max_algarism:
		rests.append(num % x_base)
		num = num // x_base

	rests.append(num)

	if x_base == 16:
		hex_digit = {
			'10' : 'A',
			'11' : 'B',
			'12' : 'C',
			'13' : 'D',
			'14' : 'E',
			'15' : 'F'
		}
		
		for digit in rests[::-1]:
			if str(digit) in hex_digit:
				base_x_num += str(hex_digit[str(digit)])
			else:
				base_x_num += str(digit)
	else:
		for digit in rests[::-1]:
			base_x_num += str(digit)

	return base_x_num # we need this in str because hex have letters


def converter(num, in_base, out_base):
	# this is an interface to convert almost any number in any base
	# to any base
	return dec_to_x(x_to_dec(num, in_base), out_base)


def main():
	menu = [
		'Decimal -> Binário',
		'Decimal -> Hexadecimal',
		'Binário -> Decimal',
		'Binário -> Hexadecimal',
		'Hexadecimal -> Decimal',
		'Hexadecimal -> Binário',	
		'Decimal -> Octal',
		'Octal -> Decimal',
		'Hexadecimal -> Octal',
		'Octal -> Hexadecimal',
		'Binário -> Octal',
		'Octal -> Binário'
	]

	print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
	print('|              CONVERSOR DE BASES                 |')
	print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')
	print('Digite o número da conversão desejada:')
	print('+============================================+')

	# Menu creation
	for i in range(0, len(menu)):
		print('({}) - {}'.format(i + 1, menu[i]))
	
	print('+============================================+\n')

	escolha = int(input('|~~~> '))
	escolha -= 1 # to get the index, because the user will put index + 1

	if escolha not in range(0, len(menu)):
		print('Escolha uma opção válida!')
		exit()

	print('\n==============================================')
	print('Digite o número a ser convertido ({}):\n'.format(menu[escolha]))
	numero = input('|~~~> ')
	print('================================================\n')
	if escolha == 0:
		print(menu[escolha])
		print('\n{} -> {}'.format(numero, converter(numero, 10, 2)))
	elif escolha == 1:
		print(menu[escolha])
		print('\n{} -> {}'.format(numero, converter(numero, 10, 16)))
	elif escolha == 2:
		print(menu[escolha])
		print('\n{} -> {}'.format(numero, converter(numero, 2, 10)))
	elif escolha == 3:
		print(menu[escolha])
		print('\n{} -> {}'.format(numero, converter(numero, 2, 16)))
	elif escolha == 4:
		print(menu[escolha])
		print('\n{} -> {}'.format(numero, converter(numero, 16, 10)))
	elif escolha == 5:
		print(menu[escolha])
		print('\n{} -> {}'.format(numero, converter(numero, 16, 2)))
	elif escolha == 6:
		print(menu[escolha])
		print('\n{} -> {}'.format(numero, converter(numero, 10, 8)))
	elif escolha == 7:
		print(menu[escolha])
		print('\n{} -> {}'.format(numero, converter(numero, 8, 10)))
	elif escolha == 8:
		print(menu[escolha])
		print('\n{} -> {}'.format(numero, converter(numero, 16, 8)))
	elif escolha == 9:
		print(menu[escolha])
		print('\n{} -> {}'.format(numero, converter(numero, 8, 16)))
	elif escolha == 10:
		print(menu[escolha])
		print('\n{} -> {}'.format(numero, converter(numero, 2, 8)))
	elif escolha == 11:
		print(menu[escolha])
		print('\n{} -> {}'.format(numero, converter(numero, 8, 2)))

main()
