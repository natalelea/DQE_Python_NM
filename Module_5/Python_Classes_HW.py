class GetInput:
    def read_publication_type(self):
        publication_type = input('*' * 10 + ' What type of publication would you like to add? ' + '*' * 10 +
                                 '\n"1" for News \n"2" for Private Ad \n"3" for Notes\n'
                                 'Please enter: ')
        while publication_type not in ('1', '2', '3'):
            publication_type = input('You entered incorrect value. Please, select once more: ')

        if publication_type == '1':
            publication_type = 'News'
        elif publication_type == '2':
            publication_type = 'Private Ad'
        elif publication_type == '3':
            publication_type = 'Self Notes'

        return publication_type

    def read_text(self):
        user_text = input('Please enter your text: ')
        return user_text

    def read_city(self):
        city_name = input('Please enter city: ')
        return city_name

    def read_date(self):
        date_until_actual = input('Please enter date until that the Ad is actual (using format "yyyy-mm-dd") : ')
        return date_until_actual

    def read_tip_wish(self):
        is_tip_wish = input('Would you like to get a daily tip?' + '\nPlease enter "yes" or "no": ')
        is_tip_wish = is_tip_wish.lower().strip()
        while is_tip_wish not in ('yes', 'no'):
            is_tip_wish = input('You entered incorrect value. Please, select once more: ')
            is_tip_wish = is_tip_wish.lower().strip()
        return is_tip_wish


class News(GetInput):
    def __init__(self, publication_type='None', user_text='None', city_name='None'):
        self.publication_type = publication_type
        self.user_text = user_text
        self.city_name = city_name

    def publish_title(self, publication_type):
        file_to_save_data.write(publication_type + ' ' + (30 - len(publication_type) - 1) * '-')

    def publish_text(self, user_text):
        file_to_save_data.write('\n' + user_text)

    def publish_city(self, city_name):
        file_to_save_data.write('\n' + city_name)

    def publish_current_date(self):
        from datetime import datetime
        file_to_save_data.write(', ' + str(datetime.today()))

    def publish_last_block_line(self):
        file_to_save_data.write('\n' + 30 * '-' + '\n\n\n')


class PrivateAd(GetInput):
    def __init__(self, publication_type='None', user_text='None', actual_until_date='None'):
        self.publication_type = publication_type
        self.user_text = user_text
        self.actual_until_date = actual_until_date

    def publish_title(self, publication_type):
        file_to_save_data.write(publication_type + ' ' + (30 - len(publication_type) - 1) * '-')

    def publish_text(self, user_text):
        file_to_save_data.write('\n' + user_text)

    def publish_date(self, actual_until_date):
        file_to_save_data.write('\n' + 'Actual until: ' + actual_until_date)

    def publish_days_left(self, actual_until_date):
        from datetime import date, datetime

        actual_until_date = datetime.strptime(actual_until_date, "%Y-%m-%d")
        current_date = datetime.strptime(str(date.today()), "%Y-%m-%d")

        days_left = str((actual_until_date - current_date).days)
        file_to_save_data.write(', ' + days_left + ' days left')

    def publish_last_block_line(self):
        file_to_save_data.write('\n' + 30 * '-' + '\n\n\n')


class Notes(GetInput):
    def __init__(self, publication_type='None', user_text='None', tip_wish='no'):
        self.publication_type = publication_type
        self.user_text = user_text
        self.tip_wish = tip_wish

    def publish_title(self, publication_type):
        file_to_save_data.write(publication_type + ' ' + (30 - len(publication_type) - 1) * '-')

    def publish_text(self, user_text):
        file_to_save_data.write('\n' + user_text)

    def publish_tip(self, tip_wish):
        if tip_wish == 'yes':
            file_to_save_data.write('\n' + 'You are doing great! Keep going ;-;')

    def publish_last_block_line(self):
        file_to_save_data.write('\n' + 30 * '-' + '\n\n\n')


def main():

    publication_type = GetInput().read_publication_type()

    if publication_type == 'News':
        input1 = News()
        user_text = input1.read_text()
        city = input1.read_city()
        input1.publish_title(publication_type)
        input1.publish_text(user_text)
        input1.publish_city(city)
        input1.publish_current_date()
        input1.publish_last_block_line()
    elif publication_type == 'Private Ad':
        input2 = PrivateAd()
        user_text = input2.read_text()
        date_until_actual = input2.read_date()
        input2.publish_title(publication_type)
        input2.publish_text(user_text)
        input2.publish_date(date_until_actual)
        input2.publish_days_left(date_until_actual)
        input2.publish_last_block_line()
    elif publication_type == 'Self Notes':
        input3 = Notes()
        user_text = input3.read_text()
        tip_wish = input3.read_tip_wish()
        input3.publish_title(publication_type)
        input3.publish_text(user_text)
        input3.publish_tip(tip_wish)
        input3.publish_last_block_line()


global file_to_save_data
file_to_save_data = open("MyFile.txt", "a")
main()
file_to_save_data.close()
