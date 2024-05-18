#2 Задание
import time
from multiprocessing import Pool, cpu_count

def find_factors(n):
    factors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:
                factors.append(n // i)
    factors.sort()
    return factors

def factorize(*numbers):
    results = []
    for number in numbers:
        results.append(find_factors(number))
    return results

def parallel_factorize(*numbers):
    with Pool(cpu_count()) as pool:
        results = pool.map(find_factors, numbers)
    return results

# Тестовые числа
numbers = (128, 255, 99999, 10651060)

# Синхронное выполнение
start_time = time.time()
results_sync = factorize(*numbers)
print("Synchronous execution time: {:.2f} seconds".format(time.time() - start_time))

# Асинхронное выполнение
start_time = time.time()
results_parallel = parallel_factorize(*numbers)
print("Parallel execution time: {:.2f} seconds".format(time.time() - start_time))

# Проверка результатов
assert results_sync == [
    [1, 2, 4, 8, 16, 32, 64, 128],
    [1, 3, 5, 15, 17, 51, 85, 255],
    [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999],
    [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
]
assert results_sync == results_parallel

print("All tests passed!")
