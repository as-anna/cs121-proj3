# cs121-proj3
UCI CS 121 - Project 3

Goal: Implement a complete search engine.

✓ Indexer:  Create an inverted index for the given corpus with data structures designed by you. 

✓ Tokens: all alphanumeric sequences in the dataset.

Stop words: do not use stopping, i.e. use all words, even the frequently occurring ones.

✓ Stemming: use stemming for better textual matches. Suggestion: Porter stemming.

Important words: Words in bold, in headings (h1, h2, h3), and in titles should be treated as more important than the other words.

Search: Your program should prompt the user for a query. This doesn’t need to be a Web interface, it can be a console prompt. At the time of the query, your program will stem the query terms, look up your index, perform some calculations (see ranking below) and give out the ranked list of pages that are relevant for the query, with the most relevant on top. Pages should be identified by their URLs.Ranking: at the very least, your ranking formula should include tf-idf scoring, and take the important words into consideration, but you should feel free to add additional components to this formula if you think they improve the retrieval.
