from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
import nltk
nltk.download('punkt_tab')
text = "SQL is a computer language that is used for storing, manipulating, and retrieving data in a structured format. This language was invented by IBM. Here SQL stands for Structured Query Language. Interacting databases with SQL queries, we can handle a large amount of data. There are several SQL-supported database servers such as MySQL, PostgreSQL, sqlite3 and so on. Data can be stored in a secured and structured format through these database servers. SQL queries are often used for data manipulation and business insights better"

parser = PlaintextParser.from_string(text, Tokenizer("english"))
summarizer = LexRankSummarizer()
summary = summarizer(parser.document, 2)

for s in summary:
    print(s)