Mathematics for Machine Learning: Plotting with Matplotlib

## Project Overview
This project focuses on plotting different types of graphs using Matplotlib in Python. The key objectives are to gain hands-on experience with visual data representation and understand various plotting techniques such as line graphs, scatter plots, bar charts, histograms, and stacked bar graphs. You will also learn to label plots, adjust axes, and create plots with multiple data sets.

### Learning Objectives
By the end of this project, you will be able to:
- Understand and explain various types of plots (line graph, scatter plot, bar graph, histogram).
- Use Matplotlib to plot different types of data visualizations.
- Label axes, set plot titles, and manage legends in Matplotlib.
- Scale axes and handle multiple data sets on a single plot.
- Combine multiple plots into a single figure.

### Requirements
- **Editors**: vi, vim, emacs
- **OS**: Ubuntu 16.04 LTS
- **Python version**: Python 3.5
- **Libraries**: Numpy (1.15) and Matplotlib (3.0)
- **Code Style**: Must follow pycodestyle (version 2.5)
- **Documentation**: Each module, class, and function should have clear docstrings.
- **File Execution**: Ensure all files are executable and follow the required format (#\!/usr/bin/env python3).

### Installation Instructions
To work with Matplotlib, install version 3.0 and other required dependencies:
```bash
pip install --user matplotlib==3.0
pip install --user Pillow
sudo apt-get install python3-tk
```
To verify successful installation, run:
```bash
pip list
```

### X11 Forwarding Setup
In your Vagrantfile, ensure X11 forwarding is enabled:
```ruby
Vagrant.configure(2) do |config|
  config.ssh.forward_x11 = true
end
```
- **Mac Users**: Install XQuartz and restart your machine.
- **Windows Users**: Follow additional X11 forwarding setup instructions for Windows.

### Tasks Breakdown

1. **Line Graph**  
   Plot `y = x^3` as a line graph using Matplotlib. The line should be solid red, and the x-axis should range from 0 to 10.

2. **Scatter Plot**  
   Create a scatter plot of height vs. weight, with appropriate axis labels and plot title. The data points should be magenta.

3. **Change of Scale**  
   Plot the exponential decay of C-14 with a logarithmic y-axis scale. Label the axes and ensure the x-axis ranges from 0 to 28,650 years.

4. **Multiple Graphs**  
   Plot two graphs: one for the decay of C-14 and another for Ra-226. The graphs should be distinguishable by line style (dashed red for C-14, solid green for Ra-226).

5. **Histogram**  
   Plot a histogram representing student grades, with bins every 10 units. The bars should have black outlines.

6. **All-in-One Plot**  
   Combine all previous plots into one figure with a 3x2 grid. Ensure axis labels and plot titles are set to x-small font size.

7. **Stacked Bar Chart**  
   Plot a stacked bar chart showing the quantity of different fruits each person possesses. Use specific colors for each fruit and label the axes appropriately.

### Style Guide
- Follow the **pycodestyle** guidelines strictly to ensure code quality.
- Ensure all Python files end with a new line and are executable.
- Each file should have proper documentation for easy readability and maintenance.

### Repository Structure
```bash
alu-machine_learning/
│
├── math/
│   └── plotting/
│       ├── 0-line.py
│       ├── 1-scatter.py
│       ├── 2-change_scale.py
│       ├── 3-two.py
│       ├── 4-frequency.py
│       ├── 5-all_in_one.py
│       └── 6-bars.py
└── README.md
```

### Manual Checklist
- Ensure the code passes `pycodestyle` checks.
- Verify each task manually and ensure it meets the project requirements.

