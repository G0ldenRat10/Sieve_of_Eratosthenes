import math
program_active = True
print("Have fun!")

def __main__():
    """ Main function of the program. """
    user_number = int(input("\nEnter a number: "))
    # Logic: assume all numbers could potentially be prime:
    # Step 1: insert boolean True into the list so the result is a list ready for indexing
    # Example: user_number = 5 --> potential_primes = [True, True, True, True, True, True]
    potential_primes = [True] * (user_number + 1)
    # Step 2: mark obvious non-primes
    potential_primes[0] = False
    potential_primes[1] = False
    # Step 3: form lists of prime and composite numbers
    prime_numbers = sieve_of_eratosthenes(user_number, potential_primes)
    # Result:
    print(f"Prime numbers less than {user_number}: {make_list(user_number, prime_numbers, list_type='prime')}")
    print(f"Composite numbers less than {user_number}: {make_list(user_number, prime_numbers, list_type='composite')}")
    
    
def sieve_of_eratosthenes(user_number, potential_primes):
    """ Calculation of prime and composite numbers """
    # The logic: for each number to be checked,
    # it is enough to check all numbers less than or equal to the square root of the number
    # to determine whether it is prime or not.
    
    for n in range(2, int(math.sqrt(user_number)) + 1):  
        # Could also use: int(user_number ** 0.5) + 1, but using math.sqrt for clarity
        if potential_primes[n]:
            for composite_number in range(n*n, user_number + 1, n):    
                # All numbers less than n*n are already multiples
                potential_primes[composite_number] = False   
                # Mark numbers we have concluded are not prime but composite
    # Final list contains True and False in the correct positions
    primes_list = potential_primes
    return primes_list

def make_list(user_number, primes_list, list_type):
    # Create empty lists
    prime_numbers_list = []
    composite_numbers_list = []
    # Check the list with True/False values and separate into new lists
    for n in range(2, user_number):
        if primes_list[n] == True:
            prime_numbers_list.append(n)
        if primes_list[n] == False:
            composite_numbers_list.append(n)
    # Depending on the argument list_type, return the requested list
    if list_type == 'prime':
        return prime_numbers_list
    elif list_type == 'composite':
        return composite_numbers_list
    else:
        print("ERROR: Invalid argument for list_type=")

while program_active == True:
    __main__()
