import os
import shutil
import json
os.chdir("/Users/atharvas/Documents/FALL_2020/vdp") # point this to the project directory 

def make_set(params):
    """
    Inputs: 
    vdp_params: dict
        A json file containing formatted dict
    
    Notes:
        dict must be formatted as such:
        params = {
            "name"  : "str", 
            "train" : ["1.jpg", "2.jpg", "3.jpg"],
            "test"  : ["4.jpg", "5.jpg", "6.jpg"]
        }
    """
    #@TODO Input verification
    normalized_name = params["name"].replace(" ", "_").lower()
    del params['name']
    folder_path = os.path.join("./data/interim/", normalized_name)
    #@TODO Logging
    for img_path in params['test']:
        new_img_path = (os.path.join(folder_path, "test", os.path.basename(img_path)))
        os.makedirs(new_img_path, exist_ok=True)
        shutil.copy(img_path, new_img_path)
    del params['test']

    for img_path in params['train']:
        new_img_path = (os.path.join(folder_path, "train", os.path.basename(img_path)))
        os.makedirs(new_img_path, exist_ok=True)
        shutil.copy(img_path, new_img_path)
    del params['train']
    
    if len(params):
        config_path = (os.path.join(folder_path, "config.json"))
        with open(config_path, 'w') as fp:
            json.dump(params, fp)        
    
    
