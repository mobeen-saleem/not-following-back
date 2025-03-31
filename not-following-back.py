def find_not_following_back(following_file, followers_file, output_file):
    # Open the files and read their contents
    # Use set() to create unordered collections of unique usernames
    with open(following_file, 'r') as f1, \
         open(followers_file, 'r') as f2, \
         open(output_file, 'w') as outfile:
        
        # Read all usernames from the following list
        # .read().splitlines() splits the file into a list of lines, removing newline characters
        following_list = set(f1.read().splitlines())
        
        # Read all usernames from the followers list
        followers_list = set(f2.read().splitlines())
        
        # Use set difference to find usernames in following_list that are NOT in followers_list
        # The - operator between sets finds elements in the first set that are not in the second
        not_following_back = following_list - followers_list
        
        # Write these usernames to the output file
        # Sorted() is optional, but makes the output alphabetically ordered
        for username in sorted(not_following_back):
            outfile.write(username + '\n')
        
        # Print out how many users are not following back
        print(f"Found {len(not_following_back)} users not following you back")

# Call the function with your input and output file names
find_not_following_back("following-usernames.txt", "followers-usernames.txt", "not-following-back.txt")