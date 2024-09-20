upper_bound = int(input("Enter an upper bound for a check: "))

deficient_count = 0
perfect_count = 0
abundant_count = 0

for number in range(1, upper_bound + 1):
    divisors_sum = 0
    for x in range(1, number):
        if number % x == 0:
            divisors_sum += x

    if divisors_sum < number:
        deficient_count += 1
    elif divisors_sum == number:
        perfect_count += 1
    else:
        abundant_count += 1

print("Between 1 and upper_bound there are:")
print(f"Deficient numbers: {deficient_count}")
print(f"Perfect numbers: {perfect_count}")
print(f"Abundant numbers: {abundant_count}")