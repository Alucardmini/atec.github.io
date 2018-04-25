## From Word Embeddings To Document Distances
依据组成词语计算文档相似度

### 简介

We present the Word Mover’s Distance (WMD), a novel distance function between text docu- ments. Our work is based on recent results in word embeddings that learn semantically mean- ingful representations for words from local co- occurrences in sentences. The WMD distance measures the dissimilarity between two text doc- uments as the minimum amount of distance that the embedded words of one document need to “travel” to reach the embedded words of another document. We show that this distance metric can be cast as an instance of the Earth Mover’s Dis- tance, a well studied transportation problem for which several highly efficient solvers have been developed. Our metric has no hyperparameters and is straight-forward to implement. Further, we demonstrate on eight real world document classi- fication data sets, in comparison with seven state- of-the-art baselines, that the WMD metric leads to unprecedented low k-nearest neighbor docu- ment classification error rates.
```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/Alucardmini/atec.github.io/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://help.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.
