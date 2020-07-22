# Image annotation and crpping

Image labeling and annotating is one of the tedious task in deep learning. Annotating a large amount of images is monotonous.
By using this tool the process is become much easier.

## Prerequisites

The only module that we have to install is,
* Opencv
```
pip install opencv-python
```

## Usage
Clone the project to your computer. Cropping and annotating image both can be done by this project. Below both are described.

### *Crop:*
For cropping the images should copy in a direcectory. In this case the images folder. For starting cropping the command should be write in the terminal.
```
python ./crop.py -i images -c cropped_images
```
here '-i' argument is used for specifying the file path where the images are located and '-c' argument is used for specifying where cropped images will be saved.
Cropping can done be using left mouse button. Pressing left button and drag through the target area will extract the cropped area. If any fault occurs same thing can be done on the image before pressing ***'a'***. After cropping one image, pressing keyboard button ***'a'*** will save the cropped image and next image will come on the screen.<br>***Example***<br>
![Screenshot (71)](https://user-images.githubusercontent.com/29359165/88235721-44894500-cc9d-11ea-8cce-862ccb951e14.png) 
![Screenshot (73)](https://user-images.githubusercontent.com/29359165/88235783-5ff45000-cc9d-11ea-8228-1b38695c8f3d.png)

### *Annotation:*
image annotation task is quite similar to the cropping process but here we need to specify a directory of a pickle file where images and the bounding boxes will be saved.
The command of start annotating is given below.
```
python .\annotation.py -i images -a img_and_annot.pickle
```
Here '-a' argument is used for specifying the pickle file directory.

Annotations can be test using this command
```
python .\annotation.py -i images -a img_and_annot.pickle
```
<br>***Example***<br>
![Screenshot (74)](https://user-images.githubusercontent.com/29359165/88236567-2290c200-cc9f-11ea-8ba6-4a3f6341e2be.png)

## Author
* Md. Iftekher Hossain [Nabil](https://www.linkedin.com/in/md-iftekher-hossain-1a3b87143/)
