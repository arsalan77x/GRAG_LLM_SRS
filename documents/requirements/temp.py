import os
import pandas as pd


folder_path = 'FR/modified/'
data = []

for file_name in os.listdir(folder_path):
    if file_name.endswith('.txt'):  
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()  
            data.append(content)  

df = pd.DataFrame(data, columns=['Text'])
df.index.name = 'Index'
print(df)
df.to_csv('FRR.csv', index=True)

