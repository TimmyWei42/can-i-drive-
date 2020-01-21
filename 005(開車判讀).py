country_1 = input('請輸入國家(中文): ')
age_1 = input('請輸入年齡: ')
age_1 = float(age_1)
if country_1 == '台灣':
	if age_1 >= 18:
		print('你可以開車')
	else:
		print('你還無法開車')
elif country_1 == '美國':
	if age_1 >= 16:
		print('你可以開車')
	else:
		print('你還無法開車')
else:
	print('你只能輸入美國或台灣') 
country_2 = input('請再次輸入國家(中文): ')
age_2 = input('請再次輸入年齡: ')
age_2 = float(age_2)
if country_2 == '台灣':
	if age_2 >= 18:
		print('你可以開車')
	else:
		print('你還無法開車')
elif country_2 == '美國':
	if age_2 >= 16:
		print('你可以開車')
	else:
		print('你還無法開車') 
