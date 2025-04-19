# DSS5105-Exercise 2
# Question 1a)
# Use linear regression to estimate the parameters α, τ , and β by python.
![image](https://github.com/user-attachments/assets/7049d58d-2f01-4c8d-8821-98f09eacf1d7)

#Results

![image](https://github.com/user-attachments/assets/153803f6-4856-403a-bffc-9135af816a3c)

# Ans: α = 95.97, τ = -9.11, β = 1.5149

# Question 1b) 
# Report the estimated ATE (ˆτ ) and its statistical significance.
# Ans: Estimated Average Treatment Effect (τ̂): −9.1057
#      p-value = 0 , which is less than 0.05, therefore the effect is statistically significant.

# Question 1c)
# Briefly explain under what assumptions ˆτ can be given a causal interpretation.
# Ans: The estimated treatment effect τ̂ can be interpreted causally if, given a corporation’s sustainability spending X, the decision to participate in the carbon offset program (W) is independent of potential stakeholder engagement scores (Y), all values of X include both treated and untreated firms, the relationship between Y, W, and X is correctly specified in the model, and each firm’s outcome Y is only affected by its own treatment status W.

# Question 2a)
# Set up a GitHub repository (or use the one you already configured in Exercise #1), and configure a Dockerfile to containerize your development environment in GitHub Codespaces. You do not need to install anything locally.
# GitHub Repository: https://github.com/ChangHongnus/DSS5105-Exercise2
# Setup Dockerfile and requirements.txt in GitHub Repo
![image](https://github.com/user-attachments/assets/f53b8085-96a0-4f62-9090-b24f16979b3a)

![image](https://github.com/user-attachments/assets/1b33c45e-be99-4488-854d-1fad529a46ca)

# Question 2b) 
# Create a simple Flask API that loads your trained regression model (from Question 1) and exposes a prediction endpoint. The endpoint should accept input values for Wi (treatment indicator) and Xi (sustainability spending), and return a predicted engagement score ˆYi
# Create Flask API as app.py
![image](https://github.com/user-attachments/assets/6cd44573-90d3-410e-ae90-70da45bd3bf8)

![image](https://github.com/user-attachments/assets/cf22c82f-fb4d-448a-811b-740dc635164b)

# Question 2c)


