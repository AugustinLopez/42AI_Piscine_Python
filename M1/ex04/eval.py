class Evaluator():
    def zip_evaluate(coefs, words):
        if not isinstance(coefs, list) \
                or not isinstance(words, list):
            return -1
        elif len(coefs) != len(words):
            return -1
        result = 0.0
        for c, w in zip(coefs, words):
            if not (isinstance(c, float) or isinstance(c, int)) \
                    or not isinstance(w, str):
                return -1
            result = result + c * len(w)
        return (result)

    def enumerate_evaluate(coefs, words):
        if not isinstance(coefs, list) \
                or not isinstance(words, list):
            return -1
        if len(coefs) != len(words):
            return -1
        result = 0.0
        for _, (p1, p2) in enumerate(zip(coefs, words)):
            if not (isinstance(p1, float) or isinstance(p1, int)) \
                    or not isinstance(p2, str):
                return -1
            result = result + p1 * len(p2)
        return(result)
