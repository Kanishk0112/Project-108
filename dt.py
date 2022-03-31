import plotly.figure_factory as ff
import pandas as pd
import plotly.express as px
import csv
import random


df = pd.read_csv("C:/Users/Hp/Desktop/White HAt Junior/PYTHON/Project 108/data.csv")
fig=ff.create_distplot([df["Rating"].tolist()],["rating"])
fig.show()