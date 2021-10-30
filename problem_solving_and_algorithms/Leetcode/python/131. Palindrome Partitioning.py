class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        
        ret = []
        def isPal(s):
            return s == s[ : : -1]

        def fn(s, l):
            if not s:
                ret.append(l)
                return
            for i in range(1, len(s) + 1):
                if isPal(s[ : i]):
                    fn(s[i : ], l + [s[ : i]])
        fn(s, [])
        
        return ret
    
    
