def solution(triangle):
    triangle[1][0] += triangle[0][0]
    triangle[1][1] += triangle[0][0]
    
    for i in range(2,len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
                
            elif j == len(triangle[i]) - 1:
                triangle[i][j] += triangle[i-1][-1]
                
            else:
                if triangle[i-1][j-1] < triangle[i-1][j]:
                    triangle[i][j] += triangle[i-1][j]
                else:
                    triangle[i][j] += triangle[i-1][j-1]
    
    return max(triangle[-1])