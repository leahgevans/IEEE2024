make sure to install these libraries

opencv with "pip install opencv-python"

onnx with "pip install onnx"

and numpy which I believe comes installed with the previous libraries, if not "pip install numpy"


vision.py is the main vision system, it plots bounding boxes as well as prints the centroids of each detection, there is also a sleep timer to limit fps and avoid overheating.
