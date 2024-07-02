def fibonacci(n):
    fibonacci_series = [0, 1]
    while len(fibonacci_series) < n:
        new_entry=fibonacci_series[-1] + fibonacci_series[-2]
        fibonacci_series.append(new_entry)
    return fibonacci_series[:n]
