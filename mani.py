import os
# Import required modules to work with file system
# Define the target folder path

# write your name of computer
folder_path = "/Users/write your name of computer/Downloads/git_tutarial/amghezi/"

# Count number of files in the folder (excluding subdirectories)
file_count = 0

print(os.listdir(folder_path))
for entry in os.listdir(folder_path):
    entry_full_path = os.path.join(f"{folder_path}/{entry}")
    if os.path.isfile(entry_full_path):
        file_count += 1

# Print the result
print(f"تعداد فایل‌های موجود در پوشه amghezi: {file_count}")
