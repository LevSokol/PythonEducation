numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(len(numbers)):
    for j in range(len(numbers)):
        print(f"{numbers[i]} * {numbers[j]} == {numbers[i] * numbers[j]}")
    print()
