
import tiktoken
import os
import re


def count_tokens(text, model):
    enc = tiktoken.encoding_for_model(model)
    tokens = enc.encode(text)
    token_count = len(tokens)
    return token_count

def delete_all_files_in_directory(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
                print(f"Deleted file: {file_path}")
            elif os.path.isdir(file_path):
                os.rmdir(file_path)
                print(f"Deleted directory: {file_path}")
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")

def join_text_files(folder_path, file_list, output_file, isFirst, isReq):
    combined_text = ""
    counter = int(output_file)
    global req_count

    if isFirst:
        req_count = 0
    if not output_file.lower().endswith('.txt'):
        output_file += '.txt'
    
    output_file = folder_path + "_" + output_file
    
    for filename in file_list:
        file_path = os.path.join(folder_path, filename)
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                req_count += 1
                if isReq:
                    combined_text += "\nReq " + str(req_count)+ "- " + file.read() + "\n"
                else:
                    combined_text += file.read() + "\n"
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except Exception as e:
            print(f"Error reading {file_path}: {str(e)}")
    req_count = counter
    if isReq:
        output_path = os.path.join("combined_chunks/FR" , output_file)
    else: 
        output_path = os.path.join("combined_chunks/articles" , output_file)
    try:
        with open(output_path, 'w', encoding='utf-8') as output:
            output.write(combined_text)
        print(f"Combined text written to: {output_path}")
    except Exception as e:
        print(f"Error writing to {output_path}: {str(e)}")

def extract_number(filename):
    match = re.search(r'\d+', filename)
    return int(match.group()) if match else 0

def combine_files_in_folder(folder_path, isReq, size = 2048 ):
    token_counter = 0
    file_list = []
    counter = 0
    isFirst = True
    filenames = sorted(os.listdir(folder_path), key=extract_number)
    for filename in filenames:
        if filename.endswith(".txt"):
            counter += 1
            file_path = os.path.join(folder_path, filename)
            token_counter += count_tokens(file_path)
            file_list.append(filename)
            if token_counter >= size:
                join_text_files(folder_path, file_list, str(counter), isFirst, isReq)
                isFirst = False 
                file_list = []
                token_counter = 0
    join_text_files(folder_path, file_list, str(counter), isFirst , isReq)

def chunk_text(text, max_tokens = 1600):
    enc = tiktoken.encoding_for_model("gpt-4o")
    tokens = enc.encode(text)
    
    chunks = []
    current_chunk = []
    current_chunk_tokens = 0
    
    for token in tokens:
        if current_chunk_tokens + 1 <= max_tokens:
            current_chunk.append(token)
            current_chunk_tokens += 1
        else:
            chunks.append(enc.decode(current_chunk))
            current_chunk = [token]
            current_chunk_tokens = 1
    
    if current_chunk:
        chunks.append(enc.decode(current_chunk))
    
    return chunks