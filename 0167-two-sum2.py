from typing import List

class Solution:
    def twosum(self,numbers:List[int], target:int) -> List[int]:

        i, j = 0, len(numbers)-1

        while i<j:
            su = numbers[i] + numbers[j]
            if su < target:
                i+=1
            elif su> target:
                j-=1
            else:
                return [i+1,j+1] #class one indexing
        return [-1,-1] #default
    
            