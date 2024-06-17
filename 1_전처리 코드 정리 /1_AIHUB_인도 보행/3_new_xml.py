from lxml.etree import XMLSyntaxError
from lxml import etree # xml

# 필요없는 거 삭제 + 필요한 것만 추출 되는지 보기
def make_new_xml(path, values):
  tree = etree.parse(path) # XML 파일 파싱
  root = tree.getroot() # 문서의 최상위 요소 찾기
  new_root = etree.Element("root") # 새로운 루트 요소 생성
  for value in values:
    elements = root.xpath(f'.//box[@label="{value}"]') # 특정 조건을 만족하는 요소들을 찾기
    # print(value, len(elements))

    # 추출한 요소들을 새로운 루트 요소에 추가
    for element in elements:
      # 요소 객체 자체를 추출 etree.tostring(element, pretty_print=True).decode('utf-8')
      # labels = etree.tostring(parent, pretty_print=True).decode('utf-8')
      # print(labels)
      parent = element.getparent() # 부모 객체 반환
      new_root.append(parent) # 루트 요소에 추가

  # 새로운 트리 생성
  new_tree = etree.ElementTree(new_root)

  # 새로운 XML 파일로 저장
  # new_tree.write('/content/extracted_elements.xml', pretty_print=True, xml_declaration=True, encoding="UTF-8")
  xml_code = etree.tostring(new_tree.getroot(), pretty_print=True).decode('utf-8')
  return xml_code
  # print(xml_code)

def remove_tags_by_attribute(input_file, output_file, tag, attribute, value):
    root = etree.fromstring(input_file) # str 타입의 xml 코드 받기
    tree = etree.ElementTree(root) # 객체를 생성
    # Find and remove elements with the specified tag and attribute value
    for val in value:
      for element in root.xpath(f'.//{tag}[@{attribute}="{val}"]'):
          parent = element.getparent()
          if parent is not None:
              parent.remove(element)

      # XPath를 사용하여 <name> 태그의 값이 val인 <label> 태그를 찾습니다
      labels_to_remove = root.xpath(f'.//label[name="{val}"]')
      # 찾은 <label> 태그를 부모 요소에서 제거합니다
      for label in labels_to_remove:
          parent = label.getparent()
          if parent is not None:
              parent.remove(label)

    # 수정된 XML을 출력
    # print(etree.tostring(root, pretty_print=True).decode('utf-8'))
    # Write the modified XML to the output file
    tree.write(output_file, encoding="utf-8", xml_declaration=True, pretty_print=True)



# 제거할 라벨 리스트
rm_label = ['bicycle', 'bus', 'carrier', 'cat',
            'dog', 'movable_signage', 'person', 'stroller',
            'wheelchair', 'barricade', 'bench', 'bollard',
            'chair', 'kiosk', 'parking_meter', 'pole',
            'potted_plant', 'power_controller', 'table',
            'traffic_light', 'traffic_light_controller',
            'traffic_sign', 'tree_trunk', 'scooter', 'fire_hydrant']

n = 6
path = f"E:/인도보행 영상/xml_label/box{n}/" # 파일 위의 경로까지
files = ['0729_13.xml', '0731_16.xml', '0801_23R.xml', '0731_21.xml']
#['0723_25.xml', '0725_24.xml', '0726_09.xml']
#['0718_06.xml', '0722_11.xml', '0722_36.xml'] # 파일 이름만
for file in files:
  value = ['truck', 'stop', 'motorcycle']
  xml_code = make_new_xml(path+file, value)


  tag = 'box'  # 제거하고자 하는 태그 이름
  attribute = 'label'  # 특정 속성
  value = rm_label # 특정 속성 값
  # if not os.path.exists(extracted_xml_dir):
  #         os.makedirs(extracted_xml_dir)
  output_file = f"E:/인도보행 영상/xml_label/output xml/output_{n}_{file}"
  remove_tags_by_attribute(xml_code, output_file, tag, attribute, value)


print('완료')