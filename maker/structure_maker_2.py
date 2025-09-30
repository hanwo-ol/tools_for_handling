
import os

def generate_fancy_directory_tree(dir_path, prefix="", max_files=3):
    """
    주어진 경로의 디렉토리 구조를 선 장식을 포함한 문자열로 생성합니다.
    폴더 당 최대 파일 수를 제한할 수 있습니다.

    :param dir_path: 탐색을 시작할 폴더 경로
    :param prefix: 트리 라인을 그리기 위한 접두사
    :param max_files: 각 폴더에 표시할 최대 파일 수
    """
    try:
        # 접근 권한이 없는 폴더 등을 처리하기 위한 예외 처리
        items = os.listdir(dir_path)
    except PermissionError:
        return prefix + "└── [접근 불가]\n"
    
    # 폴더와 파일을 분리합니다.
    dirs = sorted([d for d in items if os.path.isdir(os.path.join(dir_path, d))])
    files = sorted([f for f in items if os.path.isfile(os.path.join(dir_path, f))])
    
    # 파일 개수를 제한합니다.
    limited_files = files[:max_files]
    files_omitted = len(files) > max_files
    
    entries = dirs + limited_files
    if files_omitted:
        # 생략된 파일이 있으면 '...' 항목을 추가합니다.
        entries.append('...')
        
    tree_string = ""

    for i, entry in enumerate(entries):
        # 마지막 항목인지 확인하여 선 모양을 결정합니다.
        connector = "└── " if i == len(entries) - 1 else "├── "
        
        # 파일/폴더 아이콘 추가
        if entry in dirs:
            icon = "📁"
        elif entry == '...':
            icon = "" # 아이콘 없음
            connector = "└── " # 생략 표시는 항상 마지막처럼 처리
        else:
            icon = "📄"
        
        tree_string += f"{prefix}{connector}{icon} {entry}\n"

        # 해당 항목이 폴더라면 재귀적으로 함수를 호출합니다.
        if entry in dirs:
            new_prefix = prefix + ("    " if i == len(entries) - 1 else "│   ")
            tree_string += generate_fancy_directory_tree(
                os.path.join(dir_path, entry), new_prefix, max_files
            )
            
    return tree_string

if __name__ == "__main__":
    # 현재 스크립트가 실행되는 폴더를 기준으로 구조도를 생성합니다.
    current_directory = os.getcwd()
    
    # 출력할 최대 파일 개수 설정 (예: 3개)
    MAX_FILES_PER_FOLDER = 5
    
    print(f"📁 {os.path.basename(current_directory)} (폴더 당 최대 {MAX_FILES_PER_FOLDER}개 파일 표시)")
    tree_view = generate_fancy_directory_tree(current_directory, max_files=MAX_FILES_PER_FOLDER)
    print(tree_view)
