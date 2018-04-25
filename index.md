## From Word Embeddings To Document Distances
根据词语成分计算文档相似度

### 简介

We present the Word Mover’s Distance (WMD), a novel distance function between text documents. Our work is based on recent results in word embeddings that learn semantically meaningful representations for words from local cooccurrences in sentences. The WMD distance measures the dissimilarity between two text documents as the minimum amount of distance that the embedded words of one document need to “travel” to reach the embedded words of another document. We show that this distance metric can be cast as an instance of the Earth Mover’s Distance, a well studied transportation problem for which several highly efficient solvers have been developed. Our metric has no hyperparameters and is straight-forward to implement. Further, we demonstrate on eight real world document classi- fication data sets, in comparison with seven state- of-the-art baselines, that the WMD metric leads to unprecedented low k-nearest neighbor docu- ment classification error rates.
本文提出一种WMD模型（基于EMD模型，一种翻译为搬土距离，所以WMD可以翻译成搬字距离，一定这么翻),一种计算文档的距离。本文的实验基于句子中共同出现有意义的单词的。WMD距离根据移动文档中词语最少的个数来衡量两个文档的差异（类似于最小编辑距离）。我们发现WMD可以作为EMD的一种映射，EMD是一种高效的解决移动问题的方法。我们的度量中没有超参数可以直接使用。最后，我们使用8种现实世界的分类数据和七个国家艺术基线对比？发现WMD达到了的KNN错误率前所未有的低。







### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/Alucardmini/atec.github.io/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://help.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.
