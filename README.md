# cs121-proj3
UCI CS 121 - Project 3

Steps to run this properly:

1) `py indexer.py [file_path]`
Input: file_path is the folder where the documents are. For example: Desktop/DEV/**
Output: Produces many partial indexes (inverted_index_{}.txt).

2) `py merger.py`
Output: full_index.txt where all the partial indexes are merged and tf-idf is calculated.

3) `py cosine_dlower.py`
Output: cosine_dlower.txt that contains a dictionary with key= doc_id, value= sum of tf_idf squared for all
tokens that that document has. Will be used later for cosine scores.

4) `py splitter.py`
Output: Many split indexes (split_index/split_index_{}.txt) to make searching quicker.

5) `py searcher.py`
Input: Search query
Output: Prints top results (page's url) for given query.