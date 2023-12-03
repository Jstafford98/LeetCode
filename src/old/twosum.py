class Solution:

    def twoSum(self,nums: list[int], target: int) -> list[int]:

        '''
        BRUTE FORCE:
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                print(f'Comparing {nums[i]} + {nums[j]}')
                if nums[i] + nums[j] == target:
                    return [i,j]
        '''

        '''
            DICT ANSWER

            Works by storing values in a sumDict. We insert the compliment (the number that would add up to our target) into a dict and store the index
            that should be returned with that compliment. The key is our current number and the value is the index of it's compliment. 

            If the current number has been identified as a compliment in the sumMap, return it's index and i
            If not, add the compliment (target-curr number) to the map.
        '''
        sumMap = dict()
        for i in range(len(nums)):
            currNum = nums[i]
            print(currNum)
            print(sumMap)
            if currNum in sumMap:
                return [sumMap[currNum],i]
            else:
                sumMap[target - currNum] = i
        return []

test = Solution()

nums = [2,7,11,15] 
target = 9
print(test.twoSum(nums,target))