# ME396P_Characters_recognition

## Objectives:
Developing a media player that is able to identify the characters in a movie at any time and give us links for the detail of the characters being identified, shown below:
<img width="1462" alt="image" src="https://user-images.githubusercontent.com/112068708/206894720-e0308475-9b49-463b-938c-e9bfa9e441fe.png">




## Installation

### Requirements

  * Python 3.3+ or Python 2.7
  * macOS or Linux (Windows not officially supported, but might work)
  * OpenCV
  * face_recognition

### face_recognition Installation

#### Installing on Mac or Linux

First, make sure you have dlib already installed with Python bindings:

  * [How to install dlib from source on macOS or Ubuntu](https://gist.github.com/ageitgey/629d75c1baac34dfa5ca2a1928a7aeaf)
  
Then, make sure you have cmake installed:  
 
```brew install cmake```

Finally, install this module from pypi using `pip3` (or `pip2` for Python 2):

```bash
pip3 install face_recognition
```

Alternatively, you can try this library with [Docker](https://www.docker.com/), see [this section](#deployment).

If you are having trouble with installation, you can also try out a
[pre-configured VM](https://medium.com/@ageitgey/try-deep-learning-in-python-now-with-a-fully-pre-configured-vm-1d97d4c3e9b).

See https://github.com/ageitgey/face_recognition for more information.

## Usages

* Download main_video.py and simple_facerec.py. 
* Put all the character's pictures in a folder, and name the picture as the character’s name. 
* Change the path in main_video.py to load images. 
* Put the video you are going to play in your current working directory, and change the CV2 capture name to video’s name.
* Run the main_video.py and click identify to recognize the character.


