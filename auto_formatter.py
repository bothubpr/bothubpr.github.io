#!/usr/bin/env python3
"""Auto formatter - adds YAML Front Matter to markdown files missing it."""

import os
import time
from datetime import datetime

SYNC_DIR = "/home/ziv/Desktop/SyncDrive"
CHECK_INTERVAL = 5

def process_file(filepath):
    """Process a single markdown file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        if not lines:
            return
        
        first_line = lines[0].strip()
        
        # Skip if already has YAML Front Matter
        if first_line == '---':
            return
        
        # Extract title from filename
        filename = os.path.basename(filepath)
        title = os.path.splitext(filename)[0]
        
        # Get current date
        date_str = datetime.now().strftime('%Y-%m-%d')
        
        # Create new content with Front Matter
        front_matter = f"""---
title: '{title}'
date: {date_str}
draft: false
---

"""
        
        # Combine with original content
        new_content = front_matter + ''.join(lines)
        
        # Write back
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Formatted: {filename}")
        
    except Exception as e:
        print(f"Error processing {filepath}: {e}")

def main():
    """Main loop - check directory every 5 seconds."""
    print(f"Auto formatter started. Watching: {SYNC_DIR}")
    
    while True:
        try:
            if os.path.exists(SYNC_DIR):
                for filename in os.listdir(SYNC_DIR):
                    if filename.endswith('.md'):
                        filepath = os.path.join(SYNC_DIR, filename)
                        process_file(filepath)
        except Exception as e:
            print(f"Error in main loop: {e}")
        
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
