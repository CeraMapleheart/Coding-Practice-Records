class Solution:
    def convertDateToBinary(self, date: str) -> str:
        parts = date.split("-")
        result = [bin(int(part))[2:] for part in parts]
        return "-".join(result)


        
        
        