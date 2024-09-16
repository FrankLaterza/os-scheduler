import os

def concatenate_files(folder_path, output_file):
    with open(output_file, 'w') as outfile:
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            outfile.write(f'Filename: {filename}\n')  # Write the title of the file
            with open(file_path, 'r') as infile:
                outfile.write(infile.read())
            outfile.write('\n')  # Add newline after each file's content

def main():
    folder_path = input("Enter the path to the folder containing text files: ")
    output_file = input("Enter the desired name for the output file: ")
    concatenate_files(folder_path, output_file)
    print(f"All files have been concatenated into {output_file}")

if __name__ == "__main__":
    main()