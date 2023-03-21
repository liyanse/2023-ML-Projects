# Convert a JSON File to a CSV File
import pandas as pd

df = pd.read_json('HotelReviews.json')
df.to_csv('file.csv')