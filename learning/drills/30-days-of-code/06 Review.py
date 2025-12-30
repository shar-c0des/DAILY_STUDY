num_test = int(input().strip())


for _ in range(num_test):
    word = input().strip()
    even = ""
    odd = ""

    for i in range(len(word)):
        if i % 2 == 0:
            even += word[i]
        else:
            odd += word[i]

    print(even, odd)





