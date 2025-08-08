import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import streamlit as st

# Load dataset
data = pd.read_csv('experience_salary.csv')

X = data[["YearsExperience"]]
y = data[["Salary"]]

# Train model
model = LinearRegression()
model.fit(X, y)

# Add predicted salary for regression line
data["PredictedSalary"] = model.predict(X)

# Streamlit UI
st.title("Salary Predictor Based on Experience")
st.write("Enter your experience in years to predict your salary:")

years_input = st.number_input("Years of experience", value=0, min_value=0, max_value=50, step=1, key="experience")

if years_input > 0:
    predicted_salary = model.predict([[years_input]])[0][0]
    st.success(f"Predicted salary: ${predicted_salary:,.2f}")

# Plotting
st.subheader("Regression Line")

fig, ax = plt.subplots()
ax.scatter(X, y, color="blue", label="Actual Data")
ax.plot(X, data["PredictedSalary"], color="red", label="Regression Line")

ax.set_xlabel("Years of experience")
ax.set_ylabel("Salary")
ax.set_title("Salary vs Experience")
ax.legend()
ax.grid(True)

st.pyplot(fig)
