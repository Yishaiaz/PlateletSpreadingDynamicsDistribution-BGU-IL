April 24th, 2020

Yishaia Zabary - yshaayaz@post.bgu.ac.il

# Differential dynamics of early stages of platelet adhesion and spreading on collagen IV- and fibrinogen-coated surfaces
## The repository includes Python3 source code and one test dataset for the spatial dynamics analysis of the assay 

## Installation process:
- clone repository to your local system
- install python3 (this was developed on python 3.7) @ https://www.python.org/downloads/
- install project requirements using pip install -r requirements.txt

## Input/Output
### Input & assumptions
- Input: time lapse of single platelet spreading IRM imagery (other microscopy methods yet to be tested) in '.avi' video format.
- [ THE SCRIPT EXPECTS FIRST TEN FRAMES TO INCLUDE BACKGROUND IMAGERY ONLY ]
- for stack conversion from '.tiff' to '.avi' simply use Fiji (https://fiji.sc)
### Input & assumptions
- Output: platelet dynamics (attachment/detachment) plot & raw signal in '.npy' files, encoded dynamics video

## GUI 
- simply run the command 'MainUI.py -GUI' (case sensitive)

## Command Line Interfaces
- to run the script on the example data, simply use ' python MainUI.py '
### Command Line Arguments
- [-GUI] GUI(case sensitive): opens the gui of this software, no more parameters are needed.
                        example ' python MainUI -GUI ' for UNIX file systems.
- [-h] help: print this text to the terminal
                        example ' python MainUI -h ' for UNIX file systems.
- [-filepath] custom file: initiates the script for the file supplied as the next argument, must be a valid systems path.
                        example ' python MainUI -filepath "ExampleData/RawVideo/sample_collagen4.avi" ' for UNIX file systems.
- [-threshold] custom threshold: [ NOT RECOMMENDED ] allows you to configure the thresholds for detachment/attachment event intensity (@see repository Readme)
                        example ' python MainUi -filepath "ExampleData/RawVideo/sample_collagen4.avi"  -threshold 10,-10  '
                        notice, first integer is the detachment threshold and vice versa.
                        for UNIX file systems 
- [-filter] signal smoothing filter: [ NOT RECOMMENDED ]boolean variable(1=True, 0=False) whether to pass the obtained dynamics signal through a Savitzky-Goaly filter (see repo Readme for more details)
                        example ' python MainUi -filepath "ExampleData/RawVideo/sample_collagen4.avi"  -filter 1  '
                        for UNIX file systems 
 
### parameters
- threshold for events[default - auto calculated]: a tuple of negative integer (representing attachment intensity)
                and a positive integer (for detachment intensity)
- filter [default - True] : usage of a smoothing filter on the output dynamics signal retrieved

## Example data
- Included in the repository under 'ExampleData/RawVideo' folder.   
- The default parameters in `mainUI.py` were set for the collagen IV single platelet video

## Output folders
- For each input, a new (adding, not overwriting) 'Results' directory will be opened under the same directory as the raw imagery is.
- Each results folder includes the following sub-folders:
  - `DynamicsNumpyArrays`: the attachment and detachment signals obtained from the imagery.
  - `DynamicsPlots`: the plots of the signals. 
  - `EncodedVideos`: original imagery, now encoded with the dynamics(attachment/detachment) events.  


-----------------

## Citation

Please cite the following paper when using this code:
[Soon to be updated]

Please contact Yishaia Zabary, at yshaayaz@gmail.com, for any questions / suggestions / bug reports.

-----------------
