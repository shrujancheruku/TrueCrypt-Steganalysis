# TrueCrypt-Steganography

* The first step is to create a hidden volume in TrueCrypt.
* The outer volume password doesn't matter, since we overwrite that. Remember the inner password though.
* Once your volume is created, run `hideVolume.py <video> <tc volume>`
* Open up the tc volume, and the hidden partition should still be accessible
* The video should also play in VLC, etc. Sometimes it overwrites the first second or so of video data.
* Only works with certain encodings of mp4, still haven't figured out how to generalize it
