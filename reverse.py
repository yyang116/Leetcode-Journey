class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if x>=0:
            rev= int(str(x)[::-1])
            return rev if rev<=INT_MAX else 0
        else:
            rev = int(str(x)[:0:-1])*(-1)
            return rev if rev>=INT_MIN else 0
