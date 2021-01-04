#!/usr/bin/python
#Goal
#1) Write a function to test primes using as many tricks as I can derive
#2) Add caching to the algorithm
#3) Write test script that times the algorithm and compares answers to known results on the web

'''Informal Proof:
      All integers can be written in the form:
            6k+i where i = 0,1,2,3,4,5
      Note: 5 could be replaced by -1 bc: 
            6k'-1 = 6k+5 when k'=k+1
      All odd integers can be written in the form:
            6k+i where i = 1,3,5
      We remove 3 from i bc 6k+3 only generates a single prime (3) when k=0.
      6k+3 is composite for all other values of k:
            6k % 3 = 0 => (6k+3) % 3 = 0
      Therefore, set containing all odd primes greater than 3 can be written as:
            6k+i where i = 1,5      
'''  


import math
import time
import urllib2
import unittest

class Prime:

  def __init__(self):
    self.__cache = dict()
    
  def testPrimeWithCache(self, n): 
    if(n in self.__cache):
      return self.__cache[n]
    self.__cache[n] = self.testPrime(n)
    return self.__cache[n]          
  
  def testPrime(self, n):

    if n < 2:
      #anything less than 2 can't be prime
      return False
    elif n <= 3:
      #2,3 are prime
      return True
    elif n % 2 == 0 or n % 3 == 0:
      #any multiple of 2,3 is not prime
      #eliminates all natural numbers < 25
      return False

    #Let i = 6k+5 where k=0
    i=5
    #Since all divisors <= 5 have been coded for above. 
    while i*i <= n:
      #n mod 6k+5 == 0 or n mod 6k+1 == 0
      if n % i==0 or n % (i+2)==0: 
        return False
      #increment k in search of the next composite: 6(k+1)+1
      i += 6
    
    return True

  #prime number generator based on the Sieve of Eratosthenes
  def primeSieve(self, num):
    nums = range(2,num+1)
    outer = range(2,int(math.ceil(math.sqrt(num))))
    for i in outer:
      nums = filter(lambda x: (x == i or x % i), nums)
    
    return nums 

class TestPrimes(unittest.TestCase):
  
  #Test the basic prime number alg
  def test_first_1000_primes(self):
    p=Prime()
    knownPrimes = []
    page = urllib2.urlopen('http://primes.utm.edu/lists/small/1000.txt')
    for line in page:
      try:
        knownPrimes += map(int,line.split())  
      except Exception:
        #gulp
        pass
   
    print 'Downloaded the first ', len(knownPrimes), ' primes'
    print 'calculating first 1000 primes' 
    nums = range(2,knownPrimes[999]+1)
    calcdPrimes = []
    start = time.clock()
  
    for i in nums:
      if(p.testPrime(i)):calcdPrimes += [i]
  
    end = time.clock()
    print "elapsed time: ", end-start
    self.assertEqual(knownPrimes,calcdPrimes)

  #Test the caching    
  def test_first_1000_primes_with_cache(self):
    p=Prime()
    knownPrimes = []
    page = urllib2.urlopen('http://primes.utm.edu/lists/small/1000.txt')
    for line in page:
      try:
        knownPrimes += map(int,line.split())  
      except Exception:
        #gulp
        pass
   
    print 'Downloaded the first ', len(knownPrimes), ' primes'
    print 'calculating first 1000 primes'
    nums = range(2,knownPrimes[999]+1)
    calcdPrimes = []
    start = time.clock()
  
    for i in nums:
      if(p.testPrimeWithCache(i)):calcdPrimes += [i]
  
    end = time.clock()
    print "elapsed time: ", end-start
    print 'calculating first 1000 primes and using cache'
    nums2 = range(2,knownPrimes[999]+1)
    calcdPrimes2 = []
    start = time.clock()
  
    for i in nums2:
      if(p.testPrimeWithCache(i)):calcdPrimes2 += [i]
  
    end = time.clock()
    print "elapsed time: ", end-start
    self.assertEqual(knownPrimes,calcdPrimes2)


def main():
  p=Prime()
  while True:
    
    print "\nOptions:"
    print "1) Determine if a number is prime"
    print "2) Generate all primes up to (and including) a given number"
    print "3) Run unit tests"
    print "4) Quit"
    selection = input("Please make a selection: ")

    if selection == 1:
      num = input("Enter a number: ")
      start = time.clock()
      isPrime = p.testPrimeWithCache(num)
      end = time.clock()
      if isPrime: print num, "\nis a prime number."
      else: print num, "\nis not a prime number."
      print "elapsed time: ", end-start
      print "\n"

    elif selection == 2:
      num = input("Enter a number: ")
      primes = []
      print "Running testPrimeWithCache"
      start = time.clock()
      nums = range(2,num+1)
      for i in nums:
        if(p.testPrimeWithCache(i)):primes += [i]

      end = time.clock()
      elapsed1 = end-start
      print "Found ",len(primes), " primes."
      primes = []
      print "Running testPrime"
      start = time.clock()
      nums = range(2,num+1)
      for i in nums:
        if(p.testPrime(i)):primes += [i]

      end = time.clock()
      elapsed = end-start
      print "Found ",len(primes), " primes."
      primes = []
      #print "\n"
      #print primes
      #print "\n"
      print("Running primeSieve")
      start = time.clock()
      primes = p.primeSieve(num)
      end = time.clock()
      elapsed2=end-start
      print "Found ",len(primes), " primes."
      print "testPrimeWithCache elapsed time: ", elapsed1
      print "testPrime elapsed time: ", elapsed
      print "primeSieve elapsed time: ", elapsed2
      
    elif selection ==3:
      suite = unittest.TestLoader().loadTestsFromTestCase(TestPrimes)
      unittest.TextTestRunner(verbosity=2).run(suite)
      print "\n"
    else:
      print "Goobye"
      break;
  


main()