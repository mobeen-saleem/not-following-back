def compare_files(following_file, followers_file, output_file):
    try:
        # Read all lines from both files
        with open(following_file, 'r', encoding='utf-8') as f:
            following_lines = [line.strip() for line in f if line.strip()]
        
        with open(followers_file, 'r', encoding='utf-8') as f:
            followers_lines = [line.strip() for line in f if line.strip()]
        
        # Find lines in following_lines that are not in followers_lines
        not_matching = [line for line in following_lines if line not in followers_lines]
        
        # Write the non-matching lines to the output file
        with open(output_file, 'w', encoding='utf-8') as f:
            for line in not_matching:
                f.write(line + '\n')
        
        # Print summary
        print(f"Found {len(not_matching)} lines in '{following_file}' that don't match any line in '{followers_file}'")
        print(f"Results written to '{output_file}'")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
compare_files("following.txt", "followers.txt", "not-following-back.txt")