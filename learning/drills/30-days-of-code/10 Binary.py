# Binary basics
# converting numbers to binary using bin() function

n = int(input().strip())
binary_string = bin(n)[:2]
print(binary_string)


ones_group = binary_string.split('0')

lengths = [len(group) for group in ones_group]
print(max(lengths))

