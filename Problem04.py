def calculate_sum_and_average() -> None:
    numbers = []
    for i in range(5):
        number = float(input(f"Enter number {i+1}:"))
        numbers.append(number)

    total = sum(numbers)
    average = total / 5
    
    print(f"Sum: {total:.2f}")
    print(f"Average: {average:.2f}")

calculate_sum_and_average()

