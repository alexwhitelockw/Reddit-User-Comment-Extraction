from functions.setup_reddit_api_access import reddit 

def search_redditor(user_name):
    """
        Return a Redditor Profile based on the Reddit Username Search
    """
    redditor_search = reddit.redditors.search(user_name)
    user_search_results = list(redditor_search)
    number_redditors_returned = len(user_search_results)
    if number_redditors_returned == 0:
        print(f"Results returned {number_redditors_returned} Redditor Profile.")
        print("Try again.")
    elif number_redditors_returned == 1:
        print(f"Results returned {number_redditors_returned} Redditor Profile.")
        return user_search_results
    else:
        print(f"Results returned {number_redditors_returned} Redditor Profiles:")
        [print(user.name) for user in user_search_results]
        return None

def extract_redditor_comments(user_profile, comment_limit=None):
    user_profile = user_profile[0]
    if comment_limit is None:
        print("No limit set, the process may take a while.")
    redditor_comments = user_profile.comments.new(limit=comment_limit)
    return [comment.body.split() for comment in redditor_comments]

