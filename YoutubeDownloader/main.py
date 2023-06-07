# Import pytube, if you don't have, first install the package
import pytube

# Asking a URL from user.
url = input("Enter video URL: ")

# If you want to save downloaded videos in a folder which you want, you need to write a path.
# If path getting an empty string, video will download in the same folder with project.
path = "DownloadedVideos"

# This code will download the video with the highest resolution.
pytube.YouTube(url).streams.get_highest_resolution().download(path)

# If you want to specify resolution, you can use get_by_resolution. For example if you want 720p;
# pytube.YouTube(url).streams.get_by_resolution("720").download(path)