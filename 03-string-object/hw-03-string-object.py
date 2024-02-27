import re
import string

text_to_fix = """homEwork:
  tHis iz your homeWork, copy these Text to variable.


  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.


  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.


  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""
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
