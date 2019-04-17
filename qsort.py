import random
def qsort(a):
    if len(a)<=1:
        return a
    else:
        pivot = random.choice(a)
    lesser = [i for i in a if i < pivot]
    bigger = [i for i in a if i > pivot]
    p = [pivot] 
    #p = [pivot] * a.count(pivot)  
    return qsort(lesser) + p + qsort(bigger)
