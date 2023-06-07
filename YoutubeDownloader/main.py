# Import pytube, if you don't have, first install the package
import pytube
import time

# For elapsed time knowledge, we need to define a start time
start_time = time.time()

# Asking for a URL from the user.
url = input("Enter video URL: ")

# If you want to save downloaded videos in a folder which you want, you need to write a path.
# If path getting an empty string, video will download in the same folder with project.
path = "DownloadedVideos"

# This code will define the video with the highest resolution.
video = pytube.YouTube(url).streams.get_highest_resolution()
video.download(path)

# If you want to specify resolution, you can use get_by_resolution. For example if you want 720p;
# pytube.YouTube(url).streams.get_by_resolution("720").download(path)

# # For elapsed time knowledge, we need to define an end time
end_time = time.time()

# Calculating the elapsed time
elapsed_time = end_time - start_time

# Some information about the downloaded video
print("Download completed successfully.")
print("\nVideo Title\n", video.title)
print("\nResolution\n", video.resolution)

# Giving information about downloading time.
print("\nDownloading time: {:.2f} seconds.".format(elapsed_time))
