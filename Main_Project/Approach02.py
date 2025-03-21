import time


class ExtractsPrimeFromBinary:
    def __init__(self, binary_number):
        self.binary_number = str(binary_number)
        self.possible_binary_substrings = set()
        self.decimal_values = set()

    def extracts_unique_binary_num(self):
        """Extracts all unique substrings from the binary string."""
        length = len(self.binary_number)
        self.possible_binary_substrings = {self.binary_number[i:j] for i in range(length) for j in
                                           range(i + 1, length + 1)}

    def make_decimal(self):
        """Converts binary substrings to unique decimal values."""
        self.decimal_values = {int(binary, 2) 
        for binary in self.possible_binary_substrings}

    def is_prime(self, n):
        """Efficient prime-checking function using trial division."""
        if n < 2:
            return False
        if n in (2, 3):
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        for i in range(5, int(n ** 0.5) + 1, 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False
        return True

    def extract_primes(self, limit):
        prime_list = sorted(filter(self.is_prime, self.decimal_values))
        return prime_list[:limit]  # Apply the user-defined limit

    def print_prime_results(self, primes, limit, execution_time):
        """Displays extracted prime results with execution time."""
        print(f"\nNumber of Primes Extracted (Limit: {limit}) {len(primes)}")
        #print ("\n")
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
    #("010000110100111101001101010100000011000100111000001100010011100100100001010000010100010001010011",12)
]

# Process each binary string
for binary_string, prime_limit in binary_numbers_with_limits:
    processor = ExtractsPrimeFromBinary(binary_string)
    start_time = time.time()

    processor.extracts_unique_binary_num()
    processor.make_decimal()
    prime_numbers = processor.extract_primes(limit=prime_limit)
    execution_time = time.time() - start_time

    processor.print_prime_results(prime_numbers, prime_limit, execution_time)