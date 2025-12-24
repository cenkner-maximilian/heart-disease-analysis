#Important modules imported
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update(plt.rcParamsDefault)
plt.rcParams['lines.markersize'] = 2

#DATA CLEANING
heart_data = pd.read_csv("heart_disease.csv")
heart_data.dropna(inplace=True)
heart_data.rename(columns={"Blood Pressure": "blood_pressure", 'Cholesterol Level': "cholesterol", "Exercise Habits": "exercise_lvl", "Family Heart Disease": "heart_dis_history", "High Blood Pressure": "high_blood_pressure", "Low HDL Cholesterol": "low_HDL", "High LDL Cholesterol": "high_LDL", "Alcohol Consumption": "alcohol_consumption", "Stress Level": "stress_level", "Sleep Hours": "sleep_hours", "Sugar Consumption": "sugar_consumption", "Triglyceride Level": "triglycerides", "Fasting Blood Sugar": "fasting_blood_sugar", "CRP Level": "crp", "Homocysteine Level": "homocysteine", "Heart Disease Status": "heart_dis_status"}, inplace=True)

for elem in ["exercise_lvl", "alcohol_consumption", "stress_level", "sugar_consumption"]:
    heart_data[elem] = heart_data[elem].map({"Low": 0, "Medium": 1, "High": 2})

for elem in ["Smoking", "Diabetes", "high_blood_pressure", "low_HDL", "high_LDL"]:
    heart_data[elem] = heart_data[elem].map({"No": 0, "Yes": 1})

#Question 1A
plt.scatter(heart_data.sleep_hours, heart_data.blood_pressure, color="#DFD0B8")
#plt.savefig("1a.png")
#plt.show()

#Question 1B
plt.scatter(heart_data.sleep_hours, heart_data.cholesterol, color="#DFD0B8")
#plt.savefig("1b.png")
#plt.show()

#Question 2
results = heart_data.groupby("heart_dis_status")["homocysteine"].median()
plt.bar(results.index, results.values, color="#DFD0B8")
#plt.savefig("2.png")
#plt.show()