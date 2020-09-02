# 1
def combine_all():
    first = ['Behind', 'every', 'great', 'man']
    second = ['is', 'a', 'woman']
    third = ['rolling', 'her', 'eyes']
    
    combine = first + second + third
    
    s = " ".join(combine)    
    print(s)

combine_all()
print("\n")

#2
def merge_list():
    menus = ["chicken strip", "beef burger", "steakhouse", "mushroom swiss", "whopper"]
    price = [15,10,12,20,30]
    res = dict(zip(menus, price))
    print(str(res))

merge_list()
print("\n")

#3
def char_frequency(str1):
    dict = {}
    for n in str1.lower().replace(" ",""):
        keys = dict.keys()
        if n in keys:
            dict[n] += "*"
        else:
            dict[n] = "*"
    return dict
print(char_frequency("Mammals"))
print(char_frequency("Bruiser build"))
print("\n")

#4
def bubble_sort(numbers):
    swap = True
    i = len(numbers)-1
    step = 0
    while i > 0 and swap:
        exchanges = False
        for j in range(i):
            if numbers[j]>numbers[j+1]:
                swap = True
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                step += 1
                print(f"Step {step} : "  + str(numbers)) 
 
numbers = [12,3,5,4,8,9]
bubble_sort(numbers)
print("\n")

#5
def masking(secret_text):
    str = ''
    for char in secret_text[:-3]:
        str += '*'
    str += secret_text[-3:]
    return str
print(masking("23dn3ir30fd2eddd"))
print("\n")

#6
def find_missing_letter(chars):
    missingChar = ''
    for i in range(0,len(chars)-1):
        if(ord(chars[i+1]) - ord(chars[i]) > 1):
            missingChar = chr(ord(chars[i])+1)

    return missingChar

print(" list_letters_first =" + " " + find_missing_letter(['a','b','c','d','f']))
print(" list_letters_first =" + " " + find_missing_letter(["X","Z"]))
print("\n")

#7
def even_odd(numbers, sort_odd) : 
	j = -1

	for i in range(0, sort_odd) : 
		
		if (numbers[i] % 2 == 0) : 

			j = j + 1

			temp = numbers[i] 
			numbers[i] = numbers[j] 
			numbers[j] = temp 
				 
numbers  = [9,4,2,4,1,5,3,0] 
sort_odd = len(numbers) 

even_odd(numbers,sort_odd) 

for i in range(0,sort_odd) : 
	print( numbers[i] ,end= " ") 
