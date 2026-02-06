class Solution(object):
    def matrixReshape(self,mat,r,c):
        m=len(mat)
        n=len(mat[0]) if m>0 else 0
        if m*n!=r*c:
            return mat
        result=[]
        temp_row=[]
        for i in range(m):
            for j in range(n):
                temp_row.append(mat[i][j])
                if len(temp_row)==c:
                    result.append(temp_row)
                    temp_row=[]
        return result
mat = [[1,2],[3,4]]
r = 2
c = 4
obj=Solution()
array=obj.matrixReshape(mat,r,c)
print(array)