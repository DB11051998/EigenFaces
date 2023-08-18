import os
import skimage 


class Caltech_Dataset:
    '''
    A Dataset class for having the image object. Inorder to read the images, we used skimage package.

    Arguments

    image_folder: relative path of the folder having the images

    '''

    def __init__(self,image_folder):
        self.image_path=image_folder ##pass the relative path
        self.images= os.listdir(image_folder) ##keeps the image names

    def __len__(self):
        return len(self.images)
    def __getitem__(self,index):
        image_path=os.path.join(self.image_path,self.images[index])
        image_resized = skimage.transform .resize(image, (300, 300),
                       anti_aliasing=True)
        return image_resized
