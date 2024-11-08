#!/usr/bin/env python3
# Converts the exported VS Code Copilot chat JSON file to Markdown file.
# Usage: python vschat2md.py <input_json_file>.json <output_markdown_file>.md
import json
import os
import sys

def convert_chat_to_markdown(chat_json_file_path, output_md_file_path):
    """Convert VS Code Copilot chat JSON to Markdown format."""
    
    # Read the JSON file
    try:
        with open(chat_json_file_path, 'r', encoding='utf-8') as f:
            chat_data = json.load(f)
    except Exception as e:
        print(f"Error reading chat JSON file: {e}")
        return False

    # Prepare markdown content
    markdown_content = ""
    
    # Process each request/response pair
    for request in chat_data.get('requests', []):
        # Add user message
        user_message = request.get('message', {}).get('text', '')
        markdown_content += f"**You**: *{user_message.strip()}*\n\n"
        
        # Add Copilot response
        if 'response' in request and len(request['response']) > 0:
            response_text = request['response'][0].get('value', '')
            markdown_content += f"{response_text}\n\n"

    # Write to the markdown file
    try:
        with open(output_md_file_path, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        print(f"Successfully converted chat to: {output_md_file_path}")
        return True
    except Exception as e:
        print(f"Error writing markdown file: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 3:
        script_name = os.path.basename(sys.argv[0])
        print(f"Usage: python {script_name} <input_json_file> <output_markdown_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    convert_chat_to_markdown(input_file, output_file)
