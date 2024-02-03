def fibonacci(n):
    sequence = []
    a, b = 0, 1

    while len(sequence) < n:
        sequence.append(a)
        a, b = b, a + b

    return sequence


if __name__ == '__main__':
    count = int(input("Enter the number of Fibonacci numbers you want: "))
    fib_sequence = fibonacci(count)
    print(f"Fibonacci sequence of length {count}: {fib_sequence}")
    