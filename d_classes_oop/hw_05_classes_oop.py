import sys
from datetime import datetime


class News:
    def __init__(self, text, city):
        self.type = "News"
        self.text = text
        self.city = city
        self.date = datetime.now().strftime("%c")

    def to_string(self):
        return f"News: {self.text} | City: {self.city} | Date: {self.date} \n"


class PrivateAd:
    def __init__(self, text, expiration_date):
        self.type = "PrivateAd"
        self.text = text
        self.expiration_date = expiration_date
        self.days_left = (expiration_date - datetime.now()).days

    def to_string(self):
        return f"Private Advertisement: {self.text} | " \
               f"Expiration date: {self.expiration_date} | " \
               f"Days left: {self.days_left} \n"


class Vacancies:
    def __init__(self, company_name, name, desctription, salary):
        self.type = "Vacancy"
        self.company_name = company_name
        self.name = name
        self.description = desctription
        self.salary = salary

    def to_string(self):
        return f"Vacancy: ============================\n" \
               f"Company name: {self.company_name} \n" \
               f"Vacancy name: {self.name} \n" \
               f"Description: {self.description} \n" \
               f"Salary: {self.salary} \n" \
               f"=====================================\n"


def create_feed(feed_type):
    if feed_type == "1":
        text = input("Please enter news text: ")
        city = input("Please enter news city: ")
        return News(text, city)
    elif feed_type == "2":
        text = input("Please enter advertisement text: ")
        expiration_date = input("Please enter expiration date in format YYYY-MM-DD: ")
        try:
            expiration_date = datetime.strptime(expiration_date, "%Y-%m-%d")
        except ValueError:
            print("Expiration date does not match format. Exiting...")
            sys.exit()
        return PrivateAd(text, expiration_date)
    elif feed_type == "3":
        company_name = input("Please enter company name: ")
        name = input("Please enter vacancy name: ")
        description = input("Please enter vacancy description: ")
        salary = input("Please enter salary: ")
        return Vacancies(company_name, name, description, salary)
    else:
        print('Exiting')


def save_feed(feed):
    with open("news_feed.txt", "a") as file:
        file.write(feed.to_string())
    print(f"Feed {feed.type} saved successfully")


def run_app():
    feed_type = input("Enter feed type (1 - news, 2 - private_ad, 3 - vacancies, any other input - exit): ")
    feed = create_feed(feed_type)
    if feed:
        save_feed(feed)


if __name__ == "__main__":
    run_app()
