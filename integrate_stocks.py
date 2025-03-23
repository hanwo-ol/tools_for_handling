import os
import pandas as pd
from tqdm import tqdm 

# 주가 정보 파일들이 저장된 디렉토리 경로
directory = 'stock_data' 

# 통합된 데이터를 저장할 빈 DataFrame 생성
all_data = pd.DataFrame()

# 디렉토리 내 모든 파일 목록을 가져옴
files = [f for f in os.listdir(directory) if f.endswith('.csv')]
num_files = len(files)  # 전체 파일 개수

# tqdm으로 파일 목록을 감싸서 progress bar를 표시
with tqdm(total=num_files, desc="Processing files") as pbar:  #전체, 설명
    for filename in files:
        filepath = os.path.join(directory, filename)

        # 파일 읽기 (1, 2번째 행 건너뛰기): 티커 정보가 담겨있는 행이어서 건너 뛰었음
        try:
            df = pd.read_csv(filepath, skiprows=2)
            # 컬럼 개수 검사 추가
            if len(df.columns) < 3:
                print(f"\nSkipping file {filename}: Insufficient columns.")
                pbar.update(1) #프로그래스바 업데이트
                continue

            df.columns = ['Date', 'Close', 'Volume'] # 컬럼명을 설정해줘야 함.

        except pd.errors.EmptyDataError:
            print(f"\nSkipping empty file: {filename}")
            pbar.update(1)
            continue  # 빈 파일은 건너뜁니다.
        except pd.errors.ParserError:
            print(f"\nSkipping file with parsing error: {filename}")
            pbar.update(1)
            continue
        except Exception as e:
            print(f"\nError reading file {filename}: {e}")
            pbar.update(1)
            continue

        # 필요한 컬럼만 선택 및 컬럼명 변경 (이미 위에서 컬럼명 변경)
        if 'Date' not in df.columns or 'Close' not in df.columns or 'Volume' not in df.columns:
          print(f"\nSkipping file {filename}: Missing required columns (Date, Close, Volume).")
          pbar.update(1)
          continue

        # 'Date' 컬럼을 datetime 객체로 변환, 에러 처리
        try:
            df['Date'] = pd.to_datetime(df['Date'])
        except ValueError:
            print(f"\nSkipping file {filename}: Invalid date format.")
            pbar.update(1)
            continue

        # Ticker (종목 코드) 정보 추가. 파일명에서 .csv 확장자 제거
        ticker = filename[:-4]
        df['Ticker'] = ticker

        # 통합 DataFrame에 추가
        all_data = pd.concat([all_data, df], ignore_index=True)
        pbar.update(1)  # 진행률 업데이트


# 결과 확인
print(all_data.head())
print(all_data.tail())
print(all_data.info())

# (선택 사항) 통합된 데이터를 .csv 파일로 저장
all_data.to_csv('integrated_stock_data.csv', index=False)
