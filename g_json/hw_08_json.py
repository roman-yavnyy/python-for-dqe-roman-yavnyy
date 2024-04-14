import json
import sys
from d_classes_oop.hw_05_classes_oop import News, PrivateAd, Vacancies


class JsonFeedProvider:
    def __init__(self):
        self.json_path = './input_feeds.json'
        self.output_feeds_list = []

    def prepare_feeds_from_json_file(self):
        with open(self.path, "r") as f:
            feed_dict = json.load(f)
            if feed_dict:
                for v in feed_dict.values():
                    for key, value in v.items():
                        if v["feed_type"] == "News":
                            self.output_feeds_list.append(News(v["text"], v["city"]))
                        elif v["feed_type"] == "PrivateAd":
                            self.output_feeds_list.append(PrivateAd(v["text"], v["expiration_date"]))
                        elif v["feed_type"] == "Vacancy":
                            self.output_feeds_list.append(
                                Vacancies(v["company_name"], v["name"], v["description"], v["salary"]))
                        else:
                            print("Wrong data")
                            sys.exit()


if __name__ == "__main__":
    json_feed_provider = JsonFeedProvider()
    json_feed_provider.prepare_feeds_from_json_file()
