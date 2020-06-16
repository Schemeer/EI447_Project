from RecommandSys.models import *
from FinalProject.settings import VECTOR_DIR, WEIGHTS, BIAS, FIELDS
import numpy as np
import os
import copy

# get recommend using original field distribution
def get_score1(fields1, fields2):
    result = 0
    common_part = []
    # print(fields1, fields2)
    for i in fields1:
        for j in fields2:
            if i[0] == j[0]:
                common_part.append(i[0])
                result += abs(i[1]-j[1])
    for i in fields1:
        if i[0] not in common_part and i[0] != 0:
            result += i[1]
    for j in fields1:
        if j[0] not in common_part and j[0] != 0:
            result += j[1]
    return result

def get_recommend1(user_field, affiliation_abbr):
    all_author_field = eval(f"{affiliation_abbr}AuthorField").objects.all()
    all_parent_field = eval(f"{affiliation_abbr}ParentField").objects.all()
    score = []
    for author, parent in zip(all_author_field, all_parent_field):
        score.append([author.author_id, 0])
        field = []
        parent_field = []
        for i in range(1,6):
            field.append((getattr(author,f"field_id{i}"), getattr(author,f"weight{i}")))
        
        parent_field_tmp = parent.parents.rstrip("\r").rstrip(" ").split(" ")
        for j in range(0, len(parent_field_tmp), 2):
            if parent_field_tmp[j] != '' and int(parent_field_tmp[j])!=0 and j+1 < len(parent_field_tmp):
                parent_field.append((int(parent_field_tmp[j]), getattr(author, f"weight{int(parent_field_tmp[j+1])+1}")))
        score[-1][1] = 1 / (1 + (get_score1(user_field, field) + 0.1*get_score1(user_field, parent_field)))
    result = sorted(score, key=lambda x: x[0])
    return result

def get_a_vector(user_field):
    vec = np.zeros(45577, dtype=np.float16)
    for i in range(len(user_field)):
        if user_field[i][0] in FIELDS:
            field_index = FIELDS.index(user_field[i][0])
        vec[field_index] += user_field[i][1]
    return vec

def get_recommend2(user_field, affiliation_abbr):
    vec = get_a_vector(user_field)
    x = np.matmul(WEIGHTS.T, vec) + BIAS
    feature_vec = 1/(1+np.exp(-x))
    # print(feature_vec)
    authors = np.load(os.path.join(VECTOR_DIR, f"{affiliation_abbr}authorvector.npz"))
    author_features = authors["vector"]
    author_ids = authors["authorid"]
    score = []
    for author_feature, author_id in zip(author_features, author_ids):
        l2dist = np.linalg.norm(feature_vec - author_feature)
        sim = 1 / (1 + l2dist)
        score.append([author_id, sim])

    result = sorted(score, key=lambda x: x[0])
    return result

def get_recommend(user_field, affiliation_abbr, k):
    result1 = get_recommend1(user_field, affiliation_abbr)
    result2 = get_recommend2(user_field, affiliation_abbr)
    for i in range(len(result1)):
        result1[i][1] += result2[i][1]
    result = sorted(result1, key=lambda x: x[1], reverse=True)
    return result[:k]