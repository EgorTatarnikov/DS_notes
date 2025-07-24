#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas

# из sklearn.neighbors импортируйте алгоритм KNeighborsClassifier
from sklearn.neighbors import KNeighborsClassifier

# импортируйте метрику доли правильных ответов accuracy_score из sklearn.metrics
from sklearn.metrics import accuracy_score 


# In[2]:


train_data = pandas.read_csv('Train.csv') # прочитайте данные кофейной компании для обучения и сохраните в переменную train_data
test_data = pandas.read_csv('Test.csv') # прочитайте данные кофейной компании для теста и сохраните в переменную test_data

#print(train_data.to_string())
print(train_data)
#print(test_data.to_string())
print(test_data)


# In[3]:


X_train = train_data.drop('Segmentation', axis=1) # подготовьте обучающую выборку и сохраните в переменную X_train
y_train = train_data['Segmentation']# сохраните целевую переменную в y_train

X_test = test_data.drop('Segmentation', axis=1) # подготовьте тестовую выборку и сохраните в переменную X_test
y_test = test_data['Segmentation']# сохраните целевую переменную в y_test

print("Размер обучающей выборки X_train:", X_train.shape) # выведите на экран размер обучающей выборки
print("Размер целевой переменной y_train:", y_train.shape) # выведите на экран размер целевой переменной на обучении
print("Размер тестовой выборки X_test:", X_test.shape) # выведите на экран размер тестовой выборки
print("Размер целевой переменной y_test:", y_test.shape) # выведите на экран размер целевой переменной на тесте


# In[4]:


# вызовите алгоритм KNeighborsClassifier со значением 30 у параметра n_neighbors
knn = KNeighborsClassifier(n_neighbors=30) 

print(knn) # выведите на экран модель KNeighborsClassifier


# In[5]:


# обучите модель по обучающей выборке классифицировать классы
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test) # запустите модель строить прогнозы на тестовой выборке

print(y_pred) # выведите на экран получившиеся предсказания


# In[6]:


# подсчитайте долю правильных ответов предсказанных значений целевой переменной с истинными ответами на тестовой выборке
accuracy = accuracy_score(y_test, y_pred)

print("Доля правильных ответов:", accuracy) # выведите на экран получившиеся предсказания

