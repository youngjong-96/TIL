import pandas as pd
import numpy as np
from sklearn.datasets import load_wine
import matplotlib.pyplot as plt
import seaborn as sns

# sklearn에서 제공하는 data 나눠서 받아오기
df, y = load_wine(as_frame=True, return_X_y=True)
df['quality'] = y
# df.info()
# print(df.describe())

# Pandas 연습
# 1. 데이터셋에 포함된 와인의 총 샘플 수 구하기
sample_count = df.shape[0]
print("데이터 개수: " ,sample_count)

# 2. 데이터셋의 특성 수 구하기
feature_count = df.shape[1]
print('속성의 개수: ', feature_count)

# 3. quality는 어떤 범주가 있는지 구하기
class_count = df['quality'].nunique()
print('클래스 수: ', class_count)

# 4. quality 별 샘플 수 구하기 (0, 1, 2가 각각 몇 개인지)
class_distribution = df['quality'].value_counts().sort_index()
print('클래스별 샘플 갯수: ', class_distribution)

# 5. Alcohol의 평균값이 가장 높은 클래스를 구하기
top_alcohol_class = df.groupby('quality')['alcohol'].mean().idxmax()
print('알코홀 함량이 가장 높은 quality: ', top_alcohol_class)

# 8. color intensity가 10 이상인 샘플의 비용
# 필터 진행
filtered_df = df['color_intensity'] >= 10
# 원본에서 시리즈가 True인 애들만 뽑아서 샘플을 가져오기
high_color_samples = df[filtered_df]
# 전체에서 해당 갯수의 비율 구하기
high_color_ratio = len(high_color_samples) / len(df) * 100
print(f'high color ratio: {high_color_ratio:.2f}%')

# 10. Proline의 분포에서 가장 높은 피크를 가지는 클래스 번호 구하기
# 히스토그램
# df['proline'].hist(by=df['quality'], figsize=(10, 10), edgecolor='black', color='lightblue')
# plt.suptitle('Proline Distribution by Class')
# plt.show()


bins = 20   # 몇 개 단위로 데이터를 끊을지
global_min, global_max = df['proline'].min(), df['proline'].max()
peak_by_class = {}
for cls in df['quality'].unique():
    counts, _ = np.histogram(df.loc[df['quality'] == cls, 'proline'], bins=bins, range=(global_min, global_max))
    peak_by_class[int(cls)] = counts.max()

print(peak_by_class)
# {0: np.int64(12), 1: np.int64(14), 2: np.int64(13)}


# 12. Alcohol과 상관관계가 가장 높은 특성 구하기
alcohol_correlations = df.corr()['alcohol']
alcohol_correlations = alcohol_correlations.abs().sort_values(ascending=False)
print(alcohol_correlations)
top_corr_with_alcohol = alcohol_correlations.index[1]
print(top_corr_with_alcohol)
pro_al_corr = df['proline'].corr(df['alcohol'])
print(pro_al_corr)


# 전체 상관관계 시각화
# 모든 상관관계 저장
# corr = df.corr()

# fig, ax = plt.subplots(figsize=(10, 7))
# n = len(corr)
# mask = np.triu(np.ones((n, n)))
# sns.heatmap(data=corr, annot=True, fmt='.2f', cmap='coolwarm', mask=mask)
# ax.grid(False)
# ax.set_title('correlation between features')
# plt.show()


# Flavanoid 분포
# plt.figure(figsize=(6, 4))
# sns.histplot(data=df, x='flavanoids', bins=20, kde=True)
# plt.title('Flavanoids Distribution')
# plt.show()


# 산점도 그리기
# sns.scatterplot(data=df, x='flavanoids', y='total_phenols', hue='quality')
# plt.show()


# 결측치 탐지
# 1. 난수 고정
np.random.seed(42)

# 2. 결측치를 data에 억지로 넣기
df_missing = df.copy()
missing_idx = np.random.choice(df_missing.index, size=10, replace=False)
df_missing.loc[missing_idx, 'flavanoids'] = np.nan

# 3. heatmap으로 결측치 확인
# sns.heatmap(df_missing.isnull(), cbar=False)
# plt.title('visualize missing values')
# plt.show()


# 이상치 탐지
# 1. 이상치 생성
outlier_idx = np.random.choice(df_missing.index, size=5, replace=False)
df_missing.loc[outlier_idx, 'alcohol'] = df_missing['alcohol'].mean() * 5

# 2. 사분위(IQR) 범위로 이상치 탐지
# 전체 데이터를 구간별로 4등분 해서 가운데 2 구간의 크기를 IQR로 정의할 때
# 첫 번째 구간의 최댓값 - IQR * 1.5
# 세 번째 구간의 최솟값 + IQR * 1.5
# 를 벗어나는 데이터를 이상치로 판단
def detect_outlierss_iqr(data, column):
    # data = df, column = 'alcohol'
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return data[(data[column] < lower_bound) | (data[column] > upper_bound)]

outliers_alcohol = detect_outlierss_iqr(df_missing, 'alcohol')

# sns.boxplot(x=df_missing['alcohol'])
# plt.title('alcohol outliers')
# plt.show()

# 결측치는 평균값으로 대체
df_filled = df_missing.fillna(df_missing.mean(numeric_only=True))
print(df_filled.isnull().sum()) # null 이 있는지 확인

# 이상치 처리
# 1. 이상치 제거
df_no_outliers = df_filled[~df_filled.index.isin(outliers_alcohol.index)]
# outliers_alcohol = detect_outlierss_iqr(df_no_outliers, 'alcohol')

# 2. 평균값으로 대체
mean_alcohol = df_filled['alcohol'].mean()
df_filled.loc[outliers_alcohol.index, 'alcohol'] = mean_alcohol
outliers_alcohol = detect_outlierss_iqr(df_filled,'alcohol')
print('outliers_alcohol: ', outliers_alcohol)