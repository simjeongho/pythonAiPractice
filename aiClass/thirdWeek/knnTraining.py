from random import seed
import numpy as np
from sklearn.model_selection import train_test_split
#prepare data

fish_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0, 
                31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0, 
                35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0, 9.8, 
                10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
fish_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0, 
                500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0, 
                700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0, 6.7, 
                7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]
print(fish_length.__len__()) # 총 49개의 데이터
print(fish_weight.__len__()) # 총 49개의 데이터 
#column stack 사용법
a = np.column_stack(([1,2,3], [4,5,6]))
print(a);
fish_data = np.column_stack((fish_length, fish_weight));
print(fish_data);

# 범위 제한 사용법
print(fish_data[:9])
#ones 함수 사용
print(np.ones(5))
#concentrate함수 배열 합치기 데이터의 개수 49개 training data 와 test data로 나누기 위해 0과 1로 나눈다. 
fish_target = np.concatenate((np.ones(35), np.zeros(14)))
print(fish_target)

#Split the training set and test set with scikit-learn
# ai 를 학슴시킬 때는 training data, test data, validataion data가 존재해야함
input_Arr = np.array(fish_data);
target_Arr = np.array(fish_data);

#Data Shuffling 데이터가 편향되지 않도록 섞어준다. 1번 방법 인덱스를 섞어준다. 
np.random(seed(15));
index = np.arange(49); #Data의 개수 49개
np.random.shuffle(index);

#Create train set
train_input = input_Arr[index[:35]]
train_target = target_Arr[index[:35]]

#Create test set
test_input = input_Arr[index[35:]]
test_target = target_Arr[index[35:]]

#2번 방법 pip install --pre scikit-learn
#train_input, test_input, train_target, test_target = train_test_split(fish_data, fish_target, random_state=15);
