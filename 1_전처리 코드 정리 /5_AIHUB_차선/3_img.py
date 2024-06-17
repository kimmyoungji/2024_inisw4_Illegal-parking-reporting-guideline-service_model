import os
import shutil
import json

folder_path = "E:/차선-횡단보도 인지 영상(수도권)/Validation/낮" # 이미지 있는 폴더 경로

with open("E:/차선-횡단보도 인지 영상(수도권)/Validation/input.json") as file:
    js = json.load(file)


img_path = "E:/차선-횡단보도 인지 영상(수도권)/Validation/img" # 새로 이미지를 저장할 폴더
if not os.path.exists(img_path):
    os.makedirs(img_path)

for key in js:
    shutil.copy(os.path.join(folder_path, key[5:]), img_path)
    
print("완료")