# DSS5105-Exercise 2

# This exercise is about implementing and deployng a regression-based model that applies the Rubin Causal Model framework to estimate the Average Treament Effect (ATE) of a binary treatment (W, participation in a carbon offest program) on an outcome (Y,stakeholder engagement score), while adjusting for a covariate (X, sustainability speading) using linear regression. The regression model is deployed into a cloud-deployed API using Flask, Docker and GitHub Codespaces.

# app.py: 
# This script defines a Flask API that loads the trained regression model and provide a /predict API endpoint. It takes the input values (W,(Treatment) & X,(Sustainability Spending)), and returns a predicted stakeholder engagement score.

# Dockerfile: 
# The Dockerfile specifies the environment needed to run the Flask app, including the application (app.py), all dependencies (requirements.txt) and system environment (Python 3.10) and the execution steps. It ensures the app runs consistently across different machines by packaging the application and its environment together.

# requirements.txt:
# This file list all the Python packages (flask, scikit-learn, numpy, statsmodels) needed and Docker will use it to install everything automatically.

# Containerization and GitHub Codespaces:
# Containerization improves consistency, reproducibility and portability by putting the code and all dependencies in a portable container. Using GitHUb Codespaces allows user to run and test evertything in the cloud without installing anything locally, makeing development and collaboration easier.

________________________________________________________________________________________________________________________

# Question 1a)
# Use linear regression to estimate the parameters α, τ , and β by python.
![image](https://github.com/user-attachments/assets/7049d58d-2f01-4c8d-8821-98f09eacf1d7)

# Results

![image](https://github.com/user-attachments/assets/153803f6-4856-403a-bffc-9135af816a3c)

# Ans: α = 95.97, τ = -9.11, β = 1.5149

# Question 1b) 
# Report the estimated ATE (ˆτ ) and its statistical significance.
# Ans: Estimated Average Treatment Effect (τ̂): −9.1057
#      p-value = 0 , which is less than 0.05, therefore the effect is statistically significant.

# Question 1c)
# Briefly explain under what assumptions ˆτ can be given a causal interpretation.
# Ans: The estimated treatment effect τ̂ can be interpreted causally if, 
# 1) given a corporation’s sustainability spending X, the decision to participate in the carbon offset program (W) is independent of potential stakeholder engagement scores (Y).
# 2) all values of X include both treated and untreated firms.
# 3) the relationship between Y, W, and X is correctly specified in the model.
# 4) each firm’s outcome Y is only affected by its own treatment status W.

_________________________________________________________________________________________________________________________________________________

# Question 2a)
# Set up a GitHub repository (or use the one you already configured in Exercise #1), and configure a Dockerfile to containerize your development environment in GitHub Codespaces. You do not need to install anything locally.

# Ans: GitHub Repository: https://github.com/ChangHongnus/DSS5105-Exercise2
#      Setup Dockerfile and requirements.txt in GitHub Repo
![image](https://github.com/user-attachments/assets/f53b8085-96a0-4f62-9090-b24f16979b3a)

![image](https://github.com/user-attachments/assets/1b33c45e-be99-4488-854d-1fad529a46ca)

# Question 2b) 
# Create a simple Flask API that loads your trained regression model (from Question 1) and exposes a prediction endpoint. The endpoint should accept input values for Wi (treatment indicator) and Xi (sustainability spending), and return a predicted engagement score ˆYi

# Ans: Create Flask API as app.py
![image](https://github.com/user-attachments/assets/6cd44573-90d3-410e-ae90-70da45bd3bf8)

![image](https://github.com/user-attachments/assets/cf22c82f-fb4d-448a-811b-740dc635164b)

# Question 2c)
# Test your API using the following input values:
#  • Wi = 1 (corporation participated in the carbon offset program)
#  • Xi = 20 (corporation spent $20,000 on sustainability initiatives)
#   Report the predicted engagement score ˆYi returned by your API

# Ans:
# Enable Codespaces by clicking on the <>Code button, select the "Codespaces" tab, and click "Create codespace on main".
![image](https://github.com/user-attachments/assets/7206122a-f12a-45c9-8443-5c1740f2e1c5)
# Run Code in Codespaces:
# 1) Under Terminal, key in " docker build -t model-api ."
![image](https://github.com/user-attachments/assets/6db3e15c-ef61-46e1-9670-a74931309a21)
# 2) Key in " docker run -p 5000:5000 model-api" to run the container.
![image](https://github.com/user-attachments/assets/29d5e7a7-137b-459c-b82b-47bdab7a3b78)
# 3) With the container still running, open a new bash and key in " curl "http://localhost:5000/predict?w=1&x=20" " to get the predicted engagement score.
# Predicted engagement score = 117
![image](https://github.com/user-attachments/assets/b11bbc4a-cae5-4380-b9cc-e15d07a28559)


