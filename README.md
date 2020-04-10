# Handwritten-text-detection-and-recognition
Converts a handwritten text document image into .txt file.

## Requirements
Tensorflow 

python-opencv



## Steps to run:

1. Clone this repository.
2. go to `/src` and run the script
```bash
python text_recognition.py --folder <path to the folder containing the images eg. /home/sanya/Desktop/images> 
```
3. A new folder or directory will be created inside the `/src` folder names `"/TextFiles"` which will contain .txt files corresponding to the images in the provided folder.
4. In order to re-run this project for a new set or the same set of images, remove or relocate the `TextFiles` folder from `/src` first.

