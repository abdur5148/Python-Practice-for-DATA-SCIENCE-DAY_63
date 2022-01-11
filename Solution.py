numbers = [7, 9, 14, 22, 34]
number_to_find = 22

final = (numbers, number_to_find, 0, len(numbers) - 1)

if final == -1:
	print("This item was not found in the list.")
else:
	print("The number " + str(number_to_find) + " was found at index position " + str(final) + ".")
