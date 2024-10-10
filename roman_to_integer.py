class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        roman = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        # breakpoint()
        last = second_last = s[-1]
        print(s[-1::-1])
        for i in s[-1::-1]:
            last = second_last
            second_last = i
            
            if roman[last] > roman[second_last]:
                ans -= roman[second_last]        
            else:
                last = i
                ans += roman[last]
        return ans
    

obj = Solution()
print(obj.romanToInt('MCMXCIV'))