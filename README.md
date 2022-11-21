# ME396P_Characters_recognition

## Installation

### Requirements

  * Python 3.3+ or Python 2.7
  * macOS or Linux (Windows not officially supported, but might work)
  * OpenCV
  * face_recognition

### face_recognition Installation:

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

run

### Input and output images and videos

Input and output videos are Movie.mp4 and Characters_recognition.avi on the Box (https://utexas.app.box.com/folder/177206050234?s=558vqe2g22wz5dubw3t5lb4xnl3yn3c7), respectively. The input images are uploaded in the repository. If .avi file cannot be opened on macOS, please use MKPlayer for viewing. 


