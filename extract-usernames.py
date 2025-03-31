def extract_usernames(input_file, output_file):
    try:
        with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
            content = infile.read()
            print(f"File contents length: {len(content)}")  # Debug print
            
            # Use regex to find usernames
            import re
            
            # Pattern to find usernames in square brackets before an Instagram link
            pattern = r'\[\n?\s*([^\]]+)\n?\]\(https://www\.instagram\.com/[^/]+/\?hl=en\)'
            
            usernames = re.findall(pattern, content, re.MULTILINE)
            
            # Clean and write unique usernames
            unique_usernames = set()
            for username in usernames:
                cleaned_username = username.strip()
                if cleaned_username and cleaned_username not in unique_usernames:
                    unique_usernames.add(cleaned_username)
                    outfile.write(cleaned_username + "\n")
            
            print(f"Found {len(unique_usernames)} unique usernames")
            print(f"Usernames extracted to {output_file}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

extract_usernames("IGfollowers.txt", "followers-usernames.txt")