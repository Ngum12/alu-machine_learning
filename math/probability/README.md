# 🎲 Probability Amateur

## Dive into the World of Chance and Statistics

*By: Alexa Orrico, Software Engineer at Holberton School*

## 📊 Project Overview

Welcome to the Probability Amateur project! This exciting journey will take you through the fundamentals of probability theory and its applications in data science and machine learning.

### 🏆 Project Weight: 3

Your score will be updated as you progress through the challenges and master new concepts.

### ⏰ Timeline

- Start: Oct 6, 2024 12:00 AM
- End: Oct 12, 2024 11:59 PM

## 🎯 Learning Objectives

By the end of this project, you'll be able to explain:

- What probability is and its basic notation
- Concepts of independence and disjoint events
- Union and intersection in probability
- General addition and multiplication rules
- Probability distributions and their functions
- Cumulative distribution functions
- Mean, standard deviation, and variance
- Common probability distributions (e.g., Normal, Poisson, Binomial)

## 🧮 Key Concepts Visualization

```
    P(A∩B)     σ²     ∫ P(x) dx
      |        |         |
   ___v___   __v__    ___v___
  |       | |     |  |       |
  | Joint | | Var | | Cont.  |
  | Prob. | |     | | Dist.  |
  |_______| |_____| |_______|
      ^        ^         ^
      |        |         |
   P(A)P(B)   E[X]    P(X ≤ x)
```

## 💻 Code Examples

### Poisson Distribution

```python
import numpy as np
from poisson import Poisson

np.random.seed(0)
data = np.random.poisson(5., 100).tolist()
p1 = Poisson(data)
print('Lambtha:', p1.lambtha)
print('P(9):', p1.pmf(9))
print('F(9):', p1.cdf(9))

# Output:
# Lambtha: 4.84
# P(9): 0.03175849616802446
# F(9): 0.9736102067423525
```

### Normal Distribution

```python
import numpy as np
from normal import Normal

np.random.seed(0)
data = np.random.normal(70, 10, 100).tolist()
n1 = Normal(data)
print('Mean:', n1.mean, ', Stddev:', n1.stddev)
print('Z(90):', n1.z_score(90))
print('X(2):', n1.x_value(2))
print('PSI(90):', n1.pdf(90))
print('PHI(90):', n1.cdf(90))

# Output:
# Mean: 70.59808015534485 , Stddev: 10.078822447165797
# Z(90): 1.9250185174272068
# X(2): 90.75572504967644
# PSI(90): 0.006206096804434349
# PHI(90): 0.982902011086006
```

## 📈 Interactive Probability Visualizer

Experience the power of probability distributions with our interactive Normal Distribution visualizer:
https://github.com/user-attachments/assets/21c56d89-57f0-440f-ab19-961809fdf8a8

## 🧠 Probability Brain Teaser

**Click to reveal a probability puzzle!**

<details>
<summary>Puzzle</summary>

You have three cards: one is red on both sides, one is blue on both sides, and one is red on one side and blue on the other. You pick a card at random and look at one side. It's red. What's the probability that the other side is also red?

<details>
<summary>Solution</summary>

The probability is 2/3! There are three red sides total, two of which are on the double-red card. So if you see a red side, it's twice as likely to be from the double-red card than from the mixed card.

</details>
</details>

## 🌟 Final Thoughts

Probability is the backbone of data science and machine learning. As you progress through this project, you'll gain invaluable insights into the mathematical foundations that power modern AI and predictive analytics. 

Remember, in the world of probability, everything is possible – some things are just more likely than others! 

Happy calculating! 🎉🔢🎲 🎲 Probability Amateur

