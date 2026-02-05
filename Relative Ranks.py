class Solution(object):
    def findRelative(self,scores):
        indexed_scores=list(enumerate(scores))#enumerate use for element with index
        indexed_scores.sort(key=lambda x:x[1],reverse=True)#key tells that which part sort and lambda small function
        result=[""]*len(scores)#result for array
        for i,(idx,score) in enumerate(indexed_scores):#i rank order, idx index and score
            if i==0:
                result[idx]="Gold Medal"
            elif i==1:
                result[idx]="Silver Medal"
            elif i==2:
                result[idx]="Bronze Medal"
            else:
                result[idx] = str(i + 1)
        return result

scores=[4,3,1,2,5]
obj=Solution()
array=obj.findRelative(scores)
print(array)


