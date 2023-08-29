import os

OUTPUT_DIR = "dist"

def write_to_file(data: str, filename: str):
    # Create the dist folder if it doesn't exist
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # Write the data to the file
    with open(os.path.join(OUTPUT_DIR, filename), "w") as f:
        f.write(data)
