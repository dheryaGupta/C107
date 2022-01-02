import pandas as pd
import csv
import plotly.express as px
import plotly.figure_factory as ff

df = pd.read_csv("data2.csv")

fig=ff.create_distplot([df["Avg Rating"].tolist()],["Avg Rating"])
fig.show()