# import requests
# import pandas as pd
# import time

# API_KEY = "3b050b17f9a011f9b267c844b4bd654fe55c4f5d05a857173f928c117398ffbe"

# # List negara dan kota (bebas kamu tambah)
# locations = [
#     {"country": "ID", "city": "Jakarta"},
#     {"country": "ID", "city": "Surabaya"},
#     {"country": "IN", "city": "Delhi"},
#     {"country": "CN", "city": "Beijing"},
#     {"country": "US", "city": "Los Angeles"},
#     {"country": "GB", "city": "London"},
#     {"country": "JP", "city": "Tokyo"}
# ]

# # Parameter dan tanggal
# params_template = {
#     "parameters[]": ["pm25", "pm10", "no2", "so2", "co", "o3"],
#     "limit": 1000,
#     "page": 1,
#     "date_from": "2024-06-01T00:00:00Z",
#     "date_to": "2024-06-10T00:00:00Z",
#     "sort": "desc",
#     "order_by": "datetime"
# }

# headers = {
#     "X-API-Key": API_KEY
# }

# all_data = []

# for loc in locations:
#     print(f"🌐 Mengambil data: {loc['city']}, {loc['country']}")
#     params = params_template.copy()
#     params["city"] = loc["city"]
#     params["country"] = loc["country"]

#     response = requests.get("https://api.openaq.org/v3/measurements", params=params, headers=headers)
    
#     if response.status_code != 200:
#         print(f"❌ Gagal ambil data untuk {loc['city']} ({response.status_code}): {response.text}")
#         continue

#     results = response.json().get('results', [])
#     if not results:
#         print(f"⚠️ Tidak ada data untuk {loc['city']}")
#         continue

#     df = pd.DataFrame(results)
#     if df.empty:
#         continue

#     df['datetime'] = pd.to_datetime(df['date'].apply(lambda x: x['utc']))
#     df['city'] = loc["city"]
#     df['country'] = loc["country"]
#     all_data.append(df)

#     time.sleep(1)  # Hindari rate limit

# # Gabungkan semua data
# if all_data:
#     combined_df = pd.concat(all_data, ignore_index=True)
#     pivoted = combined_df.pivot_table(
#         index=['datetime', 'city', 'country'],
#         columns='parameter',
#         values='value',
#         aggfunc='mean'
#     ).reset_index()

#     pivoted.columns.name = None
#     pivoted.rename(columns={
#         'pm25': 'PM2.5',
#         'pm10': 'PM10',
#         'no2': 'NO2',
#         'so2': 'SO2',
#         'co': 'CO',
#         'o3': 'O3'
#     }, inplace=True)

#     pivoted.to_csv("data/openaq_v3_all_cities.csv", index=False)
#     print("✅ Semua data berhasil disimpan di: data/openaq_v3_all_cities.csv")
# else:
#     print("❌ Tidak ada data yang berhasil dikumpulkan.")
