# Sparse Matrix Operations Project

## Overview

This project implements a sparse matrix data structure and provides operations to perform addition, subtraction, and multiplication on sparse matrices. The sparse matrices are read from input files in a specified format and the operations are performed using efficient memory and runtime techniques.

## Project Structure

```
/DSA-HW02---Sparse-Matrix/
            main.py
            sparse_matrix.py
    /sample_inputs/
        matrix1.txt
        matrix2.txt
        README.md
        
```

## Getting Started

### Prerequisites

- Python 3 installed on your machine.

### Installation

1. Clone the repository:

```bash
git clone https://github.com/Taiwo1105/DSA-HW02---Sparse-Matrix.git
```

2. Navigate to the project directory:

```bash
`cd DSA-HW02---Sparse-Matrix/
``

### Running the Code

1. Prepare your sparse matrix input files and place them in the `/sample_inputs/` directory. Sample files are provided as `matrix1.txt` and `matrix2.txt`.

2. Execute the `main.py` script:

```bash
python main.py
```

3. Follow the on-screen instructions to select the matrix operation and provide the file paths.

### Sample Input Files

Here are examples of how the input files should be formatted:

`matrix1.txt`:
```
rows=3
cols=3
(3, 3, 4)
(4, 4, 5)
(5, 5, 6)
```

`matrix2.txt`:
```
rows=3
cols=3
(2, 2, 7)
(3, 3, 8)
(4, 4, 9)
```

### Features

- Load sparse matrices from files.
- Perform addition, subtraction, and multiplication on sparse matrices.
- Optimized memory and runtime using a dictionary to store non-zero values.
- Error handling for incorrect file formats.

### Functions

- `SparseMatrix(char* matrixFilePath)`: Initialize a sparse matrix from a file.
- `SparseMatrix(int numRows, int numCols)`: Initialize an empty sparse matrix with given dimensions.
- `getElement(int currRow, int currCol)`: Get the value at a specific position in the matrix.
- `setElement(int currRow, int currCol, int value)`: Set the value at a specific position in the matrix.

## Author

This project was created by Taiwo Adegboyega
