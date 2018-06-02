
"""
@author: Daniel
"""
import os
import json

root_dir='/media/mtezcan/New Volume/amazon/images/'
for i in range(10):
    if not os.path.exists(root_dir+str(i)):
        os.makedirs(root_dir+str(i))
    
if not os.path.exists(root_dir+'10plus'):
    os.makedirs(root_dir+'10plus')
    
    
    ###########
        
    metadata_dir='../metadata'
images_dir='../images'

json_dirs=os.listdir(metadata_dir)

for json_dir in json_dirs:
    json_file=open(metadata_dir+'/'+json_dir)
    metadata = json.load(json_file)
    object_count = metadata['EXPECTED_QUANTITY']
    
    img_dir=images_dir+'/'+json_dir[:-4]+'jpg'
    if(object_count<10):
        new_img_dir=images_dir+'/'+str(object_count)+'/'+json_dir[:-4]+'jpg'
    else:
        new_img_dir=images_dir+'/10plus/'+json_dir[:-4]+'jpg'
    shutil.move(img_dir,new_img_dir)