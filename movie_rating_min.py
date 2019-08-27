import numpy as np
import pickle

from konlpy.tag import Okt
from scipy.sparse import lil_matrix
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression

"""
Req 1-1-1. 데이터 읽기
read_data(): 데이터를 읽어서 저장하는 함수
"""

def read_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = [line.split('\t') for line in f.read().splitlines()][1:]
    return data

"""
Req 1-1-2. 토큰화 함수
tokenize(): 텍스트 데이터를 받아 KoNLPy의 okt 형태소 분석기로 토크나이징
"""

pos_tagger = Okt()

def tokenize(doc):
    return ['/'.join(t) for t in pos_tagger.pos(doc, norm=True, stem=True)]

"""
데이터 전 처리
"""

# train, test 데이터 읽기
train_data = read_data('ratings_train.txt')
test_data = read_data('ratings_test.txt')

# Req 1-1-2. 문장 데이터 토큰화
# train_docs, test_docs : 토큰화된 트레이닝, 테스트  문장에 label 정보를 추가한 list
train_docs = [(tokenize(row[1]), row[2]) for row in train_data]
test_docs = [(tokenize(row[1]), row[2]) for row in test_data]

# Req 1-1-3. word_indices 초기화
word_indices = {}

# Req 1-1-3. word_indices 채우기
for vocas in train_docs:
    for voca in vocas[0]:
        text = voca.split('/')[0]
        if text not in word_indices:
            word_indices[text] = len(word_indices)

print(word_indices)
    # if voca not in word_indices.keys():
    #     word_indices[voca]=len(word_indices)

# print(word_indices)
# train_tokens = [t for d in train_docs for t in d]

# Req 1-1-4. sparse matrix 초기화
# X: train feature data
# X_test: test feature data
X = None
X_test = None

# 평점 label 데이터가 저장될 Y 행렬 초기화
# Y: train data label
# Y_test: test data label
Y = None
Y_test = None