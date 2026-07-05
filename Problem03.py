def find_non_multiples(start: int, end:int) -> list:
    if start > end:
        return []
    
    result = []
    for number in range(start, end+1):
        if number %3 != 0 and number %4 != 0 and number %5 != 0:
            result.append(number)

    return result
print(find_non_multiples(10, 60))