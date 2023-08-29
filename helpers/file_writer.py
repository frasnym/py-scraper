import os

def write_to_file(data, filename):
    # Create the dist folder if it doesn't exist
    if not os.path.exists("dist"):
        os.makedirs("dist")

    # Write the data to the file
    with open(os.path.join("dist", filename), "w") as f:
        f.write(data)
