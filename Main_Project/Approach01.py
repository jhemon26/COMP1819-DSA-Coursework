

# Assume if we have an intiger value "0110"

# Need to create a fucntion that will convert the intiger value to a extent where 
# it can be 0, 01, 011, 0110,10, 11, 110, 1010 
# we then save the values in a list 
# then we have another list that will holds the decimal value of the all integers
# Need a function that will check for any prime numbers from the converted decimal values
# we would another list that holds the returned values of the prime numbres 


                                    #"Approach"#
                                    


# A fucntion that extracts all the possible unique values from the given int values
# A function that will convert the unique values to it's decimal form
# A funciton that will apply on the decimal value list and check for any prime numbers and save it in a lst




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
        for i in range(2, int(n**0.5) + 1):  # Check only up to √n
            if n % i == 0:
                return False
        return True

    
    
num = 10000110100111101001101010100000011000100111000001100010011100100100001010000010100010001010011

apply_num_to_class = Extracts_prime_from_binary(num)
apply_num_to_class.extracts_enique_binary_num()
print_decimal_values = apply_num_to_class.make_decimal()

print("\n") 
print(print_decimal_values)  
    
            

