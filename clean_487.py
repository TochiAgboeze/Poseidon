#ENCODING
import os

def process_file(input_file, output_file, encoding='ISO-8859-1'):
    # Read the input file with a specific encoding
    try:
        with open(input_file, 'r', encoding=encoding) as f:
            lines = f.readlines()
    except UnicodeDecodeError:
        print(f"Error decoding {input_file} with encoding {encoding}.")
        return

    # Find the line starting with 'Werte:'
    start_index = None
    for i, line in enumerate(lines):
        if line.startswith('Werte:'):
            start_index = i
            break

    if start_index is None:
        print(f"Warning: 'Werte:' not found in {input_file}.")
        return

    relevant_lines = lines[start_index + 1:]  

    with open(output_file, 'w', encoding=encoding) as f:
        f.writelines(relevant_lines)

    print(f"Processed {input_file} and saved to {output_file}.")

def process_folder(folder_path, output_folder, encoding='ISO-8859-1'):
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            input_file = os.path.join(folder_path, filename)
            output_file = os.path.join(output_folder, filename)
            process_file(input_file, output_file, encoding)

#replace the path with the right ones for ypur pc
input_folder = './487_sampling_points'
output_folder = './487_sampling_points_cleaned' 

process_folder(input_folder, output_folder)
