#import the MeTA python bindings
import metapy
#If you'd like, you can tell MeTA to log to stderr so you can get progress output when running long-running function calls.
metapy.log_to_stderr()
doc = metapy.index.Document()
tok = metapy.analyzers.ICUTokenizer()

doc.content("I said that I can't believe that it only costs $19.95! I could only find it for more than $30 before.")
tok.set_content(doc.content())
tok = metapy.analyzers.ListFilter(tok, "lemur-stopwords.txt", metapy.analyzers.ListFilter.Type.Reject)
tok.set_content(doc.content())
tokens = [token for token in tok]
print(tokens)


tok = metapy.analyzers.Porter2Filter(tok)
tok.set_content(doc.content())
tokens = [token for token in tok]
print(tokens)