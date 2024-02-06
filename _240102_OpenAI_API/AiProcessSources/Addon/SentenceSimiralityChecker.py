# -*- coding: cp949 -*-
from sentence_transformers import SentenceTransformer
from math import sqrt, pow

def CheckSimilarity(str1, str2) : 
    sentences = [str1, str2]

    model = SentenceTransformer('snunlp/KR-SBERT-V40K-klueNLI-augSTS')
    model.encode
    embeddings = model.encode(sentences, convert_to_tensor=True)


    comparison_value = sqrt(sum(pow(a-b,2) for a, b in zip(embeddings[0], embeddings[1])))

    print(rf"'{str1}'와 '{str2}'간의 유사도 검사 결과 : {comparison_value}점 (낮을 수록 유사도 높음)")    

    return comparison_value


