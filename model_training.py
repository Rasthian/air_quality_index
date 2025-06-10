import os
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

# Buat folder model jika belum ada
if not os.path.exists('model'):
    os.makedirs('model')

# Baca data
data = pd.read_csv('data/global_air_quality_data.csv')

# Fitur dan target
features = ['CO', 'O3', 'NO2', 'PM10', 'SO2']
target = 'PM2.5'

# Hapus baris yang mengandung NaN
data = data.dropna(subset=features + [target])

# Bagi data
X = data[features]
y = data[target]

# Split data training dan testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Inisialisasi dan latih model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Simpan model
with open('model/random_forest_model.pkl', 'wb') as f:
    pickle.dump(model, f)

# Evaluasi model
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("✅ Model disimpan di: model/random_forest_model.pkl")
print(f"📊 MAE: {mae:.2f}")
print(f"📈 R² Score: {r2:.2f}")

# Visualisasi feature importance
importances = model.feature_importances_
feature_names = X.columns

plt.figure(figsize=(8, 5))
plt.barh(feature_names, importances, color='teal')
plt.xlabel("Feature Importance")
plt.title("Kontribusi Polutan terhadap AQI (PM2.5)")
plt.tight_layout()
plt.savefig('model/feature_importance.png')
plt.show()
