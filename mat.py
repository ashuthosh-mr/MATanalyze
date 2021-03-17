#------------------------initialization----------------------#
from __main__ import *
print("\t \t MAPPARAT \t \t")
#-----------------rowwise------------------------------------------#
def rowwise():
    itera = mul/N

    if bw==itera:
        print("memory bound = compute bound")
        perutil = 1
        totalmul = nnz * N
        latency = totalmul/(perutil*mul) + 1
    elif bw<itera:
        print("memory bound")
        perutil = ((bw*N)/mul)
        latency = nnz/bw
    else:
        print("compute bound")
        perutil = 1
        totalmul = nnz * N
        latency = totalmul/(perutil*mul)
        check = ((bw-itera) * nnz )/bw
    	#print("memory needed since it is compute bound",(check*4)/1000 +"KB")
    print("% utilization", perutil*100,"%")
    print("the total latency is", latency )

    print("memory needed for storing partial sum is",(N*4)/1000,"KB")

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
    print("the total latency is", latency )
    print("memory needed for storing partial sum is",(M*itera*4)/1000,"KB")

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
    print("the total latency is", latency )
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
    print("the total latency is", latency )
    print("memory needed for storing partial sum is",(N*M*4)/1000, "KB")

#--------------------------------------------------------#
options = {"rw" : rowwise,
           "cw" : colwise,
           "ip" : inner,
           "op" : outer,
}
options[algorithm]()
