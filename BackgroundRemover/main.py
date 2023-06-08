# Import rembg package and remove function.
from rembg import remove

# Import time package and time function to give elapsed time
from time import time

# Import os to create output_path name automatically
import os

# Write the path of the image which you want to work on.
input_path = "input_image.jpg"

# Output format must be png. PNG format supports images with transparent background.
# Name is obtained by extracting the file name from input_path and removing the extension,
# then it is combined with _output.png.
output_path = f"{os.path.splitext(os.path.basename(input_path))[0]}_output.png"

# Defining start time
start_time = time()


with open(input_path, "rb") as i:
    # Your image (input_path) will open and read in binary format. rb: read binary
    with open(output_path, "wb") as o:
        # The output_path will open and write in binary format. wb: write binary
        input_file = i.read()
        output_file = remove(input_file)
        # remove() function will remove your input_file's background
        o.write(output_file)
        # Write the background removed image (output_file) in binary format.


# Defining end time
end_time = time()

# Defining elapsed time
elapsed_time = end_time - start_time

# Return information for the user.
print("Removing background process has been completed.")
print("Process takes {:.2f} seconds.".format(elapsed_time))
