def jumpingOnClouds(c, l):
    count = 0
    i = 0
    while(i<l):
        if i+2<l and c[i+2]==0:
            count = count + 1
            i = i+2
            continue
        if i+1<l and c[i+1]==0:
            count = count + 1
            i = i+1
            continue
        i=i+1

    return(count) 
