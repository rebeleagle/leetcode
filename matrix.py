class Solution:
    def spiralOrder(self, matrix): 
        def getNextEl(c, i, j):
            if c == 0:
                if j+1 == n or visited[i][j+1] == True:
                    if i+1==m or visited[i+1][j] == True: return(c, -1,-1)
                    c = (c+1)%4
                    return (c, i+1, j)
                else:
                    return (c, i, j+1)
            elif c == 1:
                if i+1 == m or visited[i+1][j] == True: 
                    if j==0 or visited[i][j-1] == True: return(c, -1,-1)
                    c = (c+1)%4
                    return (c, i, j-1)
                else:
                    return (c, i+1, j)
            elif c == 2:
                if j == 0 or visited[i][j-1] == True:
                    if i==0 or visited[i-1][j] == True: return(c,-1,-1)
                    c = (c+1)%4
                    return (c, i-1, j)
                else:
                    return (c, i, j-1)
            elif c == 3:
                if i == 0 or visited[i-1][j] == True:
                    if j==n or visited[i][j+1] == True: return(c,-1,-1)
                    c = (c+1)%4
                    return (c, i, j+1)
                else:
                    return (c, i-1, j)
                
        m = len(matrix)
        if m == 0: return []
        
        n = len(matrix[0])
        if n == 0: return []
        
        visited = []
        for i in range(m):
            visited.append([False]*n)
        
        c = 0    
        i = 0
        j = 0
        ans = []
        while i>=0 and j>=0:
            ans.append(matrix[i][j])
            visited[i][j] = True
            c,i,j = getNextEl(c,i,j)
            
        return ans
