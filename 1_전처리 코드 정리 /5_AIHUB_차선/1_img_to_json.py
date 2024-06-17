import os
import shutil
import json

img_path = "E:/차선-횡단보도 인지 영상(수도권)/Validation/낮" # 이미지 있는 폴더 경로
img_list = os.listdir(img_path)
json_path = "E:/차선-횡단보도 인지 영상(수도권)/Validation/[라벨]c_1280_720_daylight_validation_1/c_1280_720_daylight_val_1"
new_folder_path = "E:/차선-횡단보도 인지 영상(수도권)/Validation/json_path"
if not os.path.exists(new_folder_path):
    os.makedirs(new_folder_path)

for img in img_list:
    path = f'{json_path}/{img[:-4]}.json'
    if not os.path.exists(path):
        print(path)
    shutil.copy(path, new_folder_path)


print("완료")