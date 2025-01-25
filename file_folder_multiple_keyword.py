import os
def find_excel_files_with_keyword_in_filename(directory, keywords):
    """
    Finds Excel filenames containing a specific keyword (without reading file content).

    Args:
        directory: The directory to search in.
        keywords: A list of keywords to search for.

    Returns:
        A list of full filepaths of matching Excel files.
        Returns an empty list if no files are found or if the directory doesn't exist.
    """

    matching_files = []
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return matching_files

    for filename in os.listdir(directory):
        if filename.endswith(('.xls', '.xlsx')):
            for keyword in keywords:
                if keyword.lower() in filename.lower():
                    filepath = os.path.join(directory, filename)
                    matching_files.append(filepath)
                    break

    return matching_files

# Example usage:
directory_path = r'C:\Users\HP\Downloads'  # Replace with your directory
keywords_to_search = ['Portfolio', 'Report']  # List of keywords
found_files = find_excel_files_with_keyword_in_filename(directory_path, keywords_to_search)

if found_files:
    print("Files found:")
    for file_path in found_files:
        print(file_path)
else:
    print("No matching files found.")



def generate_file_paths(base_path, file_list):
    """Generates complete filepaths by combining a base path with filenames.

    Args:
        base_path: The base directory path.
        file_list: A list of filenames.

    Returns:
        A list of complete filepaths.
    """
    file_paths = []
    for filename in file_list:
        file_path = os.path.join(base_path, filename) # create a complete filepath
        file_paths.append(file_path)
    return file_paths






# Combining both functions:
directory_path = r'C:\Users\HP\Downloads'  # Replace with your directory
keywords_to_search = ['Portfolio', 'Report']  # Example keyword

matching_filenames = find_excel_files_with_keyword_in_filename(directory_path, keywords_to_search)

if matching_filenames:
    full_filepaths = generate_file_paths(directory_path, matching_filenames)
    print("Full filepaths of matching files:")
    for filepath in full_filepaths:
        print(filepath)
else:
    print("No matching files found.")