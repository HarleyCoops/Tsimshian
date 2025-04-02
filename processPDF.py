import os
import requests
import json
import time
import zipfile
import sys
import shutil
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Mathpix API credentials
APP_ID = os.getenv("MATHPIX_APP_ID")
API_KEY = os.getenv("MATHPIX_API_KEY")

import re

def format_latex(latex_content):
    # Update document class and packages
    preamble = r"""\documentclass[10pt]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{amssymb}
\usepackage[version=4]{mhchem}
\usepackage{stmaryrd}
\usepackage{graphicx}
\usepackage[export]{adjustbox}
"""
    # Replace document class more carefully
    latex_content = re.sub(r'\\documentclass(\[.*?\])?\{.*?\}', preamble, latex_content, flags=re.DOTALL)
    
    # Convert inline math
    latex_content = re.sub(r'\$([^$]+?)\$', r'\\(\1\\)', latex_content)
    
    # Convert display math
    latex_content = re.sub(r'\$\$(.*?)\$\$', r'\\[\1\\]', latex_content, flags=re.DOTALL)
    
    # Format enumerations
    latex_content = re.sub(r'\\begin\{itemize\}', r'\\begin{enumerate}', latex_content)
    latex_content = re.sub(r'\\end\{itemize\}', r'\\end{enumerate}', latex_content)
    
    # Add labels to equations
    equation_count = 0
    def add_label(match):
        nonlocal equation_count
        equation_count += 1
        return f"{match.group(0)}\\label{{eq:{equation_count}}}"
    latex_content = re.sub(r'\\begin\{equation\}', add_label, latex_content)
    
    # Format figures
    latex_content = re.sub(r'\\includegraphics', r'\\begin{figure}[h]\n\\centering\n\\includegraphics', latex_content)
    latex_content = re.sub(r'(\\includegraphics.*?})', r'\1\n\\caption{Figure caption}\n\\end{figure}', latex_content)
    
    return latex_content

# In main.py or wherever Mathpix API response is processed
#latex_content = process_pdf(pdf_path)  # This function would handle the Mathpix API call
#formatted_latex = format_latex(latex_content)

# Save the formatted LaTeX
#with open('formatted_output.tex', 'w', encoding='utf-8') as f:
#    f.write(formatted_latex)







def process_pdf(pdf_path):
    url = "https://api.mathpix.com/v3/pdf"
    
    if not os.path.exists(pdf_path):
        print(f"Error: PDF file not found at {pdf_path}")
        return None

    headers = {
        "app_id": APP_ID,
        "app_key": API_KEY
    }

    data = {
        "options_json": json.dumps({"conversion_formats": {"tex.zip": True}})
    }

    with open(pdf_path, "rb") as file:
        files = {"file": file}
        response = requests.post(url, headers=headers, data=data, files=files)

    if response.status_code == 200:
        result = response.json()
        pdf_id = result.get("pdf_id")
        print(f"PDF successfully uploaded. PDF ID: {pdf_id}")
        return pdf_id
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

def get_conversion_status(pdf_id):
    url = f"https://api.mathpix.com/v3/pdf/{pdf_id}"
    headers = {"app_id": APP_ID, "app_key": API_KEY}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else None

def poll_conversion_status(pdf_id, timeout=300, interval=5):
    start_time = time.time()
    while time.time() - start_time < timeout:
        status = get_conversion_status(pdf_id)
        if status and status.get("status") == "completed":
            return True
        time.sleep(interval)
    return False

def download_latex(pdf_id, original_filename, pdf_path):
    url = f"https://api.mathpix.com/v3/pdf/{pdf_id}.tex.zip"
    headers = {"app_id": APP_ID, "app_key": API_KEY}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # Use the same directory as the input PDF
        output_dir = os.path.dirname(os.path.abspath(pdf_path))
        zip_filename = f"{pdf_id}.tex.zip"
        zip_path = os.path.join(output_dir, zip_filename)
        
        # Save the zip file
        with open(zip_path, "wb") as file:
            file.write(response.content)
        print(f"LaTeX extraction downloaded: {zip_filename}")
        
        # Extract the contents of the zip file
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(output_dir)
        print(f"Extracted contents of {zip_filename}")
        
        # Find the extracted .tex file
        extracted_folder = os.path.join(output_dir, pdf_id)
        extracted_tex = [f for f in os.listdir(extracted_folder) if f.endswith('.tex')]
        if not extracted_tex:
            print("Error: No .tex file found after extraction")
            return None
        
        extracted_tex_path = os.path.join(extracted_folder, extracted_tex[0])
        
        # Rename and move the extracted .tex file to match the original PDF name
        new_tex_filename = f"{original_filename}.tex"
        new_tex_path = os.path.join(output_dir, new_tex_filename)
        os.rename(extracted_tex_path, new_tex_path)
        print(f"Renamed extracted .tex file to {new_tex_filename}")
        
        # Remove the zip file
        os.remove(zip_path)
        print(f"Removed {zip_filename}")
        
        # Remove the extracted folder
        shutil.rmtree(extracted_folder)
        print(f"Removed extracted folder: {pdf_id}")
        
        return new_tex_path
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None
    
    
    
def main(pdf_path):
    original_filename = os.path.splitext(os.path.basename(pdf_path))[0]
    pdf_id = process_pdf(pdf_path)

    if pdf_id:
        if poll_conversion_status(pdf_id):
            latex_file_path = download_latex(pdf_id, original_filename, pdf_path)
            if latex_file_path:
                with open(latex_file_path, 'r', encoding='utf-8') as f:
                    latex_content = f.read()
                formatted_latex = format_latex(latex_content)
                formatted_filename = f'{original_filename}_format.tex'
                with open(formatted_filename, 'w', encoding='utf-8') as f:
                    f.write(formatted_latex)
                print(f"Successfully processed and formatted {pdf_path}")
                print(f"Formatted LaTeX saved as {formatted_filename}")
            else:
                print("Failed to download or process LaTeX file")
        else:
            print("Conversion not completed within the timeout period.")
    else:
        print("Failed to process PDF. Check the error messages above.")
        
        
        
        
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <path_to_pdf_file>")
        sys.exit(1)

    pdf_path = sys.argv[1]
    
    if not os.path.exists(pdf_path):
        print(f"Error: File not found at {pdf_path}")
        sys.exit(1)

    main(pdf_path)