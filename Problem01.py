def find_multiples_of_three(start: int, end: int) -> list:
    if start > end:
        return []
    result = []
    for number in range(start, end+1):
        if number %3 == 0:
            result.append(number)
    return result

print(find_multiples_of_three(10, 36))