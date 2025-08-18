import csv
data=[["Name","Age"],["Eren",15],["Armin",15]]
with open("data.csv","w",newline="") as f:
    writer=csv.writer(f)