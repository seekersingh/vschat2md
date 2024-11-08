#!/usr/bin/env python3
# Converts all json files from a directory to markdown files using vschat2md command
# It is used with vscode copilot chat export to convert all json files to markdown files.
# Usage: python vschat2mdd.py <input_dir>
import os
import sys
import subprocess

def convert_dir(dir_path):
    """Converts the .json files from the directory to .md file using vschat2md command."""
    # Checks if vschat2md command exists
    if subprocess.run(["which", "vschat2md"], capture_output=True).returncode != 0:
        print("Error: vschat2md command not found. Please install it before using.")
        sys.exit(1)

    for file in os.listdir(dir_path):
        if file.endswith(".json"):
            input_file = os.path.join(dir_path, file)
            output_file = os.path.join(dir_path, file.replace(".json", ".md"))
            
            # Runs the conversion script
            try:
                subprocess.run(["vschat2md", input_file, output_file], check=True)
            except Exception as e:
                print(f"Error converting {input_file}: {e}")
                continue
            print(f"Successfully converted {input_file} to {output_file}")

if __name__ =="__main__":
    if len(sys.argv) != 2:
        script_name = os.path.basename(sys.argv[0])
        print(f"Usage: python {script_name} <input_json_file>")
        sys.exit(1)
    
    input_dir = sys.argv[1]
    
    convert_dir(input_dir)