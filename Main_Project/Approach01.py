

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
    def __init__(self, binarynumber):
        self.binarynumber = binarynumber
        self.possible_binary_substrings = ()
        self.decimal_values = []
        self.list_of_primes = []
        
    def extracts_enique_binary_num (self):
        given_binary_string = str(self)
        substrings = set()
        
        for i in range (len(given_binary_string)):
            for j in range (i + 1, (len(given_binary_string)) +1 ):
                substrings.add(given_binary_string [i : j])
                
        return sorted(substrings)
    
    
num = 10101
result = Extracts_prime_from_binary.extracts_enique_binary_num(num)
print(result)
    
    
            

