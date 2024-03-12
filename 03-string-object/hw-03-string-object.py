import re
import string

text_to_fix = """homEwork:
  tHis iz your homeWork, copy these Text to variable.


  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.


  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.


  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""
'''
# fixed "iz" words
fixed_text = re.sub(r'(\biz\b)', 'is', text_to_fix, flags=re.I)
# "removed extra newlines"
remove_unneeded_lines = re.sub(r'\n+\s+', '\n', fixed_text, flags=re.M)
# all chars to lower case
lower_case = remove_unneeded_lines.lower()
# removed unneeded spaces
no_extra_spaces = re.sub(r"\n\s+", "\.", lower_case)
# add list to kep capitalised sentences
capitalised = []
# go through each line
for line in no_extra_spaces.splitlines():
    # add list to store sentences
    sentence = []
    # go through each sentence
    for sent in line.split(". "):
        # capitalise each sentence
        sent = sent.capitalize()
        # add it to the list
        sentence.append(sent)
    # store each line in the list
    capitalised.append('. '.join(sentence))
# join all lines in single string
joined_text = '\n'.join(capitalised)
# print result
print(joined_text)

# calculate number of whitespaces in the text using re and \s as whitespace
count = len(re.findall(r'\s', text_to_fix))

print(f"\nNumber  of whitespaces: {count}")
'''


def correct_mistakes(sentence):
    list_of_words = []
    for word in sentence.split(' '):
        if word.lower() == "iz":
            word = word.replace("z", "s")
        list_of_words.append(word)
    return " ".join(list_of_words)


def reformat_text(input_text):
    list_input_sentences = input_text.split('.')
    list_output_words = []

    for sentence in list_input_sentences:
        mod_sent = sentence.strip().lower().capitalize()
        list_output_words.append(correct_mistakes(mod_sent))
    mod_sentence = ".\n".join(list_output_words)
    return mod_sentence


def get_last_words_in_sentence(input_text):
    list_of_sencences = input_text.split('.')
    last_words = []
    for sentence in list_of_sencences:
        last_words.append(sentence.split(' ')[-1])
    last_words_sentence = ' '.join(last_words)
    return last_words_sentence.capitalize()


modified_sentence = reformat_text(text_to_fix)
extra_sentence = get_last_words_in_sentence(modified_sentence)
print(modified_sentence)
print(extra_sentence)
