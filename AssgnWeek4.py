def modify_file_content(content):
    # Example modification: Convert all text to uppercase
    return content.upper()

def main():
    filename = input("Enter the filename to read from: ")

    try:
        with open(filename, "r") as file:
            content = file.read()
    except FileNotFoundError:
        print("❌ Error: The file was not found.")
        return
    except IOError:
        print("❌ Error: Could not read the file.")
        return

    modified_content = modify_file_content(content)

    output_filename = "modified_" + filename
    try:
        with open(output_filename, "w") as file:
            file.write(modified_content)
        print(f"✅ Modified content written to '{output_filename}'.")
    except IOError:
        print("❌ Error: Could not write to the new file.")

if __name__ == "__main__":
    main()
