#

import math


def isPalindrome():
        '''
        :type x: int
        :rtype: bool
        '''
        x = int(input())
        if(x <= 0):
            return x == 0

        log_ans = math.log10(x)
        tot_dig = math.floor(log_ans)+1
        msd_max = math.pow(10, tot_dig-1)

        for i in range(int(tot_dig)//2):

            msd = x//msd_max
            ones = x % 10

            if(msd != ones): return False

            x %= 10
            x //= msd_max

            msd_max /= 100
        return True

        

        