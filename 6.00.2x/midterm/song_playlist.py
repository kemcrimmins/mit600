#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 12:55:51 2020

@author: kemcrimmins
"""

def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next 
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order 
             in which they were chosen.
    """
    play_list = []
    play_list_size = 0
    
    if songs[0][2] <= max_size:
        play_list.append(songs[0][0])
        play_list_size += songs[0][2]
    else:
        return play_list
    
    # construct sorted sublist without mutation songs
    sub_songs = songs.copy()
    sub_songs.pop(0)
    sub_songs.sort(key = lambda x: x[2])
    
    # add smallest songs until max_size is reached
    for song in sub_songs:
        if song[2] + play_list_size <= max_size:
            play_list_size += song[2]
            play_list.append(song[0])
            
    return play_list

