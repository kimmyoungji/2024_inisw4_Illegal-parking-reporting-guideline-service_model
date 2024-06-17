import os
import json
import pandas as pd

img_data = pd.DataFrame(columns=['folder_name', 'img_name'])


def json_to_via(json_folder_path, save_path):
  # JSON 파일을 읽어옴
  file_list = [f for f in os.listdir(json_folder_path) if f.endswith(".json")]
  for file in file_list:
    with open(json_folder_path+'/'+file, 'r', encoding='utf-8') as f:
        js = json.load(f)

    all_dic = {}
    remove_arr = []

    for img in (js['image']):
      dic = {}
      dic['fileref'] = ""
      dic['size'] = int(img['@width']) * int(img['@height'])
      dic['filename'] = img['@name']
      dic['base64_img_data']= ""
      dic['file_attributes']= { }
      dic['regions'] = {}

      try:
          if not isinstance(img['box'], list): # list가 아니면
              img['box'] = [img['box']]
          for i, box in enumerate(img['box']):
              # 사각형 네 꼭짓점 좌표 계산
              x1, y1 = float(box['@xtl']), float(box['@ytl'])
              x2, y2 = float(box['@xbr']), float(box['@ytl'])
              x3, y3 = float(box['@xtl']), float(box['@ybr'])
              x4, y4 = float(box['@xbr']), float(box['@ybr'])

              dic['regions'][i] = {
                  'region_attributes': {
                      'label': box['@label']
                  },
                  'shape_attributes': {
                      "name": 'polygon',
                      "all_points_x": [x1, x2, x3, x4],
                      "all_points_y": [y1, y2, y3, y4]
                  }
              }
          all_dic[img['@name']] = dic
          img_data.loc[len(img_data)]=[file, img['@name']]
      except KeyError as e:
          #print(f"{img['@name']}에 box가 존재하지 않습니다.")
          remove_arr.append(img['@name'])

    with open(save_path+ '/via_' + file, 'w') as f:
      json.dump(all_dic, f)
      print(f"{save_path}에 저장 완료")

json_path = "E:/인도보행 영상/xml_label/output xml"
save_path = "E:/인도보행 영상/via_json"
if not os.path.exists(save_path):
  os.makedirs(save_path)
json_to_via(json_path,save_path)
img_data.to_csv('E:/인도보행 영상/xml_label/img_data.csv', index=False)
print("완료")