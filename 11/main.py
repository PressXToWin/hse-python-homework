import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json

with open('botsv1.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

data_rows = [item['result'] for item in data if 'result' in item]
df = pd.DataFrame(data_rows)

def main_graph(dataframe):
    sns.countplot(data=dataframe, y="EventCode")
    plt.title("Распределение типов событий безопасности")
    plt.xlabel("Количество событий")
    plt.ylabel("EventCode")
    plt.show()


if __name__ == '__main__':
    print(df.head())
    main_graph(df)