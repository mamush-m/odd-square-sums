def oddSquareSum(n):
    total = 0
    for i in range(n):
        curr_prime = i**2
        if curr_prime < n and curr_prime % 2 != 0:
            total += curr_prime
    return total


# TEST CASES 👇

oddSquareSum(1) # returns 0

oddSquareSum(2) # returns 1

oddSquareSum(9) # returns 1

oddSquareSum(10) # returns 10

oddSquareSum(44) # returns 35

oddSquareSum(50) # returns 84