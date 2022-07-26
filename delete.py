import pandas as pd 
import csv

df = pd.read_csv("FINAL 130.csv")

temp_stars_data_rows = list(stars_data_rows)
for stars_data in temp_stars_data_rows:
  if stars_data[3].lower() == "unknown":
    stars_data_rows.remove(stars_data)
