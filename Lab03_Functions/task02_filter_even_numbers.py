def even_numbers(numbers):
    evens = []
    for num in numbers:
        if num % 2 == 0:
            evens.append(num)
    return evens
mylist = [32, 2, 43, 12, 9, 84, 13, 6]
result = even_numbers(mylist)
print(result)
