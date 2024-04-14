import csv
from collections import Counter


def calculate_words_counts(file):
    with open(file, "r") as f:
        cleaned_file = f.read().replace("\n", " ") \
            .replace("=", "") \
            .replace("|", "") \
            .replace(":", "")
        split_file = [w for w in cleaned_file.split(" ") if (w and not w[0].isdigit())]
        result = Counter(split_file)
        # print(result.values())
        return result


def check_count(letter_list):
    cnt_upper = Counter([let for let in letter_list if let.isupper()])
    cnt_all = Counter([let.lower() for let in letter_list])
    percentages = {}
    result = {}

    for letter, count_all in cnt_all.items():
        count_upper = cnt_upper.get(letter.upper(), 0)
        total_count = count_all + count_upper
        if total_count > 0:
            percentage = f"{round(((count_upper / total_count) * 100), 2)}%"
            percentages[letter] = percentage
        else:
            percentages[letter] = 0

    for letter in percentages:
        result[letter] = [cnt_all[letter], cnt_upper[letter.upper()], percentages[letter]]
    return result


def calculate_letters_count(file):
    with open(file, "r") as f:
        cleaned_file = f.read().replace("\n", " ") \
            .replace("=", "") \
            .replace("|", "") \
            .replace(":", "") \
            .replace("-", "") \
            .replace(" ", "")
        split_file = [let for let in [*cleaned_file] if (let and not let.isdigit())]

        result = check_count(split_file)
        return result


def write_words_counts(file, count_dict, header, dialect):
    with open(file, "w") as f:
        writer = csv.DictWriter(f, fieldnames=header, dialect=dialect)
        writer.writeheader()
        for key, value in count_dict.items():
            writer.writerow({header[0]: key, header[1]: value})


def write_letters_count(file, count_dict, header, dialect):
    with open(file,"w") as f:
        writer = csv.DictWriter(f, fieldnames=header, dialect=dialect)
        writer.writeheader()
        for key, value in count_dict.items():
            writer.writerow({header[0]: key,
                             header[1]: value[0],
                             header[2]: value[1],
                             header[3]: value[2]})


def run_metrics():
    csv.register_dialect("dialect", delimiter=",", quotechar="'", quoting=csv.QUOTE_NONE)
    input_file = "../e_files/news_feed.txt"
    words_count_output_file = "words_count.csv"
    letter_counts_output_file = "letter_count.csv"
    count_of_words = calculate_words_counts(input_file)
    words_count_header = ["WORD", "COUNT"]
    letter_counts_header = ["LETTER", "TOTAL_ALL", "TOTAL_UPPERCASE", "PERCENTAGE"]
    write_words_counts(words_count_output_file, count_of_words, words_count_header, "dialect")
    letters_counts = calculate_letters_count(input_file)
    write_letters_count(letter_counts_output_file, letters_counts, letter_counts_header, "dialect")


if __name__ == "__main__":
    run_metrics()
