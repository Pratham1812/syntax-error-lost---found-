from DeepImageSearch import Index,LoadData,SearchImage
import os

def find(category,image):
    if(category == "Found"):
        path = r"C:\Users\Pratham\OneDrive\Desktop\hackathon\media\images\Found"
        
        image_list = LoadData().from_folder(folder_list = [path])

        Index(image_list).Start()
        print(SearchImage().get_similar_images(image_path=image,number_of_images=1))
    else:
        path = r"C:\Users\Pratham\OneDrive\Desktop\hackathon\media\images\Lost"
        # path = os.path.join(os.getcwd(),'media','images','Lost')
        
        image_list = LoadData().from_folder(folder_list = [path])

        Index(image_list).Start()
        print(SearchImage().get_similar_images(image_path=image,number_of_images=1))


