import pandas as pd
import sqlite3
from tkinter import *

main=Tk()
conn = sqlite3.connect('data.db')
c = conn.cursor()

def show_data():
    with sqlite3.connect('data.db') as db:
        df = pd.read_sql_query("SELECT * FROM data", c)

    Label(main,text = df).pack()