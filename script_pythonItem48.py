
# Python: 3.6.0

# Author: Curt Knutson

#Purpose: Learning Python Tech Academy

#date 1/13/2016

#Item 48 

def start():
    alist = [67,45,2,13,1,998]
    blist = [89,23,33,45,10,12,45,45,45]
    print("First list unsorted")
    print(alist)
    bubbleSort(alist)
    print("First list sorted")
    print(alist)
    print("Second list unsorted")
    print(blist)
    bubbleSort(blist)
    print("Second list sorted")
    print(blist)

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                #python multiple assignment at once to swap
                alist[i],alist[i+1]=alist[i+1],alist[i]

if __name__ == "__main__":
    start()
