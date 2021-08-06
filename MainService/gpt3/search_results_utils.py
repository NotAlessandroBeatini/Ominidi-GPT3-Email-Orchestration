# the minimum relative difference of the two highest scores of the semantic search for erl_erk
# if the rel diff is less, we use the classifier
# this is a hyperparameter we can tune
MIN_REL_DIFF = .1

def create_search_results(response):
    return list(sorted((SearchResult(datum) for datum in response["data"]), key=lambda sr: sr.score))

def rel_diff_is_too_small(search_results):
    return len(search_results) > 1 and rel_diff(search_results[0].score, search_results[1].score) < MIN_REL_DIFF

def rel_diff(a, b):
    return (a - b)/ a

class SearchResult:
    TYPES = [["erk", "elk"], ["erk"], ["elk"]]

    def __init__(self, search_result_json):
        self.type=SearchResult.TYPES[search_result_json["document"]]
        self.score=search_result_json["score"]
