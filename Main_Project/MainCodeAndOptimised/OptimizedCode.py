import time

class ExtractsPrimeFromBinary:    # Class to extract prime numbers from binary strings
    def __init__(self, binary_number):    # Constructor to initialize binary number and decimal values
        self.binary_number = str(binary_number) #stores binary number as string
        self.decimal_values = set()             #stores decimal values as set to avoid duplicates

    def extracts_unique_decimal_num(self):         # Function that extract unique decimal values from binary number
        self.decimal_values = set()                # Initializing self.decimal_values again
        alredy_extracted_decimal_values = set()    # Initializing alredy_extracted_decimal_values to avoid duplicates                      

        for i in range(len(self.binary_number)):   # Start iteration form i to the length of binary number
            decimal_nums = 0                                # Initializing decimal_nums to 0                           
            for j in range(i, len(self.binary_number)):     # Start iteration from j to the length of binary number to extract binary substrng
                decimal_nums = decimal_nums * 2 + int(self.binary_number[j])  # Converting binarysubstring to decimal equivalent

                if decimal_nums > 1 and decimal_nums not in alredy_extracted_decimal_values:     # Checking if decimal_nums is <1(0,1 not prime) and != alredy_extracted_decimal_values
                    alredy_extracted_decimal_values.add(decimal_nums)      # Then we add that decimal_nums to alredy_extracted_decimal_values             
                    self.decimal_values.add(decimal_nums)                  # Store unique decimal nums in self.decimal_values  
                    if len(self.decimal_values) > 100000:                  # Stop at < 100000 decimal values to reduce memory usage
                        return
    
    # Method that useges Advanved Trial Division with 6k +/- 1 formula.
    # Checks divisibility only by numbers of the form 6k ± 1 an upto √n
    
    def is_prime(self, n):               # Function to check if number is prime or not
        if n < 2:                        # If number is less than 2 then it is not prime
            return False             
        if n in (2, 3):                  # If number is 2 or 3 then it is prime
            return True
        if n % 2 == 0 or n % 3 == 0:     # If number is divisible by 2 or 3 then it is not prime
            return False
        for i in range(5, min(int(n**0.5) + 1, 1000000), 6):  # using 6k +/- 1 formula to check prime numbers (Advanced Trial Division)
            if n % i == 0 or n % (i + 2) == 0:                # If number is divisible by i or i+2 then it is not prime
                return False
        return True                                           # If number is not divisible by any number then it is prime
    

    def extract_primes(self, limit=100):  # Function to extract prime numbers from decimal values
        prime_numbers = []                # Stores prime numbers
        
        for DecimalValues in sorted(self.decimal_values):                
            if self.is_prime(DecimalValues):
                prime_numbers.append(DecimalValues)    # If number is prime then add it to prime_numbers list
                if len(prime_numbers) >= limit:        # Using limit to reduce calculation time 
                    break                              # Break once reached given limit
        return prime_numbers
    

    def print_prime_results(self, primes, limit, execution_time):  # Function to print prime numbers and execution time
        print(f"\nNumber of Primes Extracted (Limit: {limit}): {len(primes)}")
        print(f"Execution Time: {execution_time:.6f} seconds")
        if not primes:
            print("No prime numbers found.")
        elif len(primes) < 6:                                       # Print prime numbers if less than 6
            print(f"Prime Numbers: {primes}")
        else:                                                       # else, print first 3 and last 3 prime numbers
            print(f"Prime Numbers: {primes[:3]} ... {primes[-3:]}") 

# Binary numbers with their specified prime extraction limit
binary_numbers_with_limits = [
    ("0100001101001111",999999 ),
    ("01000011010011110100110101010000", 999999),
    ("1111111111111111111111111111111111111111", 999999),
    ("01000011010011110100110101010000001100010011100000110001", 123456789012),
    ("010000110100111101001101010100000011000100111000001100010011100100100001010000010100010001010011",12345678901234567890)
] 
# Process each binary string
for binary_string, prime_limit in binary_numbers_with_limits:    # Loop through each binary string and process them
    processor = ExtractsPrimeFromBinary(binary_string)           # Create an instance of the ExtractsPrimeFromBinary class
    start_time = time.time() # Start execution time tracking
    
    processor.extracts_unique_decimal_num()                      # Extract unique decimal numbers
    prime_numbers = processor.extract_primes(limit=prime_limit)  # Extract prime numbers with a given limit
    execution_time = time.time() - start_time  # End execution time tracking
    
    processor.print_prime_results(prime_numbers, prime_limit, execution_time)  # Print results with execution time
