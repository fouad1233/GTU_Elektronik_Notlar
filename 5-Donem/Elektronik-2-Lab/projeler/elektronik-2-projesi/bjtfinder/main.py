import re
file_path = 'standard.bjt'
# Function to parse the transistor model lines
def parse_transistor_line(line):
    # Extracting the model name, type and parameters
    parts = line.split()
    model_name = parts[1]
    model_type = parts[2]
    parameters = ' '.join(parts[3:])
    return model_name, model_type, parameters

# Function to check if the transistor meets the specified criteria
def meets_criteria(parameters, vaf_limit, cje_limit):
    # Extracting VAF and CJE values from the parameters string
    vaf_match = re.search(r'VAF=(\d+\.?\d*)', parameters)
    cje_match = re.search(r'CJE=(\d+\.?\d*[eE]?-?\d*)', parameters)

    vaf_value = float(vaf_match.group(1)) if vaf_match else float('inf')
    cje_value = float(cje_match.group(1)) if cje_match else float('inf')

    # Checking if both VAF and CJE are below the specified limits
    return vaf_value < vaf_limit #and cje_value < cje_limit

# Vaf and CJE limits
vaf_limit = 20
cje_limit = 1e-12

# Function to extract and return VAF and CJE values from the parameters string
def extract_vaf_cje(parameters):
    # Extracting VAF and CJE values from the parameters string
    vaf_match = re.search(r'VAF=(\d+\.?\d*)', parameters)
    cje_match = re.search(r'CJE=(\d+\.?\d*[eE]?-?\d*)', parameters)

    vaf_value = vaf_match.group(1) if vaf_match else 'Not specified'
    cje_value = cje_match.group(1) if cje_match else 'Not specified'

    return vaf_value, cje_value

# Re-reading the file and extracting the required information
transistor_info = []
with open(file_path, 'r', encoding='ISO-8859-1') as file:
    for line in file:
        if line.startswith('.model'):
            model_name, model_type, parameters = parse_transistor_line(line)
            if meets_criteria(parameters, vaf_limit, cje_limit):
                vaf_value, cje_value = extract_vaf_cje(parameters)
                transistor_info.append((model_name, model_type, vaf_value, cje_value))

print(transistor_info)
