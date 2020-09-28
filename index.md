## Mini Project 1

Team Members:

Raj Shinde (M.Eng. Robotics) - 

Shubham Sonawane (M.Eng. Robotics) - 116808996

### Introduction to Kalman Filters

Kalman filter is a powerful tool for combining information in presence of information uncertainty. It can be used in any place where the information about the system is uncertain. It is used to make an educated guess of what the system will do in the next time-step.

Kalman filter is an ideal tool for systems that are continuously changing. The simple calculations involved means that the speed is an advantage, making it an ideal candidate for real-time systems to be implemented on embedded platform.  

### Formal Definition

The Kalman filter requires the following information to run its algorithm:

1.	Model of the system in state space(A,B,C matrices)
2.	Input of each time step
3.	Sensor measurements
4.	Initial system state and covariance (the initial state is the best estimate of the starting point, and it is a good practice to have a large covariance matrix initially)
5.	Measurement noise covariance, which is usually calculated offline by taking a sensor and comparing it against a known value. 
6.	Model/input covariance, it is used as a tuning mechanism to optimize the filter performance. 

The Kalman filter follows a predict-update cycle to arrive at a state measurement. The process can be summed up as follows:

![BlockDiagram](img/BlockDiagram.png)

The conditions under which the Kalman filter is known to produce optimal results are:
1.	The input noise and sensor noise are independent , and uncorrelated in time with each other
2.	The input noise and measurement noise both follow gaussian distribution. 
3.	System is linear.

![Equations](img/equations.PNG)

Kalman filter operates in 2 stages, time update and measurement update. 

1.	Time update: Before starting the iterations for Kalman filter, it is necessary to enter the estimate of the state variable vector and the error covariance matrix. The time update activity involves 2 primary equations. (1) calculates the a priori estimate of the state variable vector. This is the estimate of the state at given time step k when the system measurements upto time step k-1 are known. (2) updates the error covariance matrix P. 

2.	Measurement update: (3) calculates the Kalman gain K which is helps in reducing the error covariance matrix P. (4) calculates the estimate of the state at time k given measurement data upto time k. (5) calculates the error covariance matrix P (posteriori)

### Key Results

### Application in decision making for robots

### Variants

Extended Kalman Filter

Unscented Kalman Filter

### Open research problems

### References

You can use the [editor on GitHub](https://github.com/shubham1925/Kalman-Filter/edit/gh-pages/index.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/shubham1925/Kalman-Filter/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://docs.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.
