class GetInput:
    def read_publication_type(self):
        publication_type = input('*' * 10 + ' What type of publication would you like to add? ' + '*' * 10 +
                                 '\n"1" for News \n"2" for Private Ad \n"3" for Notes\n'
                                 'Please enter: ')
        if publication_type == '1':
            publication_type = 'News'
        elif publication_type == '2':
            publication_type = 'Private Ad'
        elif publication_type == '3':
            publication_type = 'Self Notes'
        else:
            print('You entered incorrect value')
            quit()

        return publication_type

    def read_text(self):
        user_text = input('Please enter your text: ')
        return user_text

    def read_city(self):
        city_name = input('Please enter city: ')
        return city_name

    def read_date(self):
        from datetime import datetime
        actual_until_date = input('Please enter date until that the Ad is actual (using format "yyyy-mm-dd") : ')

        try:
            datetime.strptime(actual_until_date, '%Y-%m-%d')
        except ValueError:
            print('Incorrect format of date. Should be "yyyy-mm-dd"')
            quit()

        return actual_until_date

    def read_tip_wish(self):
        is_tip_wish = input('Would you like to get a daily tip?' + '\nPlease enter "yes" or "no": ')
        is_tip_wish = is_tip_wish.lower().strip()
        if is_tip_wish != 'yes':
            is_tip_wish = 'no'
        return is_tip_wish


class Publish(GetInput):
    def publish_title(self, publication_type):
        file_to_save_data.write(publication_type + ' ' + (30 - len(publication_type) - 1) * '-')

    def publish_text(self, user_text):
        file_to_save_data.write('\n' + user_text)

    def publish_last_block_line(self):
        file_to_save_data.write('\n' + 30 * '-' + '\n\n\n')


class News(Publish):

    def publish_city(self, city_name):
        file_to_save_data.write('\n' + city_name)

    def publish_current_date(self):
        from datetime import datetime
        file_to_save_data.write(', ' + str(datetime.today()))


class PrivateAd(Publish):

    def publish_date(self, actual_until_date):
        file_to_save_data.write('\n' + 'Actual until: ' + actual_until_date)

    def publish_days_left(self, actual_until_date):
        from datetime import date, datetime

        actual_until_date = datetime.strptime(actual_until_date, "%Y-%m-%d")
        current_date = datetime.strptime(str(date.today()), "%Y-%m-%d")

        if actual_until_date < current_date:
            print('Please, note: Actual until date is earlier than the current date')

        days_left = str((actual_until_date - current_date).days)
        file_to_save_data.write(', ' + days_left + ' days left')


class Notes(Publish):

    def publish_tip(self, tip_wish):
        if tip_wish == 'yes':
            file_to_save_data.write('\n' + 'You are doing great! Keep going ;-;')


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
