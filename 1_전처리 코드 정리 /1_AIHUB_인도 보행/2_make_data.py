import pandas as pd
import os
from lxml.etree import XMLSyntaxError
from lxml import etree # xml

# 처음 만들 때
data = pd.DataFrame(columns=['box_num', 'xml','truck', 'stop', 'motorcycle', 'fire_hydrant', 'car'])
# 있는 거 불러오기
#data = pd.read_csv('data.csv')

# 트럭, 버스/택시 정류장, 오토바이, 소화전, 차
find_label = ['truck', 'stop', 'motorcycle', 'fire_hydrant', 'car']

def count_labels(path, xml_path):
  # xml 여러 개 있는 경로 설정하기
  try:
    tree = etree.parse(path +'/' +xml_path)
    root = tree.getroot()
    count_list = [n, xml_path]
    for fl in find_label:
      elements = root.xpath(f'.//box[@label="{fl}"]')
      count = len(elements)
      count_list.append(count)
    #print(count_list)
    data.loc[len(data)]=count_list
  except XMLSyntaxError as e:
    print(f"Error parsing {xml_path}: {e}")
  except OSError as e:
    print(f"Error parsing {xml_path}: {e}")
    
for n in range(1,9):
  path= f'E:/인도보행 영상/xml_label/box{n}'
  files = os.listdir(path) # 리스트 형태로 경로 아래 파일들 리턴
  # 예시: ['0617_02.xml', '0617_05.xml', '0617_04.xml', '0617_01.xml', '0619_01.xml']

  for file in files:
    xml_path = file # 파일 이름만
    count_labels(path, xml_path)

print(len(data))    
#print(data)
# 저장
data.to_csv('E:/인도보행 영상/xml_label/data.csv', index=False)
print("저장됐습니다")