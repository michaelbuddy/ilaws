# ilaws using ML and deep learning to build great contact auto risk identification
 
[![image](https://api.travis-ci.org/miso-belica/sumy.png?branch=master)](https://travis-ci.org/miso-belica/sumy)

 
:


-   **Install *.whl**  upgrade pip to >8 verison using the command
>    python -m pip install --upgrade pip
 

-   **numpy,scipy,gensim** - pip install numpy*whl,pip install scipy*whl,pip install gensim*whl 
-   **Edmundson** heurestic method with previous statistic research,
    [reference](http://dl.acm.org/citation.cfm?doid=321510.321519)

-   **Latent Semantic Analysis, LSA** - one of the algorithm from
    <http://scholar.google.com/citations?user=0fTuW_YAAAAJ&hl=en> I
    think the author is using more advanced algorithms now.
    [Steinberger, J. a Je?ek, K. Using latent semantic an and
    summary evaluation. In In Proceedings ISIM '04. 2004. S.
    93-100.](http://www.kiv.zcu.cz/~jstein/publikace/isim2004.pdf)

-   **LexRank** - Unsupervised approach inspired by algorithms PageRank
    and HITS,
    [reference](http://tangra.si.umich.edu/~radev/lexrank/lexrank.pdf)

-   **TextRank** - some sort of combination of a few resources that I
    found on the internet. I really don't remember the sources. Probably
    [Wikipedia](https://en.wikipedia.org/wiki/Automatic_summarization#Unsupervised_approaches:_TextRank_and_LexRank)
    and some papers in 1st page of Google :)

-   **SumBasic** - Method that is often used as a baseline in
    the literature. Source: [Read about
    SumBasic](http://www.cis.upenn.edu/~nenkova/papers/ipm.pdf)

-   **KL-Sum** - Method that greedily adds sentences to a summary so
    long as it decreases the KL Divergence. Source: [Read about
    KL-Sum](http://www.aclweb.org/anthology/N09-1041)