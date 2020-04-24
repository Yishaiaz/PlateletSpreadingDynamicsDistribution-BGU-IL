import os
import sys
import numpy as np
import pandas as pd
import cv2
from DynamicsQuantificationScript import DynamicsQuantification
from VideoDynamicsEncoder import DynamicsEncoder


def new_data_procedure(file_path: str, **kwargs):
    print("----Starting to process file: '{0}'----\n----See results folder when finished----".format(file_path))
    file_path_folder = os.sep.join(file_path.split(os.sep)[:-1])
    error = False
    print('----creating folders----')
    try:
        os.mkdir("{0}{1}Results".format(file_path_folder, os.sep))
    except FileExistsError as e:
        error = True
    try:
        os.mkdir("{0}{1}Results{1}DynamicsPlots".format(file_path_folder, os.sep))
    except FileExistsError as e:
        error = True
    try:
        os.mkdir("{0}{1}Results{1}DynamicsNumpyArrays".format(file_path_folder, os.sep))
    except FileExistsError as e:
        error = True
    try:
        os.mkdir("{0}{1}Results{1}EncodedVideos".format(file_path_folder, os.sep))
    except FileExistsError as e:
        error = True
    if error:
        print("----folders already exist----")

    # quantify the dynamics signal
    dq = DynamicsQuantification(file_path=file_path, **kwargs)
    attach_threshold, detach_threshold = dq.obtain_dynamics()
    # Encode the video with dynamics events
    de = DynamicsEncoder(attachment_thresold=attach_threshold, detachment_thresold=detach_threshold)
    de.manipulate_video(video_path=file_path,
                        manipulated_video_path="{0}{1}Results{1}EncodedVideos".format(file_path_folder, os.sep),
                        condition=de.manipulate_frame)


def example_data_procedure(**kwargs):
    new_data_procedure("ExampleData/RawVideo/sample_collagen4_1.avi", **kwargs)


def print_help():
    with open('help.txt', 'r') as help_file:
        line = help_file.readline()
        while line is not None and line != "":
            print(line)
            line = help_file.readline()


if __name__ == '__main__':
    # print(f"Arguments count: {len(sys.argv)}")
    arg_dict = {}
    for i, arg in enumerate(sys.argv):
        if arg.startswith('-'):
            try:
                arg_dict[arg] = sys.argv[i+1]
            except Exception as e:
                pass
        print(f"Argument {i:>6}: {arg}")

    manual_thresholds = None
    if sys.argv[1] == '-h':
        print_help()
        exit(0)
    if len(arg_dict) >= 1:
        if arg_dict.get('-threshold') is not None:
            manual_thresholds = arg_dict['-threshold'].split(',')
            manual_thresholds = int(manual_thresholds[0]), int(manual_thresholds[1])
        else:
            manual_thresholds = None

        if arg_dict.get('-filepath') and arg_dict['-filepath'] is not None:
            file_path = arg_dict['-filepath']
            if file_path == "":
                print("----Wrong usage, to see help pass the '-h' argument----")
            else:
                if arg_dict is not None:
                    new_data_procedure(file_path, **arg_dict)
                else:
                    new_data_procedure(file_path)

    else:
        print("----No file path detected----\n----Example data selected----")
        example_data_procedure()





