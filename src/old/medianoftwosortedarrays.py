class Solution:

    def findMedianSortedArrays(nums1,nums2):
        
        def merge(arr1,arr2):

            imax,jmax = len(arr1)-1,len(arr2)-1
            kmax = imax + jmax + 1
            i,j,k = 0,0,0
            temp = [None]*(kmax+1)
            
            if imax == -1:
                return arr2
            elif jmax == -1:
                return arr1
            
            while i <= imax and j <= jmax:
                if arr1[i] <= arr2[j]:
                    temp[k] = arr1[i]
                    i+=1
                elif arr2[j] <= arr1[i]:
                    temp[k] = arr2[j]
                    j+=1
                k+=1

            if k <= kmax:

                if i <= imax:
                    temp[k:] = arr1[i:]
                elif j <= jmax:
                    temp[k:] = arr2[j:]
            
            return temp

        def median(arr):

            arr_len = len(arr)
            middle = arr_len // 2
            
            if arr_len % 2 == 0:
                return (arr[middle] + arr[middle-1]) / 2
            return arr[middle]

        merged = merge(nums1,nums2)
        return median(merged)


test_func = getattr(Solution,'findMedianSortedArrays')

nums1 = [1,3]
nums2 = [2]

print(nums1)
print(nums2)
print(test_func(nums1,nums2))