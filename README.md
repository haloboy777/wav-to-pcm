# wav-to-pcm
This contains python scripts for converting wav files to pcm data for further processing. 

# Requirements
* pyaudio
* wave

# Usage
First record audio using 'audio_record.py'
--> This will output a 'output.wav' file

Now if you run 'check-output1.py' it will print out..
* Number of frames
* Array containing all the frames 

* Rate of the Frame capture : 44100
* Total Time recorded : 5 
###
(Both can be changed in 'audio_record.py')
* Bit length of each Frame : 16

If you just want to use array of pcm data, Just include pcm_channels.py in your code and call "pcm_channels" by passing the name of the audio output file.
###
Function "pcm_channels" will return a tupple containing [pcm_data, sample_rate]
