list1 = [21,3,4,6,33,2,3,1,3,76]
even_count, odd_count = 0, 0
for num in list1:
   if num % 2 == 0:
      even_count += 1
   else:
      odd_count += 1
print("Even numbers available in the list: ", even_count)
print("Odd numbers available in the list: ", odd_count)