EADME.md

## Curriculum Mathematics for Machine Learning

### Overview
This project focuses on foundational concepts in linear algebra, essential for understanding machine learning algorithms. The project is designed for novice learners and will run from **September 8, 2024** to **September 14, 2024**.

### Learning Objectives
At the end of this project, you should be able to explain the following concepts:

- What is a vector?
- What is a matrix?
- What is a transpose?
- What is the shape of a matrix?
- What is an axis?
- What is a slice?
- How to slice a vector/matrix?
- What are element-wise operations?
- How to concatenate vectors/matrices?
- What is the dot product?
- What is matrix multiplication?
- What is NumPy?
- What is parallelization and why is it important?
- What is broadcasting?

### Requirements
- **Python Scripts**: All scripts must be written in Python 3 (version 3.5).
- **Environment**: The code will be executed on Ubuntu 16.04 LTS using NumPy (version 1.15).
- **File Structure**: 
  - All files must be executable.
  - Each file must end with a new line.
  - The first line of each file should be `#!/usr/bin/env python3`.
  - A README.md file is mandatory at the root of the project folder.
- **Documentation**: 
  - Follow `pycodestyle` (version 2.5) for coding style.
  - All modules, classes, and functions must have documentation.

### Resources
- **Read/Watch**:
  - Introduction to vectors
  - What is a matrix? (not the matrix)
  - Transpose
  - Understanding the dot product
  - Matrix Multiplication
  - The relationship between matrix multiplication and the dot product
  - The Dot Product, Matrix Multiplication, and the Magic of Orthogonal Matrices (advanced)
  - NumPy tutorial (up to Shape Manipulation)
  - NumPy basics (up to Universal Functions)
  - Array indexing
  - Numerical operations on arrays
  - Broadcasting
  - NumPy mutations and broadcasting

### Installation Instructions
1. **Install Ubuntu 16.04 and Python 3.5**:
   - Follow the instructions listed in "Using Vagrant" with `ubuntu/xenial64`.
   - Confirm Python 3.5 installation using `python3 -V`.

2. **Install pip**:
   ```bash
   wget https://bootstrap.pypa.io/get-pip.py
   sudo python3 get-pip.py
   rm get-pip.py
   ```

3. **Install required packages**:
   ```bash
   pip install --user numpy==1.15
   pip install --user scipy==1.3
   pip install --user pycodestyle==2.5
   ```

### Tasks
The project consists of several tasks that you will complete to achieve the learning objectives. Each task has specific requirements and constraints, including the use of loops, conditionals, and the expected output format.

### Conclusion
This project provides a hands-on approach to learning linear algebra concepts crucial for machine learning. Follow the guidelines and complete the tasks to enhance your understanding and skills in this area.

Citations:
[1] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/31180981/10064692-b055-4023-9198-26263274f637/paste.txt
