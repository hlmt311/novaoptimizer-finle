import os
import re

def split_content(file_path, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to match the file markers
    # ============================================================
    # FILE: path/to/file
    # ============================================================
    pattern = r'={60}\nFILE: (.*?)\n={60}'
    
    parts = re.split(pattern, content)
    
    # The first part is usually the header "NOVA LAUNCHER DESKTOP - ALL SOURCE FILES"
    # The rest are pairs of (file_path, file_content)
    
    for i in range(1, len(parts), 2):
        rel_path = parts[i].strip()
        file_content = parts[i+1].strip()
        
        # Create full path
        full_path = os.path.join(output_dir, rel_path)
        
        # Create directories if they don't exist
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        
        # Write the file
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(file_content)
            print(f"Created: {rel_path}")

if __name__ == "__main__":
    split_content('/home/ubuntu/upload/pasted_content.txt', '/home/ubuntu/nova-launcher-project')
