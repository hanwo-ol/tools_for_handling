import os
import pandas as pd

# 주가 정보 파일들이 저장된 디렉토리 경로
directory = 'stock_data'  

# 통합된 데이터를 저장할 빈 DataFrame 생성
all_data = pd.DataFrame()

# 디렉토리 내 모든 파일에 대해 반복
for filename in os.listdir(directory):
    if filename.endswith('.csv'):  # .csv 파일만 처리
        filepath = os.path.join(directory, filename)

        # 파일 읽기 (1, 2번째 행 건너뛰기)
        df = pd.read_csv(filepath, skiprows=2)

        # 필요한 컬럼만 선택 및 컬럼명 변경
        #df = df[['Date', 'Close', 'Volume']]
        df.columns = ['Date', 'Close', 'Volume']

        # 'Date' 컬럼을 datetime 객체로 변환
        df['Date'] = pd.to_datetime(df['Date'])
        
        # Ticker (종목 코드) 정보 추가.  파일명이 "XXXX.YY.csv" 형식이면, '.' 로 분리후 앞의 두개요소를 가져와서 합침.
        ticker = ".".join(filename.split('.')[:2])
        df['Ticker'] = ticker
        
        # 통합 DataFrame에 추가
        all_data = pd.concat([all_data, df])

# 결과 확인
print(all_data.head())
print(all_data.tail())
print(all_data.info())

# (선택 사항) 통합된 데이터를 .csv 파일로 저장
all_data.to_csv('integrated_stock_data.csv', index=False)
