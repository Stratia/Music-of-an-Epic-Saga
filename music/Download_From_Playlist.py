from pytube import Playlist
import os 


"""

Downloads from designated Youtube playlist into the "Songs" folder 
and activates Add_Songs.py script

- Downloads video
- Converts to .ogg
- Transfered to /Songs folder
- Add_Songs.py script activated, automatically placing the songs within the Mod

"""

# Downloads Playlist in .ogg format in the Songs folder
def download_playlist():
    # Creates a Playlist object to intereact with
    playlist = Playlist("https://www.youtube.com/playlist?list=PL09vFeT0St82xo678b9aeRxtJ2OiF_YNn")
    for video in playlist.videos: # Iterates through playlist
      video_stream = video.streams.filter(only_audio=True) # Ensures it only gets audio and not video
      video_stream.first().download(output_path="Songs") # Downloads song in the specified folder
      #convert_to_ogg(video.title) # Converts current video to .ogg
    activate_script() # Activates Add_Song script to add new songs to Music.asset/Songs.txt files


# Renames mp4 to an .ogg file
def convert_to_ogg(file): # File = Video Title
   pass


# Activates Add_Song.py script to put new songs in music.asset/song.txt files
def activate_script():
    exec(open("Add_Song.py").read()) # Executes Add_Song.py

download_playlist() # Calls download_playlist function, so script could start
