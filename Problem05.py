def find_divirors(n: int) -> list:
    if n <= 0:
        return []
    divisors = []
    for number in range(1, n+1):
        if n %number == 0:
            divisors.append(number)

    return divisors

print(find_divirors(35))