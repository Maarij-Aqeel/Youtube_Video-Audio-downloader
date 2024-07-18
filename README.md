# Youtube_Video-Audio-downloader

This project is a YouTube Audio/Video Downloader built using Python and Tkinter. The application allows users to download audio (mp3) or video (mp4) from YouTube by providing a URL. It offers a simple and user-friendly graphical interface to enter the YouTube link, choose the desired format, and specify the resolution for videos.

##Features
User-Friendly Interface: Simple and intuitive GUI built with Tkinter.
Clipboard Detection: Automatically detects a YouTube link if it's copied to the clipboard.
Download Options: Allows downloading in either mp3 or mp4 format.
Resolution Selection: Users can specify the desired resolution for video downloads.
Error Handling: Provides appropriate error messages for invalid URLs or unavailable resolutions.
Download Path Selection: Users can choose the directory where the files will be saved.
Requirements
Python 3.x
tkinter
pytube
pyperclip

##How to Use
###Clone the repository:
`git clone https://github.com/yourusername/youtube-downloader.git`
`cd youtube-downloader`

###Install the required packages:
`pip install tkinter pytube pyperclip`

###Run the application:
`python downloader.py`

###Using the application:

>Open the application.
>If a YouTube link is copied to your clipboard, it will be automatically inserted into the URL field.
>Choose the format (mp3 or mp4) by clicking the respective button.
>If downloading a video, specify the resolution.
>Click the "Download" button.
>Select the directory where you want to save the file.

##Acknowledgements
>pytube for providing a simple interface to download YouTube content.
>tkinter for making it easy to create the GUI.
