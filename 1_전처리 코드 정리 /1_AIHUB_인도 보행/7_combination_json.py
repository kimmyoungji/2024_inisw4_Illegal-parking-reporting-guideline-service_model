import os
import json

# 각 클래스의 json 합치기
def merge_class_json(class_label_path):
    '''각 클래스의 VIA 포맷 JSON 파일을 읽어 하나로 병합'''
    labels_json = os.listdir(class_label_path)

    result ={}
    for label_json in labels_json:
        label_file_path = os.path.join(class_label_path, label_json)
        with open(label_file_path) as file:
          js = json.load(file)
          result.update(js)

    with open("E:/인도보행 영상/sample_img/input.json", "w") as new_file:
      json.dump(result, new_file)
      
path = "E:/인도보행 영상/via_json"
merge_class_json(path)
print("완료")