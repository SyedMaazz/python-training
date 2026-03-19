class Solution:
    def asteroidCollision(self, a: List[int]) -> List[int]:
        n = len(a)
        for i in range(n):
            if a[i]<0:
                j = i-1
                while j>=0 and a[j]>0:
                    if a[j] < -1*a[i]:
                        a[j] = 0
                        j-=1
                    elif a[j] == -1*a[i]:
                        a[j] = 0
                        a[i] = 0
                        break
                    else:
                        a[i] = 0
                        break
        ans = []
        for i in range(n):
            if a[i]!=0: ans.append(a[i])
        return ans