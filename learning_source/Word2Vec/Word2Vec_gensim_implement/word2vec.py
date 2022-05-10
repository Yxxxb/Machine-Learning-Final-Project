import gensim
import logging
import multiprocessing
import os
import re
import sys
import scipy
from gensim.models import word2vec
import numpy as np
from time import time
from sklearn.metrics.pairwise import cosine_similarity
from evaluation import evalu
import json
from torch.utils.tensorboard import SummaryWriter

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',
                    level=logging.INFO)

#训练过程函数化，传入参数，返回模型训练评估score
def trainWord2Vec(index,saved=True,vector_size=200,window=10,min_count=10,negative=10,sg=0,hs=0):
    print("### index:", index, " vector_size:", vector_size, " window:", window, " min_count:", min_count, " negative:",negative)
    model = gensim.models.word2vec.Word2Vec(
                sents,
                vector_size=vector_size,
                window=window,
                min_count=min_count,
                sg=sg,  # 0 -- CBOW 1 -- skip-gram
                hs=hs,  # 0 -- negative sampling 1 -- hierarchica-softmax
                negative=negative,  # >0 -- negative sampling
                workers=multiprocessing.cpu_count()
        )

    # saving to file
    if saved:
        model.save("word2vec_gensim")
        model.wv.save_word2vec_format("word2vec_org","vocabulary",binary=False)

    #evaluate
    sims = []
    gt = []
    with open('wordsim353/combined.csv') as f:
        for line in f.readlines()[1:]:
            l = line.strip().split(',')
            if l[0] in model.wv and l[1] in model.wv:  # 过滤掉不在词表内的词
                sims.append(model.wv.similarity(l[0], l[1]))  # 模型打分
                gt.append(l[2])  # ground truth 提取

    np.save('score.npy', np.array(sims))
    np.save('ground_truth.npy', np.array(gt))
    tmp = evalu(["evaluate.py", "score.npy"])
    #print(json.dumps(tmp))
    return tmp["score"]

if __name__ == '__main__':

    data_path = 'text8'#导入训练集

    # loading dataset
    sents = word2vec.Text8Corpus('text8')#处理数据集

    t = time()
    score=trainWord2Vec(0)
    print(score)
    print("Total time: %d s" % (time() - t))


    # writer = SummaryWriter("tb_logs/parameter_fit")
    #
    # index=0
    # for vector_size in range(100,501,10):
    #     print("########## vector_size index")
    #     score=trainWord2Vec(index=index,vector_size=vector_size)
    #     writer.add_scalar("Vector_Size", score, vector_size)
    #     index+=1
    #
    # index = 0
    # for window in range(3, 21, 1):
    #     print("########## window index")
    #     score = trainWord2Vec(index=index, window=window)
    #     writer.add_scalar("Window", score, window)
    #     index += 1
    #
    # index = 0
    # for min_count in range(5, 21, 1):
    #     print("########## min_count index")
    #     score = trainWord2Vec(index=index, min_count=min_count)
    #     writer.add_scalar("Min_Count", score, min_count)
    #     index += 1
    #
    # writer.close()

    # # training word2vec
    # vector_size = 150
    # window = 11
    # min_count = 7
    # negative = 8
    # print("### vector_size:",vector_size," window:",window," min_count:",min_count," negative:",negative)
    # model = gensim.models.word2vec.Word2Vec(sents,
    #                                vector_size=vector_size,
    #                                window=window,
    #                                min_count=min_count,
    #                                sg=0, # 0 -- CBOW 1 -- skip-gram
    #                                hs=0, # 0 -- negative sampling 1 -- hierarchica-softmax
    #                                negative=negative, # >0 -- negative sampling
    #                                workers=multiprocessing.cpu_count())
    #
    # # saving to file
    # model.save("word2vec_gensim")
    # model.wv.save_word2vec_format("word2vec_org",
    #                               "vocabulary",
    #                               binary=False)
    #
    # print ("Total time: %d s" % (time() - t))
    #
    # model=gensim.models.word2vec.Word2Vec.load("word2vec_gensim")
    #
    # # testing on wordsim353
    # sims = []
    # gt=[]
    # with open('wordsim353/combined.csv') as f:
    #     for line in f.readlines()[1:]:
    #         l = line.strip().split(',')
    #         if l[0] in model.wv and l[1] in model.wv: # 过滤掉不在词表内的词
    #             sims.append(model.wv.similarity(l[0], l[1])) # 模型打分
    #             gt.append(l[2])  # ground truth 提取
    # #print("gensim:{}".format(model.wv.similarity("tiger","cat")))
    # #print("scipy:{}".format(scipy.spatial.distance.cosine(model.wv["tiger"], model.wv["cat"]) ))
    # #print("sklearn:{}".format(cosine_similarity(np.array(model.wv["tiger"]).reshape(1,-1), np.array(model.wv["cat"]).reshape(1,-1))[0][0]))
    #
    # np.save('score.npy', np.array(sims))
    # np.save('ground_truth.npy', np.array(gt))
    # tmp=evalu(["evaluate.py", "score.npy"])
    # print(json.dumps(tmp))


