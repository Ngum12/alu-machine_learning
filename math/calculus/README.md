# Mathematics for Machine Learning - Calculus

## Curriculum Overview

This curriculum focuses on developing a strong foundation in Calculus concepts that are crucial for understanding and implementing machine learning algorithms. The course includes multiple resources, tasks, and problem-solving exercises aimed at enhancing the learners' ability to apply calculus techniques in machine learning contexts.

### Learning Resources

Below are some recommended resources to guide your study of calculus for machine learning:

#### Calculus for Machine Learning:
1. **Seeing the Big Picture**  
2. **First Principles**  
3. **Finding the Derivative**  
4. **What Do We Discover?**

#### Derivatives:
- Deriving a Rule for Differentiating Powers of x:
  1. **Introducing a Substitution**  
  2. **Combining Derivatives**  
- **How to Understand Derivatives: Product, Power, and Chain Rules**  
- **Product Rule**
- **Common Derivatives and Integrals**

#### Partial Derivatives:
- **Introduction to Partial Derivatives**  
- **How to Solve Partial Derivatives?**

#### Integrals:
- **Introduction to Integration**  
- **Integration and the Fundamental Theorem of Calculus**  
- **Indefinite Integral: Basic Integration Rules, Problems, Formulas, and Trig Functions**  
- **Definite Integrals**  
- **Multiple Integrals**  
  1. **Double Integral 1**  
  2. **Double Integral 2**  

### Learning Objectives

By the end of this project, you should be able to explain the following concepts without the help of external resources:

- Summation and Product notation
- Series and common series
- Derivatives, product rule, chain rule, and common derivative rules
- Partial derivatives
- Indefinite and definite integrals
- Double integrals

## Requirements

### Multiple Choice Questions:
- All answers should be submitted in a file, ending with a new line.
- Use editors like `vi`, `vim`, or `emacs`.
- Example format:
  ```bash
  alexa@ubuntu$ cat answer_file
  2
  ```

### Python Scripts:
- All Python scripts must be compatible with Ubuntu 16.04 LTS using `python3` (version 3.5).
- Follow `pycodestyle` (version 2.5) for code style.
- Ensure each Python file starts with:
  ```bash
  #!/usr/bin/env python3
  ```
- Each function, class, and module must have documentation.
- You are not allowed to import any modules unless specified.
- Files must be executable and will be tested using `wc`.

## Tasks

### 0. Sigma is for Sum
- **Problem**: Compute the sum of a series from 2 to 5.
- **Directory**: `math/calculus`
- **File**: `0-sigma_is_for_sum`

### 1. The Greeks pronounce it sEEgma
- **Problem**: Evaluate the sum of the expression \( \sum_{k=1}^{4} 9i - 2k \).
- **Directory**: `math/calculus`
- **File**: `1-seegma`

### 2. Pi is for Product
- **Problem**: Compute the product \( \prod_{i=1}^{m} i \).
- **Directory**: `math/calculus`
- **File**: `2-pi_is_for_product`

### 3. The Greeks pronounce it pEE
- **Problem**: Compute the product \( \prod_{i=0}^{10} i \).
- **Directory**: `math/calculus`
- **File**: `3-pee`

### 4. Hello, Derivatives!
- **Problem**: Derive the function \( y = x^4 + 3x^3 - 5x + 1 \).
- **Directory**: `math/calculus`
- **File**: `4-hello_derivatives`

### 5. A Log on the Fire
- **Problem**: Find the derivative of \( x \ln(x) \).
- **Directory**: `math/calculus`
- **File**: `5-log_on_fire`

### 6. It is Difficult to Free Fools from the Chains They Revere
- **Problem**: Derive \( \ln(x^2) \).
- **Directory**: `math/calculus`
- **File**: `6-voltaire`

### 7. Partial Truths are Often More Insidious than Total Falsehoods
- **Problem**: Compute the partial derivative \( \frac{\partial f(x, y)}{\partial y} \) where \( f(x, y) = e^{xy} \).
- **Directory**: `math/calculus`
- **File**: `7-partial_truths`

### 8. Put it All Together and What Do You Get?
- **Problem**: Compute the second-order mixed partial derivative \( \frac{\partial^2}{\partial y \partial x}(e^{x^2y}) \).
- **Directory**: `math/calculus`
- **File**: `8-all-together`

### 9. Our Life is the Sum Total of All the Decisions We Make Every Day
- **Problem**: Write a Python function `summation_i_squared(n)` to calculate the sum \( \sum_{i=1}^{n} i^2 \).
- **Directory**: `math/calculus`
- **File**: `9-sum_total.py`

### 10. Derive Happiness in Oneself from a Good Day's Work
- **Problem**: Write a Python function `poly_derivative(poly)` to compute the derivative of a polynomial.
- **Directory**: `math/calculus`
- **File**: `10-matisse.py`

### 11-17: Additional Integral and Definite Integral Tasks
These tasks involve solving various integral problems and writing Python scripts to handle integrals and polynomials.

## Repository

- **GitHub Repository**: `alu-machine_learning`
- **Directory**: `math/calculus`

## Conclusion

This project on calculus for machine learning is designed to equip learners with both theoretical understanding and practical problem-solving skills. Through structured tasks and exercises, you will strengthen your calculus knowledge, which will be directly applicable to machine learning algorithms.
