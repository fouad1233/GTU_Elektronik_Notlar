import re

# Function to parse a transistor model line
def parse_transistor_line(line):
    parts = line.split()
    model_name = parts[1]
    model_type = parts[2]
    parameters = ' '.join(parts[3:])
    return model_name, model_type, parameters

# Function to extract VAF and CJE values from the parameters
def extract_vaf_cje(parameters):
    vaf_match = re.search(r'Vaf=(\d+\.?\d*(?:[eE][-+]?\d+)?)', parameters, re.IGNORECASE)
    cje_match = re.search(r'Cje=(\d+\.?\d*(?:[eE][-+]?\d+)?)', parameters, re.IGNORECASE)
    vaf_value = float(vaf_match.group(1)) if vaf_match else None
    cje_value = float(cje_match.group(1)) if cje_match else None
    return vaf_value, cje_value

# Function to check if the transistor meets the specified criteria
def meets_criteria(parameters, vaf_limit, cje_limit):
    vaf_value, cje_value = extract_vaf_cje(parameters)
    return (vaf_value is not None and vaf_value < vaf_limit) and (cje_value is not None and cje_value < cje_limit)

# Function to concatenate multi-line model definitions into single lines
def concatenate_multiline_models(file_lines):
    concatenated_models = []
    current_model = ""
    for line in file_lines:
        if line.startswith('.model'):
            if current_model:
                concatenated_models.append(current_model)
            current_model = line.strip()
        elif line.startswith('+'):
            current_model += ' ' + line.strip()
    else:
        if current_model:
            concatenated_models.append(current_model)
    return concatenated_models

# Vaf and CJE limits (You can adjust these values)
vaf_limit = 30  # Example limit for Vaf
cje_limit = 20e-12  # Example limit for CJE

# Reading the file and processing the transistors
file_path = 'standard.bjt'  # Replace with your file path
with open(file_path, 'r', encoding='ISO-8859-1') as file:
    file_content = file.readlines()

concatenated_models = concatenate_multiline_models(file_content)
transistors_meeting_criteria = []

for model_line in concatenated_models:
    model_name, model_type, parameters = parse_transistor_line(model_line)
    if meets_criteria(parameters, vaf_limit, cje_limit):
        vaf_value, cje_value = extract_vaf_cje(parameters)
        if vaf_value is not None and cje_value is not None:
            transistors_meeting_criteria.append((model_name, model_type, vaf_value, cje_value))

# Printing the filtered transistors
for transistor in transistors_meeting_criteria:
    print(transistor)
