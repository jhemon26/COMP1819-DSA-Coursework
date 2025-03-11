import time

class ExtractsPrimeFromBinary:
    def __init__(self, binary_number):  # initializing the method
        self.binary_number = str(binary_number)  # takes input as string
        self.possible_binary_substrings = set()  # stores all possible binary substrings
        self.decimal_values = set()  # stores decimal values


    def extracts_unique_binary_num(self):  # method that extracts unique substrings from the string
        for i in range(len(self.binary_number)):  # iterate from start index i
            for j in range(i + 1, len(self.binary_number) + 1):  # iterate from i+1 to len+1
                self.possible_binary_substrings.add(self.binary_number[i:j])  # extract substrings
        return sorted(self.possible_binary_substrings)  # return sorted binary substrings

    def make_decimal(self):  # method for extracting decimal values
        self.decimal_values = set()  # initialize decimal_values as a set
        for binary_string in self.possible_binary_substrings:  # looping through binary strings
            decimal_value = int(binary_string, 2)  # convert to decimal
            self.decimal_values.add(decimal_value)  # add to decimal_values set
        return sorted(self.decimal_values)

    def is_prime(self, n):  # prime-checking method
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):  # check divisibility up to √n
            if n % i == 0:
                return False
        return True  # return True if prime

    def extract_primes(self, limit=100):  # method for extracting prime numbers
        """
        Extracts prime numbers from the decimal values with a limit on how many primes to extract.
        :param limit: (int) Number of prime numbers to extract.
        :return: Sorted list of prime numbers up to the given limit.
        """
        prime_list = sorted([num for num in self.decimal_values if self.is_prime(num)])
        return prime_list[:limit]  # Return only the specified number of primes

    def print_prime_results(self, primes, limit, execution_time):
        """
        Prints the first 5 primes if the extracted prime count is below 6.
        Otherwise, prints the first 3 and last 3 primes.
        :param primes: List of extracted prime numbers.
        :param limit: Number of primes requested.
        """
        print(f"\nNumber of Primes Extracted (Limit: {limit}): {len(primes)}")
        print(f"Execution Time: {execution_time:.6f} seconds")

        if len(primes) == 0:
            print("No prime numbers found.")
        elif len(primes) < 6:
            print(f"Prime Numbers: {primes[:5]}")
        else:
            print(f"Prime Numbers: {primes[:3]} ... {primes[-3:]}")


# Define multiple binary numbers with their respective prime extraction limits
binary_numbers_with_limits = [
    #("0100001101001111",999999 ),
    ("01000011010011110100110101010000", 999999),
    ("1111111111111111111111111111111111111111", 999999),
    ("01000011010011110100110101010000001100010011100000110001", 123456789012),
    #("101011", 99)
    #("010000110100111101001101010100000011000100111000001100010011100100100001010000010100010001010011",12)
]

# Loop through each binary string and process them
for num, prime_limit in binary_numbers_with_limits:
    apply_num_to_class = ExtractsPrimeFromBinary(num)
    start_time = time.time()  # Start execution time tracking
    apply_num_to_class.extracts_unique_binary_num()
    apply_num_to_class.make_decimal()

    # Extract primes with a given limit
    prime_numbers = apply_num_to_class.extract_primes(limit=prime_limit)
    execution_time = time.time() - start_time  # End execution time tracking

    # Print results with execution time
    apply_num_to_class.print_prime_results(prime_numbers, prime_limit, execution_time)
