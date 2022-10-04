from gensim.summarization import summarize


def summary(text: str, ratio: float) -> str:
    return summarize(text, ratio=ratio).replace("\n", " ").strip()
