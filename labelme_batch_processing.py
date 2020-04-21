
import os
import shutil

# 经过改进的 labelme 处理文件
# 通过输入生成的 json 文件路径生成相应的文件到目标路径
def get_samples(foldername,savePath):
    # 如果要保存的路径不存在，那么创建路径
    if os.path.exists(savePath) is False:
        os.makedirs(savePath)  
    # 找到二级文件目录
    filenames = os.listdir(foldername)  

    for filename in filenames:       
        # json 文件的绝对路径
        full_path = os.path.join(foldername, filename)
        # 找到 json 文件中的 png 文件   
        label_png = os.listdir(full_path)[0]
        # 修改文件名称
        # new_name = filename[-15:-5]+'.png'
        # new_full_path = os.path.join(full_path,new_name)
        # os.rename(os.path.join(full_path, label_png),new_full_path)
        # 从原路径复制到目标路径
        shutil.copy(os.path.join(full_path, label_png), savePath)
        print(os.path.join(full_path, label_png))
# 目标路径        
savePath = 'C:\\Users\\surface\\Desktop\\people_pic\\pic'  
# 调用函数
get_samples('C:\\Users\\surface\\Desktop\\all_pic',savePath )       