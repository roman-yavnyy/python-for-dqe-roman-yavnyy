import sys
from datetime import datetime
sys.path.append("..")
from d_classes_oop.hw_05_classes_oop import save_feed, News, PrivateAd, Vacancies, run_app as manual_input
from f_csv.hw_07_csv import run_metrics
from g_json.hw_08_json import JsonFeedProvider


class FileFeedProvider(JsonFeedProvider):
    def __init__(self):
        self.input_feeds_list = None
        self.input_type = None
        self.text_path = './input_feeds.txt'
        self.output_feeds_list = []

    def set_input_type(self):
        self.input_type = input("For manual input please enter 1 \n"
                                "For input from text file please enter 2 \n"
                                "For imput from JSON file please enter 3")
        while self.input_type not in ["1", "2", "3"]:
            self.input_type = input("Wrong input. Please try again ")

    def set_filepath(self):
        custom_path = input("If you want to provide input file path please enter it here \n"
                            "If not - leave blank and press Enter \n")
        if custom_path != "":
            self.text_path = custom_path
            self.json_path = custom_path

    def read_feed(self):
        try:
            with open(self.path, "r") as f:
                self.input_feeds_list = [feed for feed in f.read().splitlines()]
        except FileNotFoundError as e:
            print(f"Wrong filepath. {e}")

    def prepare_feeds_from_csv_file(self):
        self.set_filepath()
        self.read_feed()
        if self.input_feeds_list:
            for feed in self.input_feeds_list:
                if feed.split("|")[0] == "News":
                    text = feed.split("|")[1]
                    city = feed.split("|")[2]
                    self.output_feeds_list.append(News(text, city))
                elif feed.split("|")[0] == "PrivateAd":
                    text = feed.split("|")[1]
                    try:
                        expiration_date = feed.split("|")[2]
                        expiration_date = datetime.strptime(expiration_date, "%Y-%m-%d")
                    except ValueError:
                        print("Expiration date does not match format. Exiting...")
                        sys.exit()
                    self.output_feeds_list.append(PrivateAd(text, expiration_date))
                elif feed.split("|")[0] == "Vacancy":
                    company_name = feed.split("|")[1]
                    name = feed.split("|")[2]
                    description = feed.split("|")[3]
                    salary = feed.split("|")[4]
                    self.output_feeds_list.append(Vacancies(company_name, name, description, salary))
                else:
                    print("Wrong data")
                    sys.exit()


if __name__ == "__main__":
    feed_creator = FileFeedProvider()
    feed_creator.set_input_type()
    if feed_creator.input_type == "1":
        manual_input()
    elif feed_creator.input_type == "2":
        feed_creator.prepare_feeds_from_csv_file()
        for feed in feed_creator.output_feeds_list:
            save_feed(feed)
    elif feed_creator.input_type == "3":
        feed_creator.prepare_feeds_from_json_file()
        for feed in feed_creator.output_feeds_list:
            save_feed(feed)
    run_metrics()
