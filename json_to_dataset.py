import argparse
import base64
import json
import os
import os.path as osp
import warnings

import PIL.Image
import yaml

from labelme import utils

# 增加的语句
import glob
# 修改 json 文件路径
json_list = glob.glob(os.path.join('C:\\Users\\surface\\Desktop\\people_pic\\pic','*.json'))


def main():

    parser = argparse.ArgumentParser()

    #  删除的语句  
    # parser.add_argument('json_file')
    # json_file = args.json_file
 
    parser.add_argument('-o', '--out', default=None)
    args = parser.parse_args()

    ###############################################增加的语句##################################
    for json_file in json_list:
    ###############################################    end       ##################################
        #######  新的名称，后面训练使用 具体的切片参数要看自己的文件名 ############
        new_name = json_file[-15:-5]+'.png'
        # print("新的名字为{}".format(new_name))
        #######  END  #############################
        if args.out is None:
            out_dir = osp.basename(json_file).replace('.', '_')
            out_dir = osp.join(osp.dirname(json_file), out_dir)
        else:
            out_dir = args.out
        if not osp.exists(out_dir):
            os.mkdir(out_dir)

        data = json.load(open(json_file))

        if data['imageData']:
            imageData = data['imageData']
        else:
            imagePath = os.path.join(os.path.dirname(json_file), data['imagePath'])
            with open(imagePath, 'rb') as f:
                imageData = f.read()
                imageData = base64.b64encode(imageData).decode('utf-8')
        img = utils.img_b64_to_arr(imageData)

        label_name_to_value = {'_background_': 0}
        for shape in sorted(data['shapes'], key=lambda x: x['label']):
            label_name = shape['label']
            if label_name in label_name_to_value:
                label_value = label_name_to_value[label_name]
            else:
                label_value = len(label_name_to_value)
                label_name_to_value[label_name] = label_value
        lbl = utils.shapes_to_label(img.shape, data['shapes'], label_name_to_value)

        label_names = [None] * (max(label_name_to_value.values()) + 1)
        for name, value in label_name_to_value.items():
            label_names[value] = name
        lbl_viz = utils.draw_label(lbl, img, label_names)

        PIL.Image.fromarray(img).save(osp.join(out_dir, 'img.png'))
        ################### 第二次修改：将label.png 替换为对应文件夹的名称 ###########
        utils.lblsave(osp.join(out_dir, new_name), lbl)
        PIL.Image.fromarray(lbl_viz).save(osp.join(out_dir, 'label_viz.png'))

        with open(osp.join(out_dir, 'label_names.txt'), 'w') as f:
            for lbl_name in label_names:
                f.write(lbl_name + '\n')

        warnings.warn('info.yaml is being replaced by label_names.txt')
        info = dict(label_names=label_names)
        with open(osp.join(out_dir, 'info.yaml'), 'w') as f:
            yaml.safe_dump(info, f, default_flow_style=False)

        print('Saved to: %s' % out_dir)


if __name__ == '__main__':
    main()

