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

```jsx
import React, { useState, useCallback } from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';

const NormalDistribution = () => {
  const [mean, setMean] = useState(0);
  const [stdDev, setStdDev] = useState(1);

  const generateData = useCallback(() => {
    const data = [];
    for (let x = -4; x <= 4; x += 0.1) {
      const y = (1 / (stdDev * Math.sqrt(2 * Math.PI))) * 
                Math.exp(-0.5 * Math.pow((x - mean) / stdDev, 2));
      data.push({ x: Number(x.toFixed(1)), y: y });
    }
    return data;
  }, [mean, stdDev]);

  return (
    <div className="p-4 bg-white rounded-lg shadow-md">
      <h2 className="text-2xl font-bold mb-4 text-center">Interactive Normal Distribution</h2>
      <ResponsiveContainer width="100%" height={300}>
        <LineChart data={generateData()} margin={{ top: 5, right: 20, bottom: 5, left: 0 }}>
          <Line type="monotone" dataKey="y" stroke="#8884d8" dot={false} />
          <CartesianGrid stroke="#ccc" strokeDasharray="5 5" />
          <XAxis dataKey="x" label={{ value: 'X', position: 'bottom' }} />
          <YAxis label={{ value: 'Probability Density', angle: -90, position: 'insideLeft' }} />
          <Tooltip />
        </LineChart>
      </ResponsiveContainer>
      <div className="mt-4">
        <label className="block mb-2">
          Mean (μ): {mean.toFixed(2)}
          <input
            type="range"
            min="-3"
            max="3"
            step="0.1"
            value={mean}
            onChange={(e) => setMean(Number(e.target.value))}
            className="w-full"
          />
        </label>
        <label className="block mb-2">
          Standard Deviation (σ): {stdDev.toFixed(2)}
          <input
            type="range"
            min="0.1"
            max="2"
            step="0.1"
            value={stdDev}
            onChange={(e) => setStdDev(Number(e.target.value))}
            className="w-full"
          />
        </label>
      </div>
    </div>
  );
};

export default NormalDistribution;
```

This interactive tool allows you to:
- Adjust the mean (μ) to shift the center of the distribution
- Modify the standard deviation (σ) to change the spread of the distribution
- See how these parameters affect the shape of the normal distribution curve in real-time

Experiment with different values to gain intuition about how probability distributions behave!

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

