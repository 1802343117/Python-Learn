# coding:utf-8
"""
中文文本的情感分析
"""

from snownlp import SnowNLP

text = '十年可见春去秋来，百年可证生老病死；千年可叹王朝更替，万年可见斗转星移；凡人如果用一天的视野，去窥探百万年的天地，是否就如同井底之蛙'
s = SnowNLP(text)
# 分词
print(s.words)
# 词性标注
tags = [x for x in s.tags]
print(tags)
# 断句
print(s.sentences)
# 拼音
print(s.pinyin)

# 情绪判断，返回值为正面情绪的概率，越接近1表示正面情绪，越接近0表示负面情绪
text1 = '有些人没有见过汪洋，以为江河最为壮美；而有些人，通过一片落叶，却能看到整个秋天。行万里路，才能见天地之广阔。'
text2 = '何为人，顶天立地的异兽'
s1 = SnowNLP(text1)
s2 = SnowNLP(text2)
# 这部电影真心棒，0.9959750990466912
print(text1, s1.sentiments)
# 这部电影简直烂到爆，0.0566960891729531
print(text2, s2.sentiments)

# 关键字抽取
text3 = '辛苦却舒爽，这就是做人的滋味'
s3 = SnowNLP(text3)
print(s3.keywords(limit=5))
# 概况总结文章
print(s3.summary(limit=4))