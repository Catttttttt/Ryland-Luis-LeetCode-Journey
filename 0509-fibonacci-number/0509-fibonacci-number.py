class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        # iteration
        if n == 0:
            return 0
        df = [0] * 2
        df[0] = 0
        df[1] = 1
        for i in range(2, n + 1):
            df[i%2] = df[0] + df[1]
        return df[n%2]
        
        
        ''' recursion
        def helper(n):
            if n == 0:
                return 0
            elif n == 1:
                return 1
            else:
                return helper(n - 1) + helper(n - 2)
        return helper(n)
        '''