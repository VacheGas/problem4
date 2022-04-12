def most_frequent(List):
	#print(set(List))
	List_set = set(List)
	max_count = 0
	new_list = List.copy()
	for i in List_set :
		if i == -1 :
			break
		if List.count(i) >= max_count:
			max_count = List.count(i)
	for i in List:
		if List.count(i) == max_count :
			new_list.remove(i)
		else :
			print(i)
			print(' ')
	print(new_list)
		
	return new_list
 
List = [2, 1, 2, 2, 1, 3]
print(List)
List = most_frequent(List)
print(List)
# Refresh this page to see the change in the result.
