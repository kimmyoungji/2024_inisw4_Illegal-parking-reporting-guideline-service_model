import zipfile
import os
import pandas as pd
import re

for n in range(4,7): # zip 박스 번호
    img_data = pd.read_csv("E:/인도보행 영상/xml_label/img_data.csv") # 수집한 이미지 이름
    # print(img_data.head())
    st = f'output_{n}'
    data= set(img_data.loc[img_data['folder_name'].str.startswith(st), 'img_name'])
    # print(len(data))
    # print(data)

    cnt = 0 
    
    
    # zip 파일 경로
    zip_file_path = f"E:/인도보행 영상/바운딩박스/Bbox_{n}_new.zip"
    # XML 파일을 추출할 디렉토리 경로
    extracted_xml_dir = f"E:/인도보행 영상/sample_img"
    # 추출할 디렉토리가 없으면 생성
    if not os.path.exists(extracted_xml_dir):
        os.makedirs(extracted_xml_dir)

    # zip 파일 열기
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        # zip 파일 내의 모든 파일 및 폴더 목록 가져오기 
        file_list = zip_ref.namelist()
        # print(file_list)
        
        for file in file_list:
            match = re.search(r'[/](\w+[.]jpg)', file) 
            if match is None:
                continue
            else:
                d = match.group(1) 
                if d in data:
                    with open(f'{extracted_xml_dir}/{d}', 'wb') as f:
                        f.write(zip_ref.read(file))
                    cnt += 1
        print(cnt)
        
print("완료되었습니다")