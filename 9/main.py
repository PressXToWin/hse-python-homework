import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json

with open('events.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

df = pd.DataFrame(data["events"])


def main_graph(dataframe):
    sns.countplot(data=dataframe, y="signature")
    plt.title("Распределение типов событий безопасности")
    plt.xlabel("Количество событий")
    plt.ylabel("Сигнатура")
    plt.savefig('graph1.png', dpi=300, bbox_inches='tight')
    plt.show()

def type_graph(dataframe):
    plt.figure(figsize=(10, 6))
    signature_type = dataframe['signature'].str.split().str[0]
    sns.countplot(y=signature_type, order=signature_type.value_counts().index)
    plt.title("Распределение типов событий безопасности (по типу события)")
    plt.xlabel("Количество событий")
    plt.ylabel("Тип события")
    plt.savefig('graph2.png', dpi=300, bbox_inches='tight')
    plt.show()


if __name__ == '__main__':
    main_graph(df)
    type_graph(df)