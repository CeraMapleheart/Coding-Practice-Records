class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        ones_m = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen"}
        tens_m = {20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety"}
        """
        hundreds = nums%1000
        thousands = (nums % 1000000) // 1000
        millions = (nums % 1000000000) // 1000000
        billions = nums % 1000000000
        """
    
        def get_string(n):
            res = []
            hundreds = n // 100
            if hundreds:
                res.append(ones_m[hundreds]+" Hundred")
            last = n % 100
            if last >= 20:
                tens, ones = last // 10, last % 10
                res.append(tens_m[tens * 10])
                if ones:
                    res.append(ones_m[ones])
            elif last:
                res.append(ones_m[last])
            return " ".join(res)

        i = 0
        word = ["", " Thousand", " Million", " Billion"]
        res = []

        while num:
            digits = num % 1000
            s = get_string(digits)
            if s: 
                res.append(s + word[i])
            num = num //1000
            i += 1
        res.reverse()
        return " ".join(res)
