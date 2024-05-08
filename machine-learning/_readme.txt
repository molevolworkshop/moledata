Note: I (Paul Lewis) added the following lines at the beginning of Machine_Learning_for_Population_Genetics_V2.ipynb:

from tensorflow.python.client import device_lib
device_lib.list_local_devices()

This was based on advice in https://gist.github.com/Quasimondo/7e1068e488e20f194d37ba80696b55d8. I found that I did NOT need to add

import os
os.environ["CUDA_VISIBLE_DEVICES"]="0"

which was suggested in other places. 
