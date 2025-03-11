import time

class ExtractsPrimeFromBinary:
    def __init__(self, binary_number):
        self.binary_number = str(binary_number)
        self.decimal_values = set()

    def extracts_unique_binary_num(self):
        """Extracts unique decimal values from binary substrings efficiently."""
        length = len(self.binary_number)
        self.decimal_values = set()
        seen = set()
        for i in range(length):
            num = 0
            for j in range(i, length):
                num = (num << 1) | int(self.binary_number[j])
                if num > 1 and num not in seen:
                    seen.add(num)
                    self.decimal_values.add(num)
                    if len(self.decimal_values) > 100000:  # Safety limit to avoid excessive computation
                        return
    
    def is_prime(self, n):
        """Optimized prime-checking function without memory-heavy lists."""
        if n < 2:
            return False
        if n in (2, 3):
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        for i in range(5, min(int(n**0.5) + 1, 1000000), 6):  # Avoid excessive iteration
            if n % i == 0 or n % (i + 2) == 0:
                return False
        return True

    def extract_primes(self, limit=100):
        """Extracts up to 'limit' prime numbers from decimal values."""
        prime_numbers = []
        for num in sorted(self.decimal_values):
            if self.is_prime(num):
                prime_numbers.append(num)
                if len(prime_numbers) >= limit:
                    break  # Stop early once we reach the required limit
        return prime_numbers

    def print_prime_results(self, primes, limit, execution_time):
        """Displays extracted prime results with execution time."""
        print(f"\nNumber of Primes Extracted (Limit: {limit}): {len(primes)}")
        print(f"Execution Time: {execution_time:.6f} seconds")
        if not primes:
            print("No prime numbers found.")
        elif len(primes) < 6:
            print(f"Prime Numbers: {primes}")
        else:
            print(f"Prime Numbers: {primes[:3]} ... {primes[-3:]}")

# Define binary numbers and their prime extraction limits
binary_numbers_with_limits = [
    ("0100001101001111",999999 ),
    ("01000011010011110100110101010000", 999999),
    ("1111111111111111111111111111111111111111", 999999),
    ("01000011010011110100110101010000001100010011100000110001", 123456789012),
    #("010000110100111101001101010100000011000100111000001100010011100100100001010000010100010001010011",12345678901234567890)
]
# Process each binary string
for binary_string, prime_limit in binary_numbers_with_limits:
    processor = ExtractsPrimeFromBinary(binary_string)
    start_time = time.time()
    
    processor.extracts_unique_binary_num()
    prime_numbers = processor.extract_primes(limit=prime_limit)
    execution_time = time.time() - start_time
    
    processor.print_prime_results(prime_numbers, prime_limit, execution_time)
