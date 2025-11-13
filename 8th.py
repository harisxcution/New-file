import os, re, math  # os: files, re: regex, math: logs/sqrt
from collections import Counter  # Counter: quick word counts

# tiny stopword list to ignore very common words
STOPWORDS = set("""
a an and are as at be but by for from has have if in into is it its of on or our so that
the their there these this those to was we were will with within without you your
""".split())

WORD_RE = re.compile(r"[a-z0-9']+")  # regex to grab simple words (lowercase letters/digits/')

def read_posts():  # read the source text file
    for p in ("posts.text", "posts.txt"):  # try preferred then fallback name
        if os.path.exists(p):  # if the file exists
            with open(p, encoding="utf-8") as f:  # open as UTF-8
                return f.read().strip()  # read all and trim edges
    # if neither file exists, tell the user what to do
    raise FileNotFoundError(
        "Make 'posts.text' (or 'posts.txt') with paragraphs separated by blank lines."
    )

def split_docs(text):  # split file into paragraph documents
    # split on blank lines, strip pieces, keep non-empty
    return [b.strip() for b in re.split(r"\n\s*\n", text) if b.strip()]

def tokenize(s):  # turn text into tokens
    # lowercase, find words, drop stopwords
    return [w for w in WORD_RE.findall(s.lower()) if w not in STOPWORDS]

def build_tfidf(docs):  # precompute TF-IDF vectors for all docs
    toks = [tokenize(d) for d in docs]  # tokens per doc
    N = len(toks)  # number of docs
    df = Counter(t for ts in toks for t in set(ts))  # document frequency per term
    idf = {t: math.log(N / (1 + dfv)) + 1.0  # IDF with smoothing
           for t, dfv in df.items()}
    tfidf_docs = []  # list of per-doc vectors
    for ts in toks:  # for each doc
        tf = Counter(ts)  # term counts in doc
        m = max(tf.values()) if tf else 1  # max count (avoid /0)
        tfidf_docs.append({t: (c / m) * idf[t]  # normalized TF * IDF
                           for t, c in tf.items()})
    return tfidf_docs, idf  # return vectors + idf for queries

def cosine(a, b):  # cosine similarity between two sparse dicts
    if len(a) > len(b):
        a, b = b, a  # iterate over smaller one
    dot = sum(wa * b.get(t, 0.0) for t, wa in a.items())  # dot product
    na = math.sqrt(sum(wa * wa for wa in a.values()))  # norm a
    nb = math.sqrt(sum(wb * wb for wb in b.values()))  # norm b
    return 0.0 if na == 0 or nb == 0 else dot / (na * nb)  # safe cosine

def vec_query(q, idf):  # vectorize the user question using same IDF
    tf = Counter(t for t in tokenize(q) if t in idf)  # count known terms only
    if not tf:
        return {}  # empty if nothing useful
    m = max(tf.values())  # max count for norm
    return {t: (c / m) * idf[t] for t, c in tf.items()}  # TF * IDF

def main():  # CLI loop
    try:
        text = read_posts()  # load file
    except FileNotFoundError as e:
        print(e)
        return  # show hint and exit

    docs = split_docs(text)  # make paragraphs
    if not docs:
        print("Your posts file is empty. Add a few paragraphs separated by blank lines.")
        return  # nothing to search

    tfidf_docs, idf = build_tfidf(docs)  # prep vectors
    print(f"Loaded {len(docs)} document(s). Ask me anything (type 'exit' to quit).")  # intro

    while True:  # REPL
        q = input("What do you want to know? ").strip()  # read query
        if not q:
            continue  # ignore empty input
        if q.lower() in {"exit", "quit", "q"}:  # quit commands
            print("Goodbye!")
            break

        qv = vec_query(q, idf)  # vectorize query
        if not qv:
            print("\nSorry, no meaningful words found in your query.\n")
            continue

        scores = [cosine(qv, dv) for dv in tfidf_docs]  # score all docs
        i = max(range(len(scores)), key=scores.__getitem__)  # best index
        if scores[i] < 0.05:  # low similarity threshold
            print("\nSorry, I couldn't find an answer in the file.\n")
            continue

        print("\n--- Answer (from your file) ---")  # show best paragraph
        print(docs[i])
        print("-------------------------------\n")

if __name__ == "__main__":  # run only when executed directly
    main()  # start the program