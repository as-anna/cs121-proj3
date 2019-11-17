class Posting(dict):
    # For the indexer, tf_idf is only occurrences of token in document
    # Calculate tf_idf later once have all docs in scorer
    def __init__(self, doc_id, tf_idf, fields):
        self.doc_id = doc_id
        self.tf_idf = tf_idf
        self.fields = fields

        # A dict object so the class is JSON serializable
        dict.__init__(self, doc_id=doc_id, tf_idf=tf_idf, fields=fields)