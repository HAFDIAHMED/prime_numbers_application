# prime number generation

Here is a screencast of the prime.py in action:

![prime.py](https://raw.githubusercontent.com/jrhea/prime-numbers/master/images/prime_loops.gif)


**proof of algorithm's optimizations:**

All integers can be written in the form:

            6k+i where i = 0,1,2,3,4,5
    
_Note: We can show that 5 could be replaced by -1 by substituting k' with k+1_

            6k'-1 = 6k+5 when k'=k+1

All odd integers can be written in the form:

            6k+i where i = 1,3,5

_Note: We can remove 3 from i bc 6k+3 only generates a single prime (3) when k=0_

6k+3 is composite for all other values of k:

           6k % 3 = 0 -> (6k+3) % 3 = 0

Therefore, set containing all odd primes greater than 3 can be written as:

            6k+i where i = 1,5  

**Now I have proven that I can speed up the prime test by:**
* incrementing i by 6 each pass of the loop 
* only checking if n mod i or n mod i+2 equals 0

_Note: i is equivalent to 6k+5 & i+2 is equivalent to 6k+1_
