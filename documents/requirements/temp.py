import os
import pandas as pd


# folder_path = 'FR/modified/'
# data = []

# for file_name in os.listdir(folder_path):
#     if file_name.endswith('.txt'):  
#         file_path = os.path.join(folder_path, file_name)
#         with open(file_path, 'r', encoding='utf-8') as file:
#             content = file.read()  
#             data.append(content)  

# df = pd.DataFrame(data, columns=['Text'])
# df.index.name = 'Index'
# print(df)
# df.to_csv('FRR.csv', index=True)

input_folder = "documents/requirements/FR/"

output_file = "combined_output.txt"

all_text = []

for filename in os.listdir(input_folder):
    if filename.endswith(".txt"):
        file_path = os.path.join(input_folder, filename)
        
        with open(file_path, 'r', encoding='utf-8') as file:
            all_text.append(file.read())

with open(output_file, 'w', encoding='utf-8') as outfile:
    outfile.write("\n".join(all_text))

print(f"All files from {input_folder} have been concatenated into {output_file}")