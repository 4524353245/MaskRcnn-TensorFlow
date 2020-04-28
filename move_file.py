import os
import shutil
filename = "mask"  # 存放json转化得到的文件夹名称
fileList = os.listdir(filename)
fileList.remove(".DS_Store")

for i in range(len(fileList)):
    img_source = "mask/" + fileList[i] + "/img.png"
    mask_source = "mask/" + fileList[i] + "/label.png"
    yaml_source = "mask/" + fileList[i] + "/info.yaml"

    img_target = "pic/img_{}.png".format(i)
    mask_target = "orig_mask/label_{}.png".format(i)
    yaml_target = "yaml/info_{}.yaml".format(i)

    shutil.copy(img_source, img_target)
    shutil.copy(mask_source, mask_target)
    shutil.copy(yaml_source, yaml_target)
