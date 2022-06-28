from nltk.translate.bleu_score import sentence_bleu
from nltk.translate.meteor_score import meteor_score
import jieba
import nltk


def get_bleu_score(reference, candidate):
    reference = ''.join(jieba.cut(reference))
    candidate = ''.join(jieba.cut(candidate))
    score = sentence_bleu([reference], candidate)
    return score


def get_meteor_score(reference, candidate):
    # need vpn
    nltk.download('wordnet')
    # reference = ''.join(jieba.cut(reference))
    # candidate = ''.join(jieba.cut(candidate))
    score = meteor_score([reference], candidate, 4)
    return score


