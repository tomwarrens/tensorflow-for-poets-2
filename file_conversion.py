from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import re
import sys
import os.path
from PIL import Image


def ale_converti(folder_path, form_in, form_out):
	for file in os.listdir(folder_path):
		if file.endswith("." + form_in + ""):
			img =Image.open(folder_path +  file)
			if img.mode == "RGBA" or mode == "P":
				img =img.convert('RGB')
			filename = folder_path + file[0:(len(file)-len(form_in)-1)]
			img.save(filename + '.' + form_out)
	to_delete = [el for el in os.listdir(folder_path) if el.endswith('.' + form_in + '')]
	
	for f in to_delete:
		os.remove(folder_path + f)

	


if __name__ == '__main__':

  single_folder = False
  my_path = os.getcwd() + '/'
    
  parser = argparse.ArgumentParser()
  parser.add_argument("--dir", type=str, help="forder s path", required=True)

  parser.add_argument("--one_folder", type=bool, help="modify just a single folder?", required=False)

  parser.add_argument("--input_format",type=str , help="input type files", required=True)

  parser.add_argument("--output_format", type=str, help="type of output format", default='jpg', required=False)

  args = parser.parse_args()


  if args.input_format:
  	input_format = args.input_format
    
  if args.output_format:
  	output_format = args.output_format
    
  if args.dir:
  	to_go = args.dir 
    
  if args.one_folder:
    single_folder=args.one_folder


  dest_path = my_path + to_go + '/'

  if single_folder:
  	ale_converti(dest_path, input_format, output_format)
  	print('\n', "did it! " ,'\n')

  else:
  	dir_list = [el for el in os.listdir(dest_path) if el != '.DS_Store']
  	for folder in dir_list:
  		ale_converti(dest_path + folder + '/', input_format, output_format)
  		print('\n', 'Just converted the folder ----> ', folder)
  		print('\n')
  	print('done!')
  	


