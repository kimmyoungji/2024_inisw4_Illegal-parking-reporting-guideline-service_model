import zipfile
import os

for n in range(4,6):
    # zip 파일 경로
    zip_file_path = f"E:/인도보행 영상/바운딩박스/Bbox_{n}_new.zip"
    # XML 파일을 추출할 디렉토리 경로
    extracted_xml_dir = f"E:/인도보행 영상/xml_label/box{n}"
    # 추출할 디렉토리가 없으면 생성
    if not os.path.exists(extracted_xml_dir):
        os.makedirs(extracted_xml_dir)

    # zip 파일 열기
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        # zip 파일 내의 모든 파일 및 폴더 목록 가져오기 
        file_list = zip_ref.namelist()
        
        a = [file for file in file_list if f'{zip_file_path}/{file}'.endswith('.xml')]
        # ['Bbox_0148/0702_25.xml', 'Bbox_0149/0702_26.xml', 'Bbox_0150/0704_01.xml'] 이런 식
        # XML 파일 추출
        for xml_file in a:
            with open(extracted_xml_dir+'/'+xml_file[10:], 'wb') as efile:
                efile.write(zip_ref.read(xml_file))
print("완료되었습니다")