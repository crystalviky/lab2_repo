def minx(arr):
	min = arr[0]
	for x in arr:
		if x<min:
			min=x
	return min
	
def avr(arr):
	s = 0
	for x in arr:
		s+=x
	return s/len(arr)
	
def coup(s):
	print ("\n","Шиворот на выворот: ",s[::-1])
	
ivan = {
		'name':'Иван',
		'age': 40,
		'children': [{
			'name':'Коля',
			'age': 12,
		},{
				'name':'Петр',
			    'age': 10,
		}],
	}	
				
daria = {
		'name':'Дарья',
		'age': 45,
		'children': [{
			'name':'Оля',
			'age': 20,
		},{
				'name':'Катя',
				'age':18,
		}],
	}
		
arr = [6,8,4,2,9]
print(minx(arr))
print(avr(arr))
coup ('hello,world')
emps = [ivan,daria]

print("\nИмена сотрудниоков,чьи дети стараше 18 лет:\n")
for i in emps:
	for j in i['children']:
		if j['age'] >= 18:
			print (i['name'])
			break
	
	
	
	
