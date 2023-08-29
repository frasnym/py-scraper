import os, csv

OUTPUT_DIR = "dist/output"


def _ensure_folder_exist():
    # Create the dist folder if it doesn't exist
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)


def write_to_file(data: str, filename: str):
    _ensure_folder_exist()

    # Write the data to the file
    with open(os.path.join(OUTPUT_DIR, filename), "w") as f:
        f.write(data)


def write_to_csv(data: list[list[str]], filename: str):
    _ensure_folder_exist()

    with open(os.path.join(OUTPUT_DIR, filename), "w", newline="") as file:
        writer = csv.writer(file)
        for row in data:
            writer.writerow(row)
