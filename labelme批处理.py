
import os
import shutil

def get_samples(foldername,savePath):
    print('savePath:',savePath)
    # 如果要保存的路径不存在，那么创建路径
    if os.path.exists(savePath) is False:
        os.makedirs(savePath)  
    filenames = os.listdir(foldername)  

    for filename in filenames:  
        # json 文件的绝对路径
        full_path = os.path.join(foldername, filename)
        # 找到 json 文件中的 png 文件
        label_png = os.listdir(full_path)[4]
        # 从原路径复制到目标路径
        shutil.copy(os.path.join(full_path, label_png), savePath)
# 目标路径        
savePath = 'C:\\Users\\surface\\Desktop\\people_pic\\cv2_mask'  
# 调用函数
get_samples('C:\\Users\\surface\\Desktop\\all_pic',savePath )       