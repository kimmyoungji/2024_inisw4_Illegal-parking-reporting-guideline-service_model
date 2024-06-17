import os
import random
import shutil
import json


# 저장 경로 선정
save_path = "E:/인도보행 영상"
train_path = save_path + '/train/'
val_path = save_path + '/val/'

# 폴더 없으면 생성
if not os.path.exists(save_path):
    os.makedirs(save_path)
if not os.path.exists(train_path):
    os.makedirs(train_path)
if not os.path.exists(val_path):
    os.makedirs(val_path)

# 이미지들이 있는 폴더, 새로 저장할 폴더
def split_files(folder_path, split_ratio=0.8):
    '''이미지를 train, val로 나누기 위해 랜덤으로 섞은 후 split'''
    # 폴더 내의 모든 jpg 파일 목록을 가져옴
    files = [f for f in os.listdir(folder_path) if f.endswith(".jpg")]

    # 파일 목록을 무작위로 섞음
    random.shuffle(files)

    # 파일을 나눌 인덱스 계산
    split_index = int(len(files) * split_ratio)

    # 파일 목록을 두 부분으로 나눔
    files1 = files[:split_index]
    files2 = files[split_index:]

    return files1, files2

def train_val_split_json(json_path):
    '''json을 train과 val로 나눠서 새로 만든다'''
    # JSON 파일을 읽어옴
    with open(json_path, 'r', encoding='utf-8') as file:
        js = json.load(file)
    tr, val = {}, {}
    for f in files1:
        tr[f] = js[f]
    for f in files2:
        val[f] = js[f]
    with open(os.path.join(train_path, 'input.json'), 'w') as file:
        json.dump(tr, file)
        print(f'train json이 저장되었습니다')
    with open(os.path.join(val_path, 'input.json'), 'w') as file:
        json.dump(val, file)
        print(f'val json이 저장되었습니다')

    
# 예제 폴더 경로
folder_path = "E:/인도보행 영상/sample_img"
# 파일 목록을 8:2로 랜덤하게 나눔
files1, files2 = split_files(folder_path)

print(len(files1), len(files2)) # 이미지 수 1049, 263
  
# 이미지 복붙  
for train in files1:
  shutil.copy(os.path.join(folder_path, train), train_path)
for val in files2:
  shutil.copy(os.path.join(folder_path, val), val_path)
  
print(len(os.listdir(os.path.join(save_path, train_path))), len(os.listdir(os.path.join(save_path, val_path))))

train_val_split_json("E:/인도보행 영상/sample_img/input.json")
print("완료")