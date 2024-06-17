import json
import os
import xmltodict

def xml_to_json(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        xml_content = file.read()

    # Convert XML to a Python dictionary
    data_dict = xmltodict.parse(xml_content)

    # Convert the Python dictionary to a JSON string
    json_data = json.dumps(data_dict, indent=4, ensure_ascii=False)

    # Write the JSON string to an output file
    with open(output_file, 'w', encoding='utf-8') as json_file:
      json_file.write(json_data)

path = "E:/인도보행 영상/xml_label/output xml" + '/' # 너네 xml 들어있는 폴더
input_files = os.listdir(path) # 변환전 xml들 경로
for input_file in input_files:
  output_file = input_file[:-4]+'.json' # 변환후 json 경로
  xml_to_json(path+input_file, path+output_file)
print("완료")