import pandas as pd

# DataFrame
data = {
    'Name': ['Alex', 'Brad', 'Chad'],
    'Age': [25, 30, 35],
    'Score': [55.5, 90.3, 78.9],
}
df = pd.DataFrame(data)
print(df)
"""
   Name  Age  Score
0  Alex   25   55.5
1  Brad   30   90.3
2  Chad   35   78.9
"""

# series - 데이터프레임의 열(속성, 컬럼)
name_series = df['Name']
print(name_series)
"""
0    Alex
1    Brad
2    Chad
Name: Name, dtype: object
"""

# record - 데이터프레임의 행
print(df.iloc[0])  # index_location
"""
Name     Alex
Age        25
Score    55.5
Name: 0, dtype: object
"""

print(df.iloc[1, 2]) # 1행 2열의 데이터 >>> 90.3
print(df.loc[0, 'Name']) # 0행의 'Name' 속성 >>> Alex

# 여러 열을 추출
print(df[['Name', 'Score']])
"""
   Name  Score
0  Alex   55.5
1  Brad   90.3
2  Chad   78.9
"""



# 정보 찾아보기
df.info()
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 3 entries, 0 to 2
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   Name    3 non-null      object
 1   Age     3 non-null      int64
 2   Score   3 non-null      float64
dtypes: float64(1), int64(1), object(1)
memory usage: 204.0+ bytes
"""

# 상세 요약
print(df.describe())
"""
        Age      Score
count   3.0   3.000000
mean   30.0  74.900000
std     5.0  17.741477
min    25.0  55.500000
25%    27.5  67.200000
50%    30.0  78.900000
75%    32.5  84.600000
max    35.0  90.300000
"""

print(df.shape) # 배열 크기 >>> (3, 3)
print(df.columns.tolist())  # colums 들을 리스트로 변환 >>> ['Name', 'Age', 'Score']
print(df.index)  # 인덱스 볌위 >>> RangeIndex(start=0, stop=3, step=1)
# 상위 일부 가져오기
print(df.head(2))
"""
Name  Age  Score
0  Alex   25   55.5
1  Brad   30   90.3
"""

# 집계 기능
print(df['Score'].mean())   # 점수의 평균  >>> 74.9
print(df['Age'].max())      # 나이의 최댓값  >>> 35
print(df.sort_values(by='Age'))    # 나이 순 정렬
"""
   Name  Age  Score
0  Alex   25   55.5
1  Brad   30   90.3
2  Chad   35   78.9
"""


# 다양한 타입의 데이터를 활용하여 DataFrame 만들기
# 1. 여러 딕셔너리에서 만들기 - 각 딕셔너리가 레코드라고 생각하고 리스트로
alex = {'Name': 'Alex', 'Age': 25, 'Score': 85.5}
brad = {'Name': 'Brad', 'Age': 30, 'Score': 90.3}
chad = {'Name': 'Chad', 'Age': 35, 'Score': 78.9}
df_from_dict = pd.DataFrame([alex, brad, chad])
print(df_from_dict)

# 2. 여러 리스트에서 만들기 - 딕셔너리처럼 하는데 속성명을 몰라서 따로 인자로 전달
alex = ['Alex', 25, 85.5]
brad = ['Brad', 30, 90.3]
chad = ['Chad', 35, 78.9]
df_from_list = pd.DataFrame([alex, brad, chad], columns=['Name', 'Age', 'Score'])
print(df_from_list)

# 3. numpy array 에서 만들기
import numpy as np
nums = np.array([
    [25, 85.5],
    [30, 90.3],
    [35, 78.9],
])
names = ['Alex', 'Brad', 'Chad']

# 일단 나이와 점수로 DataFrame 만들기
df_from_nparr = pd.DataFrame(nums, columns=['Age', 'Score'])
# 0 번에 이름 추가하기
df_from_nparr.insert(0, 'Name', names)

# 시리즈 형변환
df_from_nparr['Score'] = df_from_nparr['Score'].astype(int)
print(df_from_nparr)
"""
   Name   Age  Score
0  Alex  25.0     85
1  Brad  30.0     90
2  Chad  35.0     78
"""