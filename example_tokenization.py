#import the MeTA python bindings
import metapy
#If you'd like, you can tell MeTA to log to stderr so you can get progress output when running long-running function calls.
metapy.log_to_stderr()
doc = metapy.index.Document()

doc.content("I said that I can't believe that it only costs $19.95!")
tok = metapy.analyzers.ICUTokenizer()
tok.set_content(doc.content()) # this could be any string
tokens = [token for token in tok]
print(tokens)

doc.content("I said that I can't believe that it only costs $19.95! I could only find it for more than $30 before.")
tok.set_content(doc.content())
tokens = [token for token in tok]
print(tokens)

tok = metapy.analyzers.ICUTokenizer(suppress_tags=True)
tok.set_content(doc.content())
tokens = [token for token in tok]
print(tokens)

tok = metapy.analyzers.LengthFilter(tok, min=2, max=30)
tok.set_content(doc.content())
tokens = [token for token in tok]
print(tokens)