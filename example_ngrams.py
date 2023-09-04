#import the MeTA python bindings
import metapy
#If you'd like, you can tell MeTA to log to stderr so you can get progress output when running long-running function calls.
metapy.log_to_stderr()
doc = metapy.index.Document()
tok = metapy.analyzers.ICUTokenizer()

doc.content("I said that I can't believe that it only costs $19.95! I could only find it for more than $30 before.")

tok = metapy.analyzers.ICUTokenizer(suppress_tags=True)
tok = metapy.analyzers.LowercaseFilter(tok)
tok.set_content(doc.content())
tokens = [token for token in tok]
print(tokens)

ana = metapy.analyzers.NGramWordAnalyzer(1, tok)
print(doc.content())
unigrams = ana.analyze(doc)
print(unigrams)

ana = metapy.analyzers.NGramWordAnalyzer(2, tok)
bigrams = ana.analyze(doc)
print(bigrams)

tok = metapy.analyzers.CharacterTokenizer()
ana = metapy.analyzers.NGramWordAnalyzer(4, tok)
fourchar_ngrams = ana.analyze(doc)
print(fourchar_ngrams)