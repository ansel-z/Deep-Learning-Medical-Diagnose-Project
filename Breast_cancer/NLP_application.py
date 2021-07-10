import spacy
import yake
from rake_nltk import Rake


def get_keywords(description):
    keyword_dict = {}
    keyword_list, length = get_keyword_spacy(description)
    keyword_list.extend(get_keyword_yake(description))
    keyword_list.extend(get_keyword_rake_nltk(description))
    # print(keyword_list)
    for keyword in keyword_list:
        for word in keyword.split(" "):
            if word.lower() in keyword_dict:
                keyword_dict[word.lower()] += 1
            else:
                keyword_dict[word.lower()] = 1
    # print(list(keyword_dict.items()))
    # print(length)
    top_keywords = sorted(list(keyword_dict.items()),key=lambda x:x[1],reverse=True)[:int(length * 0.4)]
    keywords_to_display = [keyword[0] for keyword in top_keywords]
    return keywords_to_display

def get_keyword_spacy(description):
    nlp = spacy.load("en_core_web_md")
    doc = nlp(description)
    keyword_list = [keyword.text for keyword in list(doc.ents)]
    return keyword_list, len(doc)

def get_keyword_yake(description):
    nlp = yake.KeywordExtractor()
    nlp2 = yake.KeywordExtractor(lan="en", n=3, dedupLim=0.9, top=15, features=None)
    keywords = nlp2.extract_keywords(description)
    # print(keywords)
    keyword_list = [keyword[0] for keyword in keywords]
    return keyword_list

def get_keyword_rake_nltk(description):
    nlp = Rake()
    nlp.extract_keywords_from_text(description)
    keyword_list = nlp.get_ranked_phrases()
    return keyword_list


if __name__ == '__main__':
    # Test example
    text = "I am a 46 years old man, and my bump hurts. I have had it for three weeks. Is it cancer?"
    list = get_keywords(text)
    print("Input Description:")
    print(text)
    print("Keywords extracted:")
    print(list)
