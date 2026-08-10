# DSA-Python


class solution:
    def __int__(self):
        pass

    def romantoint(self, s: str) -> int:
        """
        type s: str
        """

        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        res = 0
        for i in range(len(s)):  # index (0,1,2,3,4)
            # index + 1 = 5 if less than len of s eg.v == 1
            # roman[1[1]] < roman[1[1+1]] => roman[1] < roman [2]
            # then, --i => 0-1
            # else : 0 + 1 +++
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
                res -= roman[s[i]]
            else:
                res += roman[s[i]]

        return res


takeinput = input("Enter number roman to int:")
s = solution()
print(s.romantoint(takeinput))
