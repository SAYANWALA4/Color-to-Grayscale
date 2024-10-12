def clear_file():
    """Clears the content of the specified text file."""
    
    file_path = 'tore_Values.txt'
    try:
        with open(file_path, 'w') as file:
            file.truncate()  # Truncates the file to zero length
        print(f"The file '{file_path}' has been cleared.")
    except Exception as e:
        print(f"An error occurred: {e}")

