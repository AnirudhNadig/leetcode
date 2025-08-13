from typing import List

class solution :
    def hasDuplicates(self, nums: List[int]) -> bool:
        ### we use the set() when we have these type of problems !!!

        # return len(nums) != len(set(nums))  #fastest method!! returns true or false immediately


        seen = set()

        for num in nums:

            if num in seen:
                return True
            seen.add(num)
        return False
    
def main():
    s= solution()
    print(s.hasDuplicates([1,1,3,4]))

if __name__=="__main__":
    main()