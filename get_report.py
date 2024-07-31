# import os
# import re
# import pandas as pd


# def parse_item(item, counter):
#     id_value = counter

#     relationship_match = re.search(r'Relationship: ([^\n]+)', item)
#     if relationship_match:
#         relationship = relationship_match.group(1).strip()
#     else:
#         relationship = None

#     content_reference_match = re.search(r'Content Reference: ([^\n]+)', item)
#     if content_reference_match:
#         content_reference = content_reference_match.group(1).strip()
#     else:
#         content_reference = None

#     reason_match = re.search(r'Reason: ([^\n]+)', item)
#     if reason_match:
#         reason = reason_match.group(1).strip()
#     else:
#         reason = None

#     suggested_solution_match = re.search(r'Suggested Solution: ([^\n]+)', item)
#     if suggested_solution_match:
#         suggested_solution = suggested_solution_match.group(1).strip()
#     else:
#         suggested_solution = None

#     return {
#         'ID': id_value,
#         'Relationship': relationship,
#         'Content Reference': content_reference,
#         'Reason': reason,
#         'Suggested Solution': suggested_solution
#     }

# def extract_violations(file_path):
#     with open(file_path, 'r', encoding='utf-8') as file:
#         content = file.read()


#     violations = []
#     entries = content.split('\n\n') 
#     for entry in entries:
#         if 'Relationship: Partial Violation' in entry:
#             violations.append(entry)
#         if 'Relationship: Complete Violation' in entry:
#             violations.append(entry)
#     return violations


# for i in range(1, 46):
#     data_list = []
#     data_list.append(extract_violations(f"documents/compliance_result/{i}_comp_res.txt"))
    
#     data = []
#     for sublist in data_list:
#         for item in sublist:
#             data.append(parse_item(item, i))

#     df = pd.DataFrame(data, index=range(1, len(data) + 1))
#     df.to_csv(f"result_csv/NAIVE/{i}.csv",index = False)
import os
import pandas as pd
import glob

def is_csv_empty(file_path):
    try:
        with open(file_path, 'r') as f:
            first_line = f.readline().strip()
        return first_line == ''
    except Exception as e:
        print(f"Error checking if file is empty: {file_path}")
        print(f"Error message: {str(e)}")
        return False

def process_csv_files(folder_path):
    # Step 1: Delete empty CSV files
    for file in glob.glob(os.path.join(folder_path, '*.csv')):
        if is_csv_empty(file):
            os.remove(file)
            print(f"Deleted empty file: {file}")
        else:
            try:
                df = pd.read_csv(file)
                if df.empty or df.iloc[:, 0].isnull().all():
                    os.remove(file)
                    print(f"Deleted file with empty first column: {file}")
            except pd.errors.EmptyDataError:
                os.remove(file)
                print(f"Deleted file with no parseable data: {file}")
            except Exception as e:
                print(f"Error processing file: {file}")
                print(f"Error message: {str(e)}")

    # Step 2: Concatenate remaining CSV files
    all_files = glob.glob(os.path.join(folder_path, "*.csv"))
    if not all_files:
        print("No CSV files remaining after deletion of empty files.")
        return

    dfs = []
    for f in all_files:
        try:
            df = pd.read_csv(f)
            dfs.append(df)
        except Exception as e:
            print(f"Error reading file: {f}")
            print(f"Error message: {str(e)}")

    if not dfs:
        print("No valid CSV data found in any of the files.")
        return

    combined_csv = pd.concat(dfs, ignore_index=True)

    # Save the combined CSV
    output_path = os.path.join(folder_path, "combined_output.csv")
    combined_csv.to_csv(output_path, index=False)
    print(f"Combined CSV saved to: {output_path}")

# Usage
folder_path = "result_csv/NAIVE"
process_csv_files(folder_path)