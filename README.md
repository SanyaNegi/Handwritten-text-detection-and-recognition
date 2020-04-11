# Handwritten-text-detection-and-recognition
Converts a handwritten text document image into .txt file.

## Requirements
Tensorflow</br> 
python-opencv</br>
numpy</br>
argparse</br>
glob</br>



## Steps to run:

1. clone this repository.
2. go to `/model` and unzip model.zip and place all it's files in `/model` directory( not in any subdirectory of `/model`) 
3. go to `/src` and run the script
```bash
python text_recognition.py --folder <path to the folder containing the images eg. /home/sanya/Desktop/images> 
```
4. A new folder or directory will be created inside the `/src` folder names `"/TextFiles"` which will contain .txt files corresponding to the images in the provided folder.
5. In order to re-run this project for a new set or the same set of images, remove or relocate the `TextFiles` folder from `/src` first.

## Sample Output

Sample output .txt file ( named Sample_Output_file1.txt ) can be found in `/data` along with the correponding input image ( named Sample_Input.jpg ) for it.


