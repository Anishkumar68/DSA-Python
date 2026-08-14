class solution:

    def intToroman(self, num):

        # rules are for the int to roman 
        rules = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
            ]

        # empty str to store end results 
        result = "" 
        # value = 1000,500,100,50 etc 
        # symbol  =  m,cm,x,d,cd  etc 
        for value, symbol in rules:
            while num >= value:
                num -=value
                result += symbol

        return result

a = solution()
print(a.intToroman(int(input("enter a number: "))))

