
import os

#This makes a list of all the files in the folder where you put songs
ogg_files=(os.listdir('Songs'))

#I wanted to write this part on its own cause its kinda complicated and we gotta do it multiple times
def titleificate(file_name):
    #We just have to turn the ugly song file names into actual song titles
    #Its super duper long but basically it just gets rid of the under scores and .ogg part and capitalizes the words
    return(' '.join([word.capitalize()for word in file_name.replace('_',' ').replace('.ogg','').split()]))

#This writes the music.asset file
music_asset=open('music.asset','w')
#You have to specify which song is gonna be the main theme
music_asset.write('music={name="maintheme"\n file="Xian.ogg"}')
#The for loop can add each file from the song folder
for song in ogg_files:
    #This is the first part where we use the titleificate thingy we made
    music_asset.write('\nmusic={name="'+titleificate(song)+'"\n file="Songs/'+song+'"}')
music_asset.close()

#This writes the songs.txt file
songs_txt=open('songs.txt','w')
#As of 1.35 I'm making the main theme play during the normal game cause the update makes the main theme stop as soon as the game loads for some reason
songs_txt.write('song={name="maintheme"\n chance={modifier={factor=1}}}')
#All the other ones you can do with a for loop again
for song in ogg_files:
    #This is the other part where we use the titleification thingy
    songs_txt.write('\nsong={name="'+titleificate(song)+'"\n chance={modifier={factor=1}}}')
songs_txt.close()

#That's all! Right now it doesn't do different types of songs, like for peace or war, so I might try to do that sometime
#Also if you think there's a better way I could program it please tell me. Thanks!
