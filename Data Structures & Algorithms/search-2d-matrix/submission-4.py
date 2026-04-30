class Solution:

    def binarySearch(self,elements,target):
        num_row = len(elements)
        left = 0
        right = num_row-1
        while left<=right:
            
            mid = (left+right)//2
            curr=elements[mid]

            if  curr <target:
                left = mid+1
            elif curr==target:
                return True
            else:
                right = mid-1
        return False



    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        num_row = len(matrix)
        if num_row ==0:
            return False

        if  num_row ==1:
            return self.binarySearch(matrix[0],target)

        left = 0
        right = num_row-1
        mid =0
        while left<=right:
            print(left,right)
            
            
            mid = (left+right)//2
            curr  = matrix[mid][0]
            
            print(curr)
            print(target)
            print(matrix[mid][-1])
            if  curr<target and matrix[mid][-1] >= target:
                return self.binarySearch(matrix[mid],target)
            elif curr<target:
                left = mid +1
            elif curr==target:
                return True
            elif matrix[mid][-1] <= target:
                return self.binarySearch(matrix[mid],target)
            else:
                right = mid-1
            print(left,right)
        return False  
        
       

                        