def x_to_dec(num, base_num):
	#TODO: Falta implementar em hexadecimal
	num = str(num)
	index = 0
	dec_number = 0

	for digit in num[::-1]:
		dec_number += int(digit) * base_num ** index
		index += 1

	return dec_number


def dec_to_x(num, x_base):
	#TODO: Falta implementar em hexadecimal
	if x_base == 0:
		return False
	
	max_algarism = x_base - 1
	rests = list()
	base_x_num = str()

	if num <= max_algarism or x_base == 10:
		return num

	while num > max_algarism:
		rests.append(num % x_base)
		num = num // x_base

	rests.append(num)

	for digit in rests[::-1]:
		base_x_num += str(digit)

	return int(base_x_num) # mudar isso para str, já que existe o hexadecimal


def converter(num, in_base, out_base):
	return dec_to_x(x_to_dec(num, in_base), out_base)

def main():
	borda = '-='

	print('{}-'.format(borda*10))
	print('CONVERSOR DE BASES')
	print('{}-'.format(borda*10))
	
	print('Digite a base do número:')
	base_entrada = int(input())
	print('Digite o número:')
	numero = int(input())
	print('Digite a base de saída:')
	base_saida = int(input())
	
	print(converter(numero, base_entrada, base_saida))
main()
