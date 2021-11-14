class Evaluator():
    def zip_evaluate(coefs, words):
        if len(coefs) != len(words):
            return -1
        result = 0
        for c, w in zip(coefs, words):
            result = result + c * len(w)
        return (result)
        
    def enumerate_evaluate(coefs, words):
        if len(coefs) != len(words):
            return -1     
        result = 0
        for _, (p1, p2) in enumerate(zip(coefs, words)):
            result = result + p1 * len(p2)
        return(result)
