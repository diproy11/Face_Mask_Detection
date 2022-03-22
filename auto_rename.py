from dataclasses import replace

import os
# path = "/Users/musubimanagement/Desktop/image_dataset-main/with_mask"
ss="/Users/musubimanagement/Desktop/image_dataset-main/Marged"

val = 691

# path = os.chdir("/Users/musubimanagement/Desktop/image_dataset-main/with_mask")
path_without_mask = os.chdir("/Users/musubimanagement/Desktop/image_dataset-main/without_mask")
for file in os.listdir():
    
    f_name, f_extention = os.path.splitext(file)
    new_name_file = "pic{}{}".format(val,f_extention)     
    os.rename(file,ss+"/"+new_name_file)    
    val += 1
    
   
    
