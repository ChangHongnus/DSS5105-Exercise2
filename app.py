#### app.py ####

from flask import Flask, request, jsonify
from sklearn.linear_model import LinearRegression
import numpy as np
import statsmodels.api as sm

app = Flask(__name__)

# Training data
y = np.array([137, 118, 124, 124, 120, 129, 122, 142, 128, 114,
              132, 130, 130, 112, 132, 117, 134, 132, 121, 128])
w = np.array([0, 1, 1, 1, 0, 1, 1, 0, 0, 1,
              1, 0, 0, 1, 0, 1, 0, 0, 1, 1])
x = np.array([19.8, 23.4, 27.7, 24.6, 21.5, 25.1, 22.4, 29.3, 20.8, 20.2,
              27.3, 24.5, 22.9, 18.4, 24.2, 21.0, 25.9, 23.2, 21.6, 22.8])

# Combine W and X into feature matrix for regression
X = np.column_stack((w, x))  # shape: (20, 2)

model = LinearRegression().fit(X, y)

# # Extract coefficients
# intercept = model.intercept_      # α
# tau = model.coef_[0]              # τ (effect of treatment W)
# beta = model.coef_[1]             # β (effect of spending X)

# # Save the results to output.txt
# with open("output.txt", "w") as f:
#     f.write("Rubin Causal Model using sklearn.linear_model\n")
#     f.write("=============================================\n")
#     f.write(f"Intercept (alpha): {intercept:.4f}\n")
#     f.write(f"Treatment Effect (tau): {tau:.4f}\n")
#     f.write(f"Spending Effect (beta): {beta:.4f}\n")

# # Also print to terminal
# print("Rubin Causal Model using sklearn.linear_model")
# print("=============================================")
# print(f"Intercept (alpha): {intercept:.4f}")
# print(f"Treatment Effect (tau): {tau:.4f}")
# print(f"Spending Effect (beta): {beta:.4f}")

#  sklearn's LinearRegression doesn't have a 'summary' function.  
#  statsmodels library does.  Here's how to get a summary:
X2 = sm.add_constant(X) #  statsmodels needs a constant added
est = sm.OLS(y, X2)
est2 = est.fit()
print(est2.summary())



@app.route("/predict")
def predict():
    try:
        x = float(request.args.get("x", 0))
        w = float(request.args.get("w",0))
        y_pred = model.predict([[w,x]])[0]
    
        # Log prediction
        with open("output.txt", "w") as f:
            f.write(f"Input w: {w}, x: {x}\nPrediction: {y_pred:2f}\n")
    
        return jsonify({"w" :w, "x": x, "prediction": y_pred})

    except Exception as e:
        print("Error in /predict:", e)
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500
      

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


