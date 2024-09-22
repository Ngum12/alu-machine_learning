# Advanced Linear Algebra

This repository contains implementations of various matrix-related functions in Python. Each function is designed to handle different linear algebra operations, including calculating determinants, minors, cofactors, adjugates, and inverses of matrices, as well as assessing matrix definiteness.

## Table of Contents
- [Determinant](#determinant)
- [Minor](#minor)
- [Cofactor](#cofactor)
- [Adjugate](#adjugate)
- [Inverse](#inverse)
- [Definiteness](#definiteness)

## Determinant
The `determinant` function calculates the determinant of a matrix.

### Function Signature:
```python
def determinant(matrix):
```

### Parameters:
- `matrix`: A list of lists representing a square matrix.

### Exceptions:
- Raises a `TypeError` if `matrix` is not a list of lists.
- Raises a `ValueError` if `matrix` is not a square matrix.

### Return:
- Returns the determinant of the matrix.

### Example:
```bash
./0-main.py
1
5
-2
0
192
matrix must be a list of lists
matrix must be a square matrix
```

## Minor
The `minor` function calculates the minor matrix of a matrix.

### Function Signature:
```python
def minor(matrix):
```

### Parameters:
- `matrix`: A list of lists representing a square matrix.

### Exceptions:
- Raises a `TypeError` if `matrix` is not a list of lists.
- Raises a `ValueError` if `matrix` is not a non-empty square matrix.

### Return:
- Returns the minor matrix of the input matrix.

### Example:
```bash
./1-main.py
[[1]]
[[4, 3], [2, 1]]
[[1, 1], [1, 1]]
[[-12, -36, 0], [10, -34, -32], [47, 13, -16]]
matrix must be a list of lists
matrix must be a non-empty square matrix
```

## Cofactor
The `cofactor` function calculates the cofactor matrix of a matrix.

### Function Signature:
```python
def cofactor(matrix):
```

### Parameters:
- `matrix`: A list of lists representing a square matrix.

### Exceptions:
- Raises a `TypeError` if `matrix` is not a list of lists.
- Raises a `ValueError` if `matrix` is not a non-empty square matrix.

### Return:
- Returns the cofactor matrix of the input matrix.

### Example:
```bash
./2-main.py
[[1]]
[[4, -3], [-2, 1]]
[[1, -1], [-1, 1]]
[[-12, 36, 0], [-10, -34, 32], [47, -13, -16]]
matrix must be a list of lists
matrix must be a non-empty square matrix
```

## Adjugate
The `adjugate` function calculates the adjugate matrix of a matrix.

### Function Signature:
```python
def adjugate(matrix):
```

### Parameters:
- `matrix`: A list of lists representing a square matrix.

### Exceptions:
- Raises a `TypeError` if `matrix` is not a list of lists.
- Raises a `ValueError` if `matrix` is not a non-empty square matrix.

### Return:
- Returns the adjugate matrix of the input matrix.

### Example:
```bash
./3-main.py
[[1]]
[[4, -2], [-3, 1]]
[[1, -1], [-1, 1]]
[[-12, -10, 47], [36, -34, -13], [0, 32, -16]]
matrix must be a list of lists
matrix must be a non-empty square matrix
```

## Inverse
The `inverse` function calculates the inverse of a matrix.

### Function Signature:
```python
def inverse(matrix):
```

### Parameters:
- `matrix`: A list of lists representing a square matrix.

### Exceptions:
- Raises a `TypeError` if `matrix` is not a list of lists.
- Raises a `ValueError` if `matrix` is not a non-empty square matrix.

### Return:
- Returns the inverse of the matrix or `None` if the matrix is singular.

### Example:
```bash
./4-main.py
[[0.2]]
[[-2.0, 1.0], [1.5, -0.5]]
None
[[-0.0625, -0.052083333333333336, 0.24479166666666666], [0.1875, -0.17708333333333334, -0.06770833333333333], [0.0, 0.16666666666666666, -0.08333333333333333]]
matrix must be a list of lists
matrix must be a non-empty square matrix
```

## Definiteness
The `definiteness` function calculates the definiteness of a matrix.

### Function Signature:
```python
def definiteness(matrix):
```

### Parameters:
- `matrix`: A numpy array representing a square matrix.

### Exceptions:
- Raises a `TypeError` if `matrix` is not a numpy array.
- Returns `None` if `matrix` is not a valid matrix.

### Return:
- Returns one of the following strings: `Positive definite`, `Positive semi-definite`, `Negative definite`, `Negative semi-definite`, or `Indefinite`.

### Example:
```bash
./5-main.py
Positive definite
Positive semi-definite
Negative semi-definite
Negative definite
Indefinite
None
None
matrix must be a numpy.ndarray
```

## Repository
- **GitHub repository:** `alu-machine_learning`
- **Directory:** `math/advanced_linear_algebra`

```
