import os

# 파일 읽기
def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        html_text = f.read()
        print(f"{file_path} 파일 읽기 완료")
    return html_text

# 지정된 폴더가 없으면 생성하고 파일을 저장하는 함수
def save_data_overwrite(data, foldername, filename):
    current_dir = os.getcwd()    
    folder_path = os.path.join(current_dir, foldername)
    file_path = os.path.join(folder_path, filename)
    
    # 폴더가 없으면 생성
    os.makedirs(folder_path, exist_ok=True)

    # 파일 저장
    with open(file_path, "w", encoding="utf-8") as f:
        if isinstance(data, list):
            f.write("\n".join(data))
        else:
            f.write(data)  # 문자열인 경우 바로 저장
        print(f"{file_path} 파일로 저장되었습니다.")