import os
import glob
from operator import itemgetter
from itertools import groupby

cur_path = os.getcwd() # get working directory
main_path = os.path.join(cur_path,'main_folder') # get main folder path
all_paths = glob.glob(main_path+ '/**/*', recursive=True) # get all paths in main directory recursively - doesn't work in python 2

# get a list of image files (filter files with all relevant extensions)
img_paths = list(filter(lambda x: os.path.isfile(x) and (x.lower().endswith('.jpg') or x.lower().endswith('.png') or x.lower().endswith('.jpeg') or x.endswith('.gif'))\
                        , all_paths))
img_names = list(map(os.path.basename, img_paths)) # get image names
dir_paths = list(filter(lambda x: os.path.isdir(x), all_paths)) # filter only paths of directories
dir_names = list(map(os.path.basename, list(map(os.path.dirname, img_paths)))) # get images parent directory names

#print('\n'.join(img_paths)) # print paths of all images
print('\nimage names:\n'+'\n'.join(img_names)) # print names of all pictures by using image base name
print('\nnum of images:', len(img_paths)) # print number of all pictures
print('\nnum of folders:', len(dir_paths)) # print number of all folders
print('\nfolder paths:\n'+'\n'.join(dir_paths)) # print paths of all folders

pair_lst = list(zip(dir_names, img_names)) # create tuple with parent folders names & images inside
img_dict = dict((k, [v[1] for v in itr]) for k, itr in groupby(pair_lst, itemgetter(0))) # create dictionary from tuple
print('\ndictionary:\n')
print(img_dict)

print("\nfolders with 'i':")
print(list(filter(lambda x: x.find('i') > 0, list(map(os.path.basename, dir_paths))))) # print folders that contain 'i'
