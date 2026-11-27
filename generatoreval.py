from pygarble import EnsembleDetector
def main():
    scorer = EnsembleDetector()
    with open("generated.txt", "r") as f:
        with open("names.txt", "w", encoding = None) as newFile:
            lines = [line.strip() for line in f]
            for word in lines:
                score = scorer.predict_proba(word)
                if (1-score) * 100 > 95:
                    print(word, file = newFile)
main()