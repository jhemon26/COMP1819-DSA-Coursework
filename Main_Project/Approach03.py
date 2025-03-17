import time

class ExtractsPrimeFromBinary:             # Class to extract prime numbers from binary numbers
    def __init__(self, binary_number):     # Initializer
        self.binary_number = str(binary_number)  # Sotres Bin num as string
        self.decimal_values = set()             # Stores Dec val as set to avoid duplicates

    def extracts_unique_binary_num(self):   # Method which converts binary string > sub
            
        self.decimal_values = set()         # ReInitializing self.decimal_values
        Unique_decimal_values = set()       # An Approach to avoid duplicates and reduce redundancy
        for i in range((len(self.binary_number))):   
            Extracted_decimal = 0           # A variable that stores the extracted decimal value
            for j in range(i, (len(self.binary_number))):  # Extracting binary substrings
                Extracted_decimal= (Extracted_decimal<< 1) | int(self.binary_number[j]) # use bitwise op. to convert Bin to Dec
                if Extracted_decimal > 1 and Extracted_decimal not in Unique_decimal_values:  # Condition to avoid redundancy
                    Unique_decimal_values.add(Extracted_decimal)
                    self.decimal_values.add(Extracted_decimal)
                    if len(self.decimal_values) > 100000:  # Safety limit to avoid huge memory use and time complexity
                        return
    
    def is_prime(self,n):        # Method to check if a number is prime or not
        if n < 2:                # it n less than 2 return False
            return False
        if n == 2 or n == 3:     # if n is 2 or 3 return True cause they are prime 
            return True
        if n % 2 == 0 or n % 3 == 0:  # if n is divisible by 2 or 3 return False
            return False
        for i in range(5, int(n ** 0.5) + 1, 2):  # trial Division formula
            if n % i == 0:                        # if n is divisible by i return False
                return False
        return True


    def extract_primes(self, limit=100):
        
        prime_numbers = []                          # A list to store prime numbers
        for num in sorted(self.decimal_values):     # Loop through sorted decimal values
            if self.is_prime(num):                  # appply is_prime on the (num)
                prime_numbers.append(num)
                if len(prime_numbers) >= limit:     # Break if limit is reached
                    break  
        return prime_numbers

    def print_prime_results(self, primes, limit, execution_time):   # Method to print prime numbers and execution time
        
        print(f"\nNumber of Primes Extracted {len(primes)}")
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
    ("010000110100111101001101010100000011000100111000001100010011100100100001010000010100010001010011",12345678901234567890)
]
# Process each binary string
for binary_string, prime_limit in binary_numbers_with_limits:
    processor = ExtractsPrimeFromBinary(binary_string)
    start_time = time.time()
    
    processor.extracts_unique_binary_num()
    prime_numbers = processor.extract_primes(limit=prime_limit)
    execution_time = time.time() - start_time
    
    processor.print_prime_results(prime_numbers, prime_limit, execution_time) # Print results with execution time
