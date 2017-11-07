from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import re
import sys
import os.path
from PIL import Image

def conversion_with_pil(directory, input, output):
    for file in os.listdir(directory):
        if file.endswith("."+input+""):
            img = Image.open(directory+"\\"+file)
            if img.mode == 'RGBA':
                img = img.convert('RGB')
            filename = directory+"\\"+file[0:(len(file)-len(input)-1)]
            img.save(filename.strip()+'.jpg')


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument(
          '--directory',
          type=str,
          default='\\tf_files\\dataset',
          help='Path to folders of images.'
      )
    parser.add_argument(
          '--input_format',
          type=str,
          default='',
          help='input format to parse'
      )
    parser.add_argument(
          '--output_format',
          type=str,
          default='',
          help='output format desired'
      )

    args = parser.parse_args()

    input_format = args.input_format
    output_format = args.output_format
    input_direx = os.getcwd()
    direx = args.directory

    conversion_with_pil(input_direx+direx+'\\Car', input_format, output_format)
    conversion_with_pil(input_direx+direx+'\\noCar', input_format, output_format)

