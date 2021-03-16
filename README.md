# MATanalyze
The current file works for different algorithms given bandwidth,dimensions,multipliers,nnz of the sparse matrix, matrix A off chip, matrix B on chip. 
The type of Matrix multiplication assumed is Sparse-Dense.

## Downloading the files :
From the terminal,
```
git clone https://github.com/ashuthosh-mr/MATanalyze
```
## Inputs :
The parameters could be changed in the param.py file :

* Dimensions : M,K,N = 256,256,256
* Number of NNZ in Matrix A : nnz = 256
* Algorithm used, rw for row-wise, cw for column-wise, in for inner product, op for outer product : algorithm = "rw"
* Number of multipliers : mul = 512
* Number of values every cycle (assuming compute freq = data transfer freq) : bw = 2
* Location of Matrix1 (off if off chip, on if on chip) : mat1 = "off"
* Location of Matrix1 (off if off chip, on if on chip) : mat2 = "on"

## Running the code :
From the terminal go to the MATanalyze directory that contains the following files : mat.py and param.py \
After making the necessary changes to the param.py file,
```
python param.py 
```
## Output :
The output will contain the following information :

* Memory bound or compute bound?
* Latency
* Minimum On chip memory necessary
