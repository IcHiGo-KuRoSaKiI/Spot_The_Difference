import os # for the good purpose of trying and watching that can we use pillow or not??

try:
  import PIL
except ImportError:
  print ("Trying to Install required module: PIL\n")
  os.system(' python -m pip install Pillow')
#--above lines try to install pil module if not present
#--if all went well, import required module again (for global access and charity)
from PIL import Image , ImageChops
import tkinter as tk
from tkinter import filedialog
#tkniter window creation
root = tk.Tk()
root.withdraw()
#prompting for file paths
file_path1 = filedialog.askopenfilename()
file_path2 = filedialog.askopenfilename()
#printing the file paths (not sure why i did that but meh)
#print (file_path1)
#print (file_path2)
#and finally using pillow to load them up for the processing
im1=Image.open(file_path1)
im2=Image.open(file_path2)
#im1.show()
#im2.show()
#testting the images for differnce
Test=ImageChops.difference(im1,im2)
if Test.getbbox():
    Test.show()

#so that's all. I do think that this is kinda a baby one but
#we gotta start somewhere . lets see
