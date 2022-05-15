from functions.extract_reddit_user_comments import search_redditor
from functions.extract_reddit_user_comments import extract_redditor_comments
from functions.analyse_reddit_user_comments import count_redditor_bad_words

if __name__ == "__main__":
    redditor = search_redditor("")
    redditor_comments = extract_redditor_comments(redditor)
    count_redditor_bad_words(redditor_comments)