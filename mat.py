#------------------------initialization----------------------#
from __main__ import *

#-----------------rowwise------------------------------------------#
def rowwise():
    itera = mul/N
    check = (bw*N)/N
    if check==itera:
        print("memory bound = compute bound")
        perutil = 100
        totalmul = nnz * N
        latency = totalmul/(perutil*mul)
    elif check<itera:
        print("memory bound")
        perutil = ((check*N)/mul)*100
        totalmul = nnz * N
        latency = totalmul/(perutil*mul)
    else:
        print("compute bound")
        perutil = 100
        totalmul = nnz * N
        latency = totalmul/(perutil*mul)
    print("the total latency is %d", latency )
    print("memory needed for storing partial sum is %d KB",(N*itera*4)/1000)
#-------------colwise-------------------#
def colwise():
    itera = mul/(K/nnz)
    if bw==mul:
        print("memory bound = compute bound")
        perutil = 100
        totalmul = (K/nnz) * N * K
        latency = totalmul/(perutil*mul)
    elif bw<mul:
        print("memory bound")
        perutil = ((bw)/mul)*100
        totalmul = (K/nnz) * N * K
        latency = totalmul/(perutil*mul)
    else:
        print("compute bound")
        perutil = 100
        totalmul = (K/nnz) * N * K
        latency = totalmul/(perutil*mul)
    print("the total latency is %d", latency )
    print("memory needed for storing partial sum is %d KB",(M*itera*4)/1000)

#----------------------inner------------------#
def inner():
    if bw==mul:
        print("memory bound = compute bound")
        perutil = 100
        totalmul = M * N * K
        latency = totalmul/(perutil*mul)
    elif bw<mul:
        print("memory bound")
        perutil = ((bw)/mul)*100
        totalmul = M * N * K
        latency = totalmul/(perutil*mul)
    else:
        print("compute bound")
        perutil = 100
        totalmul = M * N * K
        latency = totalmul/(perutil*mul)
    print("the total latency is %d", latency )
    print("memory needed for storing partial sum is < 1 KB")

#----------------------outer--------------------#

def outer():
    if bw==mul:
        print("memory bound = compute bound")
        perutil = 100
        totalmul = M * N * K
        latency = totalmul/(perutil*mul)
    elif bw<mul:
        print("memory bound")
        perutil = ((bw)/mul)*100
        totalmul = M * N * K
        latency = totalmul/(perutil*mul)
    else:
        print("compute bound")
        perutil = 100
        totalmul = M * N * K
        latency = totalmul/(perutil*mul)
    print("the total latency is %d", latency )
    print("memory needed for storing partial sum is %d KB",(N*M*4)/1000)

#--------------------------------------------------------#
options = {"rw" : rowwise,
           "cw" : colwise,
           "ip" : inner,
           "op" : outer,
}
options[algorithm]()
