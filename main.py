# Importing module
from pytube import YouTube

# Main part
link = input("Enter the video link : ")
print("Downloading.../")

YouTube(link).streams.first().download()
print("Download Successful")