import pandas as pd

def count_redditor_bad_words(user_comments):
    """
        Count Redditor Bad Words
    """
    bad_words = pd.read_csv("data/bad_words/bad_words_list.csv")
    bad_words = bad_words["word"].to_list()  # Select word vector, transform to list.
    user_bad_words = [word for comment in user_comments for word in comment if word in bad_words]
    bad_word_counts = {word: user_bad_words.count(word) for word in user_bad_words} #Iterate through each word in 
    # collection of user bad words. Returns unique word and then a count of each word in the refined list of bad words.
    bad_word_counts = pd.DataFrame.from_dict(bad_word_counts, orient="index").reset_index()
    bad_word_counts.rename(
        columns={"index": "word", 0: "count"}, 
        inplace=True)
    bad_word_counts.sort_values(
        by="count",
        ascending=False,
        inplace=True
    )
    return bad_word_counts
