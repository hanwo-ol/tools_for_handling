


import os

def list_csv_files(folder_path):
  """
  지정된 폴더 내의 모든 CSV 파일 목록을 반환합니다.

  Args:
    folder_path: CSV 파일을 검색할 폴더의 경로입니다.

  Returns:
    폴더 내의 CSV 파일 이름 목록 (확장자 포함)입니다.  
    오류가 발생하거나 폴더가 존재하지 않으면 빈 리스트를 반환하고 오류 메시지를 출력합니다.
  """
  csv_files = []
  try:
    for filename in os.listdir(folder_path):
      if filename.endswith(".csv"):
        csv_files.append(filename)
  except FileNotFoundError:
    print(f"Error: Folder '{folder_path}' not found.")
    return []  #  빈 리스트 반환
  except Exception as e:
    print(f"An unexpected error occurred: {e}")
    return []
  return csv_files


# "stocks/tickers" 폴더 경로.  실제 경로로 바꿔주세요.
folder_path = "stocks/tickers"  # 상대 경로 예시
# folder_path = "/path/to/your/stocks/tickers" # 절대 경로 예시 (더 안정적)


csv_list = list_csv_files(folder_path)

if csv_list:
  print("CSV files in the folder:")
  for file in csv_list:
    print(file)
else:
  print("No CSV files found or folder does not exist.")
