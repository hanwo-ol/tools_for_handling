import os

def generate_fancy_directory_tree(dir_path, prefix=""):
    """
    주어진 경로의 디렉토리 구조를 선 장식을 포함한 문자열로 생성합니다.
    """
    # 폴더 내의 항목들을 리스트로 가져옵니다.
    files = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]
    dirs = [d for d in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, d))]
    
    entries = dirs + files
    tree_string = ""

    for i, entry in enumerate(entries):
        # 마지막 항목인지 확인하여 선 모양을 결정합니다.
        connector = "└── " if i == len(entries) - 1 else "├── "
        tree_string += prefix + connector + entry + "\n"

        # 해당 항목이 폴더라면 재귀적으로 함수를 호출합니다.
        if entry in dirs:
            new_prefix = prefix + ("    " if i == len(entries) - 1 else "│   ")
            tree_string += generate_fancy_directory_tree(os.path.join(dir_path, entry), new_prefix)
            
    return tree_string

if __name__ == "__main__":
    # 현재 스크립트가 실행되는 폴더를 기준으로 구조도를 생성합니다.
    current_directory = os.getcwd()
    print(f"📁 {os.path.basename(current_directory)}")
    tree_view = generate_fancy_directory_tree(current_directory)
    print(tree_view)
