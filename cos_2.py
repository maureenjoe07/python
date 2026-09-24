
def read_file(file_name, mode='text'):
    try:
        if mode == 'text':
            with open(file_name, 'r', encoding='utf-8') as f:
                return f.read()          # Returns full content as a string

        elif mode == 'lines':
            with open(file_name, 'r', encoding='utf-8') as f:
                return f.readlines()     # Returns a list of lines

        elif mode == 'binary':
            with open(file_name, 'rb') as f:
                return f.read()          # Returns raw bytes (for PDFs, images, etc.)

        else:
            raise ValueError("Invalid mode. Use: 'text', 'lines', or 'binary'")

    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except PermissionError:
        print(f"Error: Permission denied to read '{file_name}'.")
    except Exception as e:
        print(f"Unexpected error: {e}")


file_name = input('enter the file you want to find: ')
content = read_file(file_name)
print(content)