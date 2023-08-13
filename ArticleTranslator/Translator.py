from parrot import Parrot
import torch
import warnings
warnings.filterwarnings("ignore")


# #uncomment to get reproducable paraphrase generations
# def random_state(seed):
#   torch.manual_seed(seed)
#   if torch.cuda.is_available():
#     torch.cuda.manual_seed_all(seed)
#
# random_state(1234)


#Init models (make sure you init ONLY once if you integrate this to your code)
parrot = Parrot(model_tag="prithivida/parrot_paraphraser_on_T5")

phrases = ["Keeks is a menace she despises everyone I walked into a conversation like this?",
           "make sure you init ONLY once if you integrate this to your code",
           "Later, the writing becomes a bit monotonous as it gives minute illustrations of the projects",
           "Where can I find most love?",
           "Can you recommend, some upscale restaurants in Newyork",
           "What are the famous places we should not miss in Russia?"
]

# for phrase in phrases:
#     print("-"*100)
#     print("Input_phrase: ", phrase)
#     print("-"*100)
#     para_phrases = parrot.augment(input_phrase=phrase, use_gpu=False)
#     print(para_phrases[0][0])
#     # for para_phrase in para_phrases:
#     #     print(type(para_phrase))
#     #     print(para_phrase[0])

class Translator:
    # Class Variable
    _verbose = False

    # The init method or constructor
    def __init__(self, replacer = False, verbose = False):
        # Instance Variable
        self._verbose = verbose

    def _getdiffIndices(self, phrases, ori_phrases):
        temp = []
        for index in range(0, len(phrases)):
            if phrases[index] != ori_phrases[index]:
                temp.append(index)
        return temp

    def translate(self, phrases, ori_phrases):
        phrases = phrases.split("\n")
        ori_phrases = ori_phrases.split("\n")

        indices_toTranslate = self._getdiffIndices(phrases, ori_phrases)
        phrases_toTranslate = [phrases[i] for i in indices_toTranslate]

        para_phrases = []
        for phrase in phrases_toTranslate:
            if self._verbose :
                print("Phrase to translate : ", phrase)
            para_phrase = parrot.augment(input_phrase=phrase, use_gpu=False)
            if para_phrase:
                first_para_phrase = para_phrase[0]
                para_phrases.append(first_para_phrase[0])
            else:
                para_phrases.append(phrase)

        indices_tobeInserted = [item for item in list(range(0, len(phrases))) if item not in indices_toTranslate]
        for i in indices_tobeInserted:
            para_phrases.insert(i, ori_phrases[i])

        return "\n".join(para_phrases)
