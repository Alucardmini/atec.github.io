## From Word Embeddings To Document Distances
根据词语成分计算文档相似度

### 摘要

We present the Word Mover’s Distance (WMD), a novel distance function between text documents. Our work is based on recent results in word embeddings that learn semantically meaningful representations for words from local cooccurrences in sentences. The WMD distance measures the dissimilarity between two text documents as the minimum amount of distance that the embedded words of one document need to “travel” to reach the embedded words of another document. We show that this distance metric can be cast as an instance of the Earth Mover’s Distance, a well studied transportation problem for which several highly efficient solvers have been developed. Our metric has no hyperparameters and is straight-forward to implement. Further, we demonstrate on eight real world document classi- fication data sets, in comparison with seven state- of-the-art baselines, that the WMD metric leads to unprecedented low k-nearest neighbor docu- ment classification error rates.
本文提出一种WMD模型（基于EMD模型，一种翻译为搬土距离，所以WMD可以翻译成搬字距离，一定这么翻),一种计算文档的距离。本文的实验基于句子中共同出现有意义的单词的。WMD距离根据移动文档中词语最少的个数来衡量两个文档的差异（类似于最小编辑距离）。我们发现WMD可以作为EMD的一种映射，EMD是一种高效的解决移动问题的方法。我们的度量中没有超参数可以直接使用。最后，我们使用8种现实世界的分类数据和七个国家艺术基线对比？发现WMD达到了的KNN错误率前所未有的低。

### 前言
Accurately representing the distance between two documents has far-reaching applications in document retrieval (Salton & Buckley, 1988), news categorization and clustering (Ontrup & Ritter, 2001; Greene & Cunningham, 2006), song identification (Brochu & Freitas, 2002), and multilingual document matching (Quadrianto et al., 2009).
实际上计算两个文档之间的距离在文档检索(Salton & Buckley, 1988)、新闻分类和聚类(Ontrup & Ritter, 2001; Greene & Cunningham, 2006)、音乐识别(Brochu & Freitas, 2002)和多语言文档匹配(Quadrianto et al., 2009)等领域有着广泛的应用，

The two most common ways documents are represented is via a bag of words (BOW) or by their term frequency- inverse document frequency (TF-IDF). However, these features are often not suitable for document distances due to their frequent near-orthogonality (Scho ̈lkopf et al., 2002; Greene & Cunningham, 2006). Another significant drawback of these representations are that they do not capture the distance between individual words. Take for example the two sentences in different documents: Obama speaks to the media in Illinois and: The President greets the press in Chicago. While these sentences have no words in common, they convey nearly the same information, a fact that cannot be represented by the BOW model. In this case, the closeness of the word pairs: (Obama, President); (speaks, greets); (media, press); and (Illinois, Chicago) is not factored into the BOW-based distance.
两个最常用于文本表示的模型:词袋(BOW)模型和词频-逆文档频率(TF-IDF)模型。然而，这些特征往往不适合表示文档距离因为生成的特征向量往往是正交的(Scho ̈lkopf et al., 2002; Greene & Cunningham, 2006). 另一个显著的缺点是这些特征无法表示单个词语之间的距离。举个例子在不同的文档中提取出两句话：1.“奥巴马在伊利诺斯州回答记者问题” 2.“总统在芝加哥接见媒体(访问)” 这两句话里没有相同的词语，却几乎表达了同样的意思。这种情况下无法用此袋模型来表示, 词袋模型考虑不到（总统、奥巴马)／(speak、greet) (伊利诺斯州、芝加哥)（记者、媒体）这些词对之间的距离。
There have been numerous methods that attempt to circumvent this problem by learning a latent low-dimensional representation of documents. Latent Semantic Indexing (LSI) (Deerwester et al., 1990) eigendecomposes the BOW feature space, and Latent Dirichlet Allocation (LDA) (Blei et al., 2003) probabilistically groups similar words into topics and represents documents as distribution over these topics. At the same time, there are many competing variants of BOW/TF-IDF (Salton & Buckley, 1988; Robertson & Walker, 1994). While these approaches produce a more coherent document representation than BOW, they often do not improve the empirical performance of BOW on distance-based tasks (e.g., nearest-neighbor classifiers) (Petterson et al., 2010; Mikolov et al., 2013c).
有多种手段可以规避这种问题，大多基于一个隐含低维的文本表示。潜层语义分析(LSI)(Deerwester et al., 1990)产生组合的词袋特征空间，和潜层狄利克雷分布(LDA)(Blei et al., 2003)通过概率计算主题分布中主题词的相似度来表示文档。同时存在很多基于BOW/TF-IDF的变体(Salton & Buckley, 1988; Robertson & Walker, 1994)。这些方法比词袋模型多生称一种耦合的文档，在计算距离任务上相对于词袋(BOW)模型并不能提高实验性能。
In this paper we introduce a new metric for the distance between text documents. Our approach leverages recent results by Mikolov et al. (2013b) whose celebrated word2vec model generates word embeddings of unprecedented quality and scales naturally to very large data sets (e.g., we use a freely-available model trained on approximately 100 bil- lion words). The authors demonstrate that semantic rela- tionships are often preserved in vector operations on word vectors, e.g., vec(Berlin) - vec(Germany) + vec(France) is close to vec(Paris). This suggests that distances and between embedded word vectors are to some degree se- mantically meaningful. Our metric, which we call the Word Mover’s Distance (WMD), utilizes this property of word2vec embeddings. We represent text documents as a weighted point cloud of embedded words. The distance be- tween two text documents A and B is the minimum cumu- lative distance that words from document A need to travel to match exactly the point cloud of document B. Figure 1 shows a schematic illustration of our new metric.
本文引入一种新的度量文档距离的标准，利用Mikolov(word2vec作者)等人(2013b)的最新成果,使用word2vec模型可以快速训练海量数据集生成词向量(e.g., we use a freely-available model trained on approximately 100 billion words).作者已证明语义关系在向量操作中大多保留在词向量中，例如V(柏林)-V(德国)+V(法国)非常接近V(巴黎)。这说明词向量之间的距离在某种程度上对文档的语义上有意义，我们的度量标准我们称之为搬词距离（Word Mover’s Distance,WMD)利用word2vec的这种属性。我们将文档作为词集合的一种权重点,文档A与文档B之间的距离定义为文档A为了达到与文档B匹配需要移动的最少的单词点。图一是新度量的一种示意图
The optimization problem underlying WMD reduces to a special case of the well-studied Earth Mover’s Distance (Rubner et al., 1998) transportation problem and we can leverage existing literature on fast specialized solvers (Pele & Werman, 2009). We also compare several lower bounds and show that these can be used as approximations or to prune away documents that are provably not amongst the k-nearest neighbors of a query.
WMD的优化问题是训练好的EMD的一种特例(Rubner et al., 1998)，传输问题我们可以利用存在的字母快速解决(Pele & Werman, 2009).同样也可以比较多个KNN近似的下界用来得出近似或者删除文档。
The WMD distance has several intriguing properties: 1. it is hyper-parameter free and straight-forward to understand and use; 2. it is highly interpretable as the distance between two documents can be broken down and explained as the sparse distances between few individual words; 3. it naturally incorporates the knowledge encoded in the word2vec space and leads to high retrieval accuracy it outperforms all 7 state-of-the-art alternative document distances in 6 of 8 real world classification tasks.
WMD有几个有趣的属性：1.没有超参数可以直接理解使用，2.可以高度体现距离因为两个文档间的距离可能分解，稀疏矩阵只有极少个单词。3.天然包含了word2vec空间学到的编码内容，具有很高的搜索精度。

### 相关工作
Constructing a distance between documents is closely tied with learning new document representations. One of the first works to systematically study different combinations of term frequency-based weightings, normalization terms, and corpus-based statistics is Salton & Buckley (1988). Another variation is the Okapi BM25 function (Robertson & Walker, 1994) which describes a score for each (word, document) pair and is designed for ranking applications. Aslam & Frost (2003) derive an information-theoretic sim- ilarity score between two documents, based on probability of word occurrence in a document corpus. Croft & Lafferty (2003) use a language model to describe the probability of generating a word from a document, similar to LDA (Blei et al., 2003). Most similar to our method is that of Wan (2007) which first decomposes each document into a set of subtopic units via TextTiling (Hearst, 1994), and then mea- sures the effort required to transform a subtopic set into another via the EMD (Monge, 1781; Rubner et al., 1998).
建立文档间的距离矩阵与学习文档特征表示相似。首先要做的事情是系统化学习不同的词频权重，归一化词语，和基于预料的统计Salton & Buckley (1988)另一个变种是Okapi BM25 方法 (Robertson & Walker, 1994)这里为每个(词，文档)对设置一个分数，用于排序系统。Aslam & Frost (2003)引入一种基于文档集合中单词共现概率的信息论相似度。 Croft & Lafferty (2003)使用一种语言模型来描述从文档种生成单词的概率，类似于LDA模型(Blei et al., 2003).我们使用的大多数相似度是Wan(2007) 首次通过文章分解(Hearst, 1994)将每个文档分解成一个子主题集合，然后通过EMD (Monge, 1781; Rubner et al., 1998)衡量子主题之间转换的代价。

New approaches for learning document representations include Stacked Denoising Autoencoders (SDA) (Glorot et al., 2011), and the faster mSDA (Chen et al., 2012), which learn word correlations via dropout noise in stacked neural networks. Recently, the Componential Counting Grid (Perina et al., 2013) merges LDA (Blei et al., 2003) and Counting Grid (Jojic & Perina, 2011) models, allow- ing ‘topics’ to be mixtures of word distributions. As well, Le & Mikolov (2014) learn a dense representation for doc- uments using a simplified neural language model, inspired by the word2vec model (Mikolov et al., 2013a).
新的文本表示方法包括多层降噪自动编码机(Stacked Denoising Autoencoders,SDA, Glorot et al., 2011),和较快的mSDA (Chen et al., 2012),根据多层神经网络降噪来学习单词之间的联系。最近，网格成分计算(Perina et al., 2013) 结合LDA和网格计算模型，将主题视为单词的混合分布。同时Le & Mikolov (2014)受到word2vec的启发，提出一种利用简单的神经语言模型，基于密度的文本表示方法。
The use of the EMD has been pioneered in the computer vision literature (Rubner et al., 1998; Ren et al., 2011). Sev- eral publications investigate approximations of the EMD for image retrieval applications (Grauman & Darrell, 2004; Shirdhonkar & Jacobs, 2008; Levina & Bickel, 2001). As word embeddings improve in quality, document retrieval enters an analogous setup, where each word is associated with a highly informative feature vector. To our knowledge, our work is the first to make the connection between high quality word embeddings and EMD retrieval algorithms.
EMD算法已经用于计算机视觉领域(Rubner et al., 1998; Ren et al., 2011)，多篇著作在图像索引应用中的调查研究与EMD相似 (Grauman & Darrell, 2004; Shirdhonkar & Jacobs, 2008; Levina & Bickel, 2001).由于词向量在质量傻姑娘和文档检索是相同的，每个词都与一个信息量很高的特征向量相关。在我们的认知中，我们的首要任务是建立高质量词向量和EMD检索算法之间的连接。
Cuturi (2013) introduces an entropy penalty to the EMD objective, which allows the resulting approximation to be solved with very efficient iterative matrix updates. Further, the vectorization enables parallel computation via GPGPUs However, their approach assumes that the number of di- mensions per document is not too high, which in our set- ting is extremely large (all possible words). This removes the main benefit (parallelization on GPGPUs) of their ap- proach and so we develop a new EMD approximation that appears to be very effective for our problem domain。
Cuturi (2013)介绍了EMD的一种熵，使得近似计算结果可以非常高效的随着矩阵的更新而迭代。更重要的是这种功能向量计算可以使用多个GPU并行计算。然而这种计算方法假设每个文档的维度不会太高，否则会使得配置集合超级大（包含所有可能的单词）。这删除了主要的计算便利（GPU并行计算）。我们优化出新的EMD解决方法，从结果看可以很高效的解决以上问题。

### Word2Vec Embedding
Word2Vec 词向量
Recently Mikolov et al. (2013a;b) introduced word2vec, a novel word-embedding procedure. Their model learns a vector representation for each word using a (shallow) neu- ral network language model. Specifically, they propose a neural network architecture (the skip-gram model) that con- sists of an input layer, a projection layer, and an output layer to predict nearby words. Each word vector is trained to maximize the log probability of neighboring words in a corpus, i.e., given a sequence of words w1 , . . . , wT ,
最近，Mikolov et al. (2013a;b)提出了word2vec，一种新的词向量计算过程。

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/Alucardmini/atec.github.io/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://help.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.