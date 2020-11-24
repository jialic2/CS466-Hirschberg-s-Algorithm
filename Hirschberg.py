
def linearspacescore(s1, s2):
    len1 = len(s1)
    len2 = len(s2)
    dp = [[0 for j in range(len1 + 1)] for i in range(2)]
    curridx = 0
    for i in range(len2 + 1):
        for j in range(len1 + 1):
            if i==0 and j==0:
                dp[curridx][j]=0
            elif i>0 and j==0:
                dp[curridx][j]=dp[1-curridx][j]-1
            elif i==0 and j>0:
                dp[curridx][j]=dp[curridx][j-1]-1
            else:
                score = 0 if s1[j-1] == s2[i-1] else -1
                dp[curridx][j] = max(dp[1-curridx][j]-1,max(dp[curridx][j-1]-1,dp[1-curridx][j-1]+score))
        curridx = 1-curridx
    return (dp[1-curridx])

def originalres(s1,s2):
    len1 = len(s1)
    len2 = len(s2)
    dp = [[0 for j in range(len1 + 1)] for i in range(len2 + 1)]
    for i in range(len2 + 1):
        for j in range(len1 + 1):
            if i==0 and j==0:
                dp[i][j]=0
            elif i>0 and j==0:
                dp[i][j]=dp[i-1][j]-1
            elif i==0 and j>0:
                dp[i][j]=dp[i][j-1]-1
            else:
                score = 0 if s1[j-1]==s2[i-1] else -1
                dp[i][j] = max(dp[i-1][j]-1,max(dp[i][j-1]-1,dp[i-1][j-1]+score))
    return dp[len2]

def hirschbergrecur(s1,s2,i,j,ip,jp,res):
    print("hirschbergrecur(",s1,",",s2,",",s1[i:ip:],",",s2[j:jp],",",i,j,ip,jp,")")
    # i,j,ip,jp are all inclusive i.e. s1[i.....ip) and s2[j.....jp) and 1-indexed
    if jp-j==1:
        for idx in range(i,ip):
            res.append((idx,j))
        return
    if ip-i==1:
        for idx in range(j,jp):
            res.append((i,idx))
        return
    mid = int((j+jp)/2)
    prefix = linearspacescore(s1[i:ip:],s2[j:mid:])
    suffix = linearspacescore(s1[i:ip:][::-1],s2[mid:jp:][::-1])
    assert prefix == originalres(s1[i:ip:],s2[j:mid:])
    assert suffix == originalres(s1[i:ip:][::-1],s2[mid:jp:][::-1])
    assert len(prefix) == len(suffix)
    maxidx = -1
    maxweight = -1
    for idx in range(len(prefix)):
        weight = prefix[idx] + suffix[-idx-1]
        print("idx=",idx,"weight=",weight,end=" ")
        if maxidx == -1 or maxweight <= weight:
            maxidx = idx
            maxweight = weight
    res.append((maxidx+i, mid))
    print("\nappend (",maxidx+i,mid,")")
    hirschbergrecur(s1,s2,i,j,maxidx+i,mid,res)
    hirschbergrecur(s1,s2,maxidx+i,mid,ip,jp,res)

def hirschberg(s1,s2):
    res = []
    len1 = len(s1)
    len2 = len(s2)
    hirschbergrecur(s1,s2,0,0,len1,len2,res)
    res.sort(key=lambda x: (x[0],x[1]))
    print(res)

def originalscore(s1,s2):
    len1 = len(s1)
    len2 = len(s2)
    dp = [[0 for j in range(len1 + 1)] for i in range(len2 + 1)]
    for i in range(len2 + 1):
        for j in range(len1 + 1):
            if i==0 and j==0:
                dp[i][j]=0
            elif i>0 and j==0:
                dp[i][j]=dp[i-1][j]-1
            elif i==0 and j>0:
                dp[i][j]=dp[i][j-1]-1
            else:
                score = 0 if s1[j-1]==s2[i-1] else -1
                dp[i][j] = max(dp[i-1][j]-1,max(dp[i][j-1]-1,dp[i-1][j-1]+score))
    i = len2
    j = len1
    res = []
    res.append((i,j))
    while i>0 or j>0:
        if i>0 and dp[i][j] == dp[i-1][j]-1:
            i-=1
        elif j>0 and dp[i][j]==dp[i][j-1]-1:
            j-=1
        else:
            i -= 1
            j -=1
        res.append((i,j))
    res.sort(key=lambda x: (x[0],x[1]))
    print(res)



    

if __name__ == "__main__":
    while True:
        s1 = input()
        s2 = input()
        originalscore(s1,s2)
        hirschberg(s1,s2)