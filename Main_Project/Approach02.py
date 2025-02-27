class Extracts_prime_from_binary:
    def __init__(self, binarynumber):                 #initializing the method
        self.binarynumber = str(binarynumber)         #takes input as strings
        self.possible_binary_substrings = set()     #stores all the possible binary substrings
        self.decimal_values = set()
        self.list_of_primes = set()
        
    def extracts_enique_binary_num (self):            #method that extracts unique substrings from the string
        
        for i in range (len(self.binarynumber )):     #cheks the len of the strings with starting index "i"
            for j in range (i + 1, (len(self.binarynumber )) +1 ):    #checks the ending with j = from i+1 to len +1
                self.possible_binary_substrings.add(self.binarynumber  [i : j])  #extracts the substrings
                
        return sorted(self.possible_binary_substrings)          #returns sorted binary substrings
    
    
    
    def make_decimal (self):                             #method for extracting decimal vlaues
        self.decimal_values = set ()                      #initializing decimal_values as a set
        for binary_strings in self.possible_binary_substrings:      #loopint through the binary SStrings 
            decimal_value = int(binary_strings , 2)          #using built in func to get decimal vlaues
            self.decimal_values.add(decimal_value)           #adding the values to the decimal_vlaues list
        
        return sorted(self.decimal_values)



    def is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, n + 1):  # Loop runs up to `n`
            if n % i == 0 and i != n:  # Ensure we ignore `n` itself
                return False
        return True


    
    
num = 10000110100111101001101010100000011000100111000001100010011100100100001010000010100010001010011

apply_num_to_class = Extracts_prime_from_binary(num)
apply_num_to_class.extracts_enique_binary_num()
print_decimal_values = apply_num_to_class.make_decimal()

print("\n") 
print(print_decimal_values) 