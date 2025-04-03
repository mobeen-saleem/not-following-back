def extract_usernames(input_file, output_file):
    try:
        with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
            content = infile.read()
            print(f"File contents length: {len(content)}")  # Debug print
            
            # Import regex module
            import re
            
            # Multiple patterns to try catching different Instagram format variations
            patterns = [
                # Original pattern
                r'\[\n?\s*([^\]]+)\n?\s*\]\(https://www\.instagram\.com/[^/]+/\?hl=en\)',
                
                # Alternative pattern with different URL format
                r'\[\n?\s*([^\]]+)\n?\s*\]\(https://(?:www\.)?instagram\.com/[^/]+/.*?\)',
                
                # More general pattern for any Instagram link
                r'\[\n?\s*([^\]]+)\n?\s*\]\(https://(?:.*?)instagram(?:\..*?)/([^/]+)/.*?\)',
                
                # Backup pattern using the @ format if present
                r'@([a-zA-Z0-9._]+)'
            ]
            
            # Try all patterns and collect all matches
            all_usernames = []
            for pattern in patterns:
                matches = re.findall(pattern, content, re.MULTILINE)
                if matches:
                    # Handle tuple results from capture groups
                    for match in matches:
                        if isinstance(match, tuple) and len(match) > 1:
                            # If we captured username from URL, use that
                            username = match[1]
                        else:
                            # Otherwise use the main capture
                            username = match
                        all_usernames.append(username)
            
            # Also try to find usernames directly
            direct_pattern = r'\[\s*\n?\s*([a-zA-Z0-9._]+)\s*\n?\s*\]'
            direct_matches = re.findall(direct_pattern, content, re.MULTILINE)
            all_usernames.extend(direct_matches)
            
            # Clean and write unique usernames
            unique_usernames = set()
            for username in all_usernames:
                # Make sure we're working with a string
                if not isinstance(username, str):
                    continue
                
                cleaned_username = username.strip()
                # Filter out common non-usernames
                if (cleaned_username and 
                    cleaned_username not in ['myself', 'Following'] and
                    cleaned_username not in unique_usernames):
                    unique_usernames.add(cleaned_username)
                    outfile.write(cleaned_username + "\n")
            
            print(f"Found {len(unique_usernames)} unique usernames")
            
            # If no usernames found, try a more aggressive approach
            if len(unique_usernames) == 0:
                print("No usernames found with standard patterns. Trying fallback method...")
                # Look for any text between square brackets
                fallback_pattern = r'\[\s*\n?\s*([^\]]+?)\s*\n?\s*\]'
                fallback_matches = re.findall(fallback_pattern, content, re.MULTILINE)
                
                for match in fallback_matches:
                    cleaned_match = match.strip()
                    # Skip certain patterns
                    if (cleaned_match and 
                        cleaned_match != 'myself' and 
                        not cleaned_match.startswith('!') and
                        not cleaned_match.startswith('http')):
                        unique_usernames.add(cleaned_match)
                        outfile.write(cleaned_match + "\n")
                
                print(f"Fallback method found {len(unique_usernames)} potential usernames")
            
            print(f"Usernames extracted to {output_file}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

extract_usernames("IGfollowing.txt", "following-usernames.txt")