
n = int(input().strip())
phone_book = {}

for _ in range(n):
    entry = input().split()
    name = entry[0]
    phone = entry[1]

    phone_book[name] = phone

while True:
    try:
        query = input().strip()
        if not query:
            break

        if query in phone_book:
            print(f"{query}={phone_book[query]}")
        else:
            print("Not found")
    except EOFError:
        break
