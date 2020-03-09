# CV_project_YCP_preprocessing

## Setup
The environment was set up on a Win 10 machine (64 bit) using conda.
All dependencies can be installed from the "requirements.txt" file.
If you have trouble with the open3d module on Windows (saying something about a DLL not being found), 
install the latest Visual C++ Redistributable from [here](https://support.microsoft.com/en-us/help/2977003/the-latest-supported-visual-c-downloads).

## Generate Point Cloud
Open the file ycb_generate_point_cloud.py and edit the variables *viewpoint_camera* and *viewpoint_camera* in the first section.
Run the script from the project's root directory:
```python
python ycb_generate_point_cloud.py
```
The resulting point cloud will be saved under './data/<object_name>/clouds'.

## Display Point Cloud
Open the file display_point_cloud.py and edit the file path of the .ply file you want to display.
Run the script from the project's root directory:
```python
python display_point_cloud.py
```