## This is where I will place the data fetching module
import json
import pandas as pd
import sqlite3

# Open JSON data
with open("[games].json") as f:
    data = json.load(f)

# Create A DataFrame From the JSON Data
normal = pd.json_normalize(data)
dframe = pd.DataFrame(normal)
df = dframe.applymap(str)

conn = sqlite3.connect("data.db")
c = conn.cursor()

df.to_sql("what",conn)