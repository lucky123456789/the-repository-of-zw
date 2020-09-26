def ks_jiami(words, process=3):
	result_1 = ''
	words = list(words)
	for word_store_1 in words:
		word_store_1 = ord(word_store_1)
		if word_store_1 >= 65 and word_store_1 <= 90:
			word_store_1 = 65 + ((word_store_1 - 65) + process) % 26
			result_1 = result_1 + chr(word_store_1)
		elif word_store_1 >= 97 and word_store_1 <= 122:
			word_store_1 = 97 + ((word_store_1 - 97) + process) % 26
			result_1 = result_1 + chr(word_store_1)
		else:
			print('输入错误，请重试！')
	return result_1


def ks_jiemi(words, process=3):
	result_2 = ''
	words = list(words)
	for word_store_2 in words:
		word_store_2 = ord(word_store_2)
		if word_store_2 >= 65 and word_store_2 <= 90:
			word_store_2 = 65 + ((word_store_2 - 65) -process) % 26
			result_2 = result_2 + chr(word_store_2)
		elif word_store_2 >= 97 and word_store_2 <= 122:
			word_store_2 = 97 + ((word_store_2 - 97) -process) % 26
			result_2 = result_2 + chr(word_store_2)
		else:
			print('输入错误，请重试！')
	return result_2
	


def main():
	print('欢迎使用凯撒加密程序')
	print('1、加密	2、解密	3、退出')
	choice = input('请选择需要的操作: ')
	if choice == '1':
		words = input('请输入需要加密的字符串（大小写均可): ')
		process = int(input('请输入需要偏移的位数: '))
		final = ks_jiami(words, process)
		print(final)
	
	elif choice == '2':
		words = input('请输入需要解密的字符串（小写均可）: ')
		process = int(input('请输入需要偏移的位数： '))
		final = ks_jiemi(words, process)
		print(final)
	
	elif choice == '3':
		exit()
	else:
		print('输入错误，请重试!')
		main()

if __name__ == '__main__':
	main()
