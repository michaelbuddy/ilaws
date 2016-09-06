#!/usr/bin/env python
#-*-coding=utf-8-*-
import codecs 
"""
     原始数据，用于建立模型
"""
#缩水版的courses，实际数据的格式应该为 课程名\t课程简介\t课程详情，并已去除html等干扰因素
courses = [
u'a long-term contract 长期合同 a short-term contract 短期合同 a nice fat contract 一个很有利的合同 a written contract 书面合同 an executor contract 尚待执行的合同 breach of contract 违反合同 cancellation of contract 撤消合同 completion of contract 完成合同 contract for future delivery', 
u'期货合同 contract for goods 订货合同 contract for purchase 采购合同 contract for service 劳务合同 contract law 合同法 contract life 合同有效期 contract note 买卖合同（证书）',
u'了解和掌握英文合同的词汇特点是正确理解英文合同、书写英文合同乃至翻译英文合同的前提之一',
u' 关键词：英文合同 词汇 特点 引言 随着世界经济一体化进程的不断推进，中国融入国际社会步伐的加快，对外交往 日益密切，与国外经济、技术、文化交流日趋频繁，英语合同的应用越发广泛',
u'人们订立合同的目的是 确认合同各方应尽的义务及应享受的权利，合同一经依法订立，就成为一种具有约束力的法律文件，成 为预防和解决争议的法律依据',
u'要做到正确地理解和书写英文合同，首先必须了解它的用词特点',
u'合同 语言属于法律语言，英文合同在语言上力求用词严谨，表述准确，尽量避免可能出现的对合同内容或条 款的误解或曲解，确保合同的严谨性、准确性和权威性',
u'因此，英语合同的用词具有准确、严谨、正式、 庄重和保守等特征，具体体现在以下几个方面： 1.使用情态动词 英文合同的用词一般都是正式、规范的语言，情态动词的使用就体现了这一特点',
u'英 文合同中常见的情态动词主要有以下两个，即，shall 和 should',
u'但它们在合同中分别表示不同的含义',
u'shall 是英文合同中使用频率最高的一个词，也是语气最重的一个词，常用于第三人称',
u'shall 常用来表 示法律上必须履行的责任和应尽的义务，如不履行合同条款就会产生违反法律责任和义务的后果，其含 义相当于中文的“应当”或“必须”',
u'例如：1.The Seller shall present the following documents required for negotiation to the banks（卖方必须将下列单据提交银行附议）.shall 的否定形式 shall not 在英文合同 中常表示不得发生的行为',
u' 例如：2. Party A shall not supply the contracted commodity to other buyers in the above-mentioned territory（甲方不得向上述地区其他买主供应本合同项下商品）',
u'但必须注意的 是，在英文合同中，shall 在表示“应该”时不可随便用 should 代替，should 虽然也表示“应该”，但它没有 shall 那样重的含义，因为 should 并不表示法律义务，只表示一般的义务或道义上的义务，有时甚至表 示“原该”或“最好如此”的含义',
u'当 should 出现在合同中时，它常放在句子的开头，表示一个隐含的条件 状语，相当于由 if、in case 或 in the event that 引导的状语从句，其含义相当于中文的“如果”、“万一” 而不是“应该”',
u'例如：3. Should the verification conclusion contradict the conditions of an auction target stated in an auction contract, the auctioneer has the right to demand a change or rescind the contract （如果鉴定结论与委托拍卖合同载明的拍卖标的状况不相符，拍卖人有权要求变更或者解除合同）',
u'此 外，英文合同中有时也出现情态动词 may 和 must',
u'may 用于约定当事人的权利（可以做什么）,没有 任何义务的含义，不带有强制性，有时表示允许或许可，相当于中文的“可以”、“得”等含义',
u'其否定形式 may not 用于禁止性义务（不得做什么），语气不如 shall not 强烈',
u'must 用于强制性义务（必须做什 么），但这一义务不一定具有法律的约束力，其否定形式一般不会出现在英文合同中',
u'了解和掌握情态 动词的确切含义有助于正确理解英文合同条款的内容',
u'由于合同中权利和义务的约定构成了合同的主 体，情态动词如选用不当，有可能会引起法律纠纷',
u' 2.使用古体词和外来词 为体现合同文本行为正式、庄重的文体特征，英文合同常使用一些古体词',
u'这些 词主要来源于古英语和中古英语，主要是由 here-，there-和 where- 与一个或几个介词组成的复合副词， 如 hereafter(此后，今后), hereby(特此，兹), herein(此中，于此，本合同中)，hereinafter(以下，此后， 在下文), hereof(于此，在本合同中), hereto (于此)，hereunder(在下文，据此，根据本合同)，hereunto （于此）, herewith（与此一道），thereafter（此后，后来）thereby (因此，由此，在那方面), therefrom （由此、从此），therein（其中，在其中），thereinafter（在下文），thereof（关于、由此，其中）， thereto（此外，附随），thereunder（在其下，据此、依据）, whereas（鉴于），whereby(因此,由是， 据此)，wherefore（为此，因此）,wherein（在那方面），whereof(关于那事/人)等',
u'在这些复合副词中， here 表示 this，there 表示 that，where 表示 what 或 which',
u'英文合同中使用这些词能使语言精练、直 观,使合同语言显得更为规范、严肃，显示合同语言的权威性和严密性',
u'例如：4.The parties hereto shall, first of all, settle any dispute arising from or in connection with the contract through amicable negotiations（合同双方首先应通过友好协商， 解决因合同而发生的或与合同有关的争议）',
u'此句中的 hereto 表示上文已提及的内容，即，to this contract',
u'这类词的使用使句子简练、严密，构成合同语言的保守性和稳定性，体现合同文本正式、庄 重的文体特征',
]

f = codecs.open(u'data/合同文本.txt', 'r','utf-8')              #文件为123.txt
sourceInLines = f.readlines()  #按行读出文件内容
f.close()
str=''
new = []                                   #定义一个空列表，用来存储结果
for line in sourceInLines:
   # print line
    temp1 =   line.replace("\n",",")         #去掉每行最后的换行符'\n'
    new.append(temp1)
    
#print new

#只是为了最后的查看方便
#实际的 courses_name = [course.split('\t')[0] for course in courses]
#courses_name = courses

courses_name = courses


"""
    预处理(easy_install nltk)
"""
def pre_process_cn(courses, low_freq_filter = True):
    """
     简化的 中文+英文 预处理
        1.去掉停用词
        2.去掉标点符号
        3.处理为词干
        4.去掉低频词

    """
    import nltk
    import jieba.analyse
    from nltk.tokenize import word_tokenize
   
    texts_tokenized = []
    for document in courses:
        texts_tokenized_tmp = []
        for word in word_tokenize(document):
            texts_tokenized_tmp += jieba.analyse.extract_tags(word,10)
        texts_tokenized.append(texts_tokenized_tmp)   
   
    texts_filtered_stopwords = texts_tokenized

    #去除标点符号
    english_punctuations = [',', '.', ':', ';', '?', '(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%']
    texts_filtered = [[word for word in document if not word in english_punctuations] for document in texts_filtered_stopwords]

    #词干化
    from nltk.stem.lancaster import LancasterStemmer
    st = LancasterStemmer()
    texts_stemmed = [[st.stem(word) for word in docment] for docment in texts_filtered]
   
    #去除过低频词
    if low_freq_filter:
        all_stems = sum(texts_stemmed, [])
        stems_once = set(stem for stem in set(all_stems) if all_stems.count(stem) == 1)
        texts = [[stem for stem in text if stem not in stems_once] for text in texts_stemmed]
    else:
        texts = texts_stemmed
    return texts

lib_texts = pre_process_cn(courses)



"""
    引入gensim，正式开始处理(easy_install gensim)
"""

def train_by_lsi(lib_texts):
    """
        通过LSI模型的训练
    """
    from gensim import corpora, models, similarities

    #为了能看到过程日志
    #import logging
    #logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

    dictionary = corpora.Dictionary(lib_texts)
    corpus = [dictionary.doc2bow(text) for text in lib_texts]     #doc2bow(): 将collection words 转为词袋，用两元组(word_id, word_frequency)表示
    tfidf = models.TfidfModel(corpus)
    corpus_tfidf = tfidf[corpus]

    #拍脑袋的：训练topic数量为10的LSI模型
    lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=10)
    index = similarities.MatrixSimilarity(lsi[corpus])     # index 是 gensim.similarities.docsim.MatrixSimilarity 实例
   
    return (index, dictionary, lsi)

   
#库建立完成 -- 这部分可能数据很大，可以预先处理好，存储起来
(index,dictionary,lsi) = train_by_lsi(lib_texts)
   
   
#要处理的对象登场
target_courses = [u'should']
target_text = pre_process_cn(target_courses, low_freq_filter=False)


"""
对具体对象相似度匹配
"""

#选择一个基准数据
ml_course = target_text[0]

#词袋处理
ml_bow = dictionary.doc2bow(ml_course)  

#在上面选择的模型数据 lsi 中，计算其他数据与其的相似度
ml_lsi = lsi[ml_bow]     #ml_lsi 形式如 (topic_id, topic_value)
sims = index[ml_lsi]     #sims 是最终结果了， index[xxx] 调用内置方法 __getitem__() 来计算ml_lsi

#排序，为输出方便
sort_sims = sorted(enumerate(sims), key=lambda item: -item[1])

#查看结果
print sort_sims[0:10]   #看下前10个最相似的，第一个是基准数据自身
print courses_name[sort_sims[1][0]]   #看下实际最相似的数据叫什么
print courses_name[sort_sims[2][0]]   #看下实际最相似的数据叫什么
print courses_name[sort_sims[3][0]]   #看下实际最相似的数据叫什么
