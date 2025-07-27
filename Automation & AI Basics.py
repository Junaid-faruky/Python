# 41. Current time
from datetime import datetime
datetime.now()

# 42. Sleep timer
import time
time.sleep(5)

# 43. Send email
import smtplib
s = smtplib.SMTP('smtp.example.com')
s.sendmail('from@example.com', 'to@example.com', 'Hello')

# 44. Read/write file
with open("file.txt", "r") as f: data = f.read()

# 45. Regex search
import re
bool(re.search(r'\d+', 'abc123'))

# 46. System command
import os
os.system('dir')

# 47. Basic ML with sklearn
from sklearn.linear_model import LinearRegression
model = LinearRegression().fit(X, y)

# 48. Predict
model.predict(X_test)

# 49. Save model
import joblib
joblib.dump(model, 'model.pkl')

# 50. Load model
model = joblib.load('model.pkl')
