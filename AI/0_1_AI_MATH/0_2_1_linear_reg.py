import seaborn as sns
import numpy as np
import pandas as pd

# 

df = sns.load_dataset('diamonds')   # seaborn에 있는 여러 샘플 데이터셋 중 diamonds 가져오기
# 정보 확인
df.info()
print(df.describe())
print(df)

# 범주형 변수, 연속형 변수 구분
# category로 나누어진 데이터와 숫자형(연속적인) 데이터를 가진 속성을 분류
categorical_cols = df.select_dtypes(include=['category']).columns.tolist()
continuous_cols = df.select_dtypes(include=['number']).columns.tolist()
print(categorical_cols)
print(continuous_cols)

# 연속형 변수들만 뽑아저 저장
X_raw = df[continuous_cols].values

# 해당 변수들의 평균을 구한다
mu = X_raw.mean(axis=0)

# 해당 변수들의 표준편차를 구한다
std = X_raw.std(axis=0)

# 표준편차가 0일 경우 다른 값으로 변경한다
# 1. 1로 변경
std = np.where(std == 0, 1.0, std)
# 2. 영향이 없을 정도로 작은 값으로 변경
epsilon = 1e-8
std = np.where(std == 0, epsilon, std)

# 표준화된 X 값들을 구한다
X_norm = (X_raw - mu) / std
print(X_norm)

# 정규방정식으로 theta 만들기
# 계산의 편의를 위해 X_norm을 DataFrame으로 변경
X_df = pd.DataFrame(X_norm, columns=continuous_cols)

# feature와 label의 분리
X = X_df.drop(labels='price', axis=1).values
y = X_df['price'].values

# 절편항을 추가
m, n = X_norm.shape
X_b = np.c_[np.ones((m, 1)), X_norm]





# 정규방정식 계산
XT_X = X_b.T @ X_b
XT_Y = X_b.T @ y

# np.linalg.inv를 통해 theta 구하기
theta = np.linalg.inv(XT_X) @ XT_Y

# 시각화 함수
def plot_prediction(y_true, y_pred):
    y_true = y_true.flatten()
    y_pred = y_pred.flatten()
    assert y_true.shape == y_pred.shape, f"Size mismatch between y_true and y_pred"
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(6, 4))

    # 회귀선
    sns.scatterplot(x=y_true, y=y_pred,
                    alpha=0.5, label="Model Prediction", ax=ax)

    # 이상적인 예측선
    sns.lineplot(x=[y.min(), y.max()],
                 y=[y.min(), y.max()],
                 label="Ideal Regression", linestyle="--", color="red")

    ax.set_xlabel('Actual Price')
    ax.set_ylabel('Predicted Price')
    ax.set_title('Actual vs Predicted Price')
    fig.tight_layout()
    plt.show()

### 1 ###
# 예측값 만들기
y_pred = X_b @ theta
# MSE 계산
mse = np.mean((y_pred - y) ** 2)
plot_prediction(y_true=y, y_pred=y_pred)

### 2 ###
# 최소제곱법
theta_listsq, _, _, _ = np.linalg.lstsq(X_b, y, rcond=None)
y_pred = X_b @ theta_listsq
plot_prediction(y, y_pred)

### 3 ###
# SVD (Singular Vector Decomposition)
U, S, Vt = np.linalg.svd(X_b, full_matrices=False)
# 의사 역행렬 구하기
s_plus = np.diag(1.0 / S)
# theta 계산
theta_svd = Vt.T @ s_plus @ U.T @ y

y_pred = X_b @ theta_svd
plot_prediction(y, y_pred)