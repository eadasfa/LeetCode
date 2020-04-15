def run():
    print(KMP("ABCDEABCAE","AC"))
def KMP(s,p):
    next_ = cal_next(s)   
    print(next_) 
    i,j = 0,0
    while i<len(s) and j < len(p):
        if j==-1 or s[i]==p[j]:
            i,j = i+1,j+1
        else:
            j = next_[j]
    if j>=len(p):
        return (i-len(p),i)
    return (-1,-1)

def cal_next(s):
    next_k = [ -1 for _ in range(len(s))]
    i,k = 0,-1
    while i<len(s)-1:
        if k==-1 or s[k] == s[i]:
            k,i=k+1,i+1
            next_k[i] = k
        else :
            k = next_k[k]
    return next_k

if __name__ == "__main__":
    run()