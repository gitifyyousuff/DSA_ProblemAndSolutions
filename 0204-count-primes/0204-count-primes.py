class Solution:
    def countPrimes(self, n: int) -> int:
        #Sieve of Eratosthenes Theorem
        #TC : O(nlog(log(n))), SC : O(1), where 1 is n given
        #Edge case 
        if n<=2:
            return 0
        
        #Making every as True for n length
        #Marking 0 and 1 as False since non-prime
        isPrime = [True] * n
        isPrime[0] = isPrime[1] = False
        limit = int(math.sqrt(n))
        
        #start from 2 to limit, where limit is sqareroot of given n
        for i in range(2,limit+1):
            #if it is prime, then start marking False from the square of curr num
            #till n with the step of curr num
            if isPrime[i] == True:
                for j in range(i*i,n,i):
                    isPrime[j] = False
                    
        #after the above steps, prime numbers will be marked as True 
        #and non-prime numbers will be marked as False
        count = 0
        for i in range(2,n):
            if isPrime[i] == True:
                count += 1
                
        return count
        
                    
                    
                    
        