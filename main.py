from fibonacci import fibonacci

def main():
    n = int(input("Enter the limit\n"))
    fib_series = fibonacci(n)
    print(f"Fibonacci series up to {n}th term:", fib_series)

if __name__ == "__main__":
    main()
