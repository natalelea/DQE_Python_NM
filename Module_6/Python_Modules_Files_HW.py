class GetInputFromConsole:

    def read_data_providing_way(self):
        data_providing_way = input('What way of providing data would you prefer? ' +
                                 '\n"1" for direct input from console \n"2" for reading data from file\n'
                                 'Please enter: ')

        if data_providing_way == '1':
            data_providing_way = 'Console'
        elif data_providing_way == '2':
            data_providing_way = 'File'
        else:
            print('You entered incorrect value')
            quit()

        return data_providing_way

    def read_publication_type(self):
        publication_type = input('What type of publication would you like to add? ' +
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
        is_tip_wish = input('Would you like to get a daily tip? \nPlease enter "yes" or "no": ')
        is_tip_wish = is_tip_wish.lower().strip()
        if is_tip_wish != 'yes':
            is_tip_wish = 'no'
        return is_tip_wish


class GetInputFromFile:
    def read_records_quantity(self):
        records_quantity = input('Please specify how many rows does the file contain? \nPlease enter "one" or "many": ')
        records_quantity = records_quantity.lower().strip()

        if records_quantity not in ('one', 'many'):
            print('You entered incorrect value')
            quit()

        return records_quantity

    def read_input_file_path(self):
        input_file_path = input('Please specify path to the file containing data? '
                                '\nPlease enter file path or press "Enter" to use the default way: ')

        if input_file_path == '':
            input_file_path = 'input_from_file.txt'

        return input_file_path

    def read_many_rows_from_file(self, input_file_path):
        from Module_4.Python_Functions_Strings_HW import capitalize_first_letter

        try:
            file_with_data = open(input_file_path, "r")
            list_for_all_publications = []

            for line in file_with_data.readlines():
                one_publication_data = {}
                line = line.strip('\n').split('|')
                one_publication_data['publication_type'] = capitalize_first_letter(line[0])
                one_publication_data['user_text'] = capitalize_first_letter(line[1])
                one_publication_data['additional_data'] = capitalize_first_letter(line[2])
                list_for_all_publications.append(one_publication_data)
            file_with_data.close()

            return list_for_all_publications

        except FileNotFoundError:
            print('Incorrect path to file')
            quit()

    def read_one_row_from_file(self, input_file_path):
        from Module_4.Python_Functions_Strings_HW import capitalize_first_letter

        try:
            file_with_data = open(input_file_path, "r")

            list_for_all_publications = []
            one_publication_data = {}

            line = file_with_data.readline()
            line = line.strip('\n').split('|')
            one_publication_data['publication_type'] = capitalize_first_letter(line[0])
            one_publication_data['user_text'] = capitalize_first_letter(line[1])
            one_publication_data['additional_data'] = capitalize_first_letter(line[2])
            list_for_all_publications.append(one_publication_data)
            file_with_data.close()

            return list_for_all_publications

        except FileNotFoundError:
            print('Incorrect path to file')
            quit()

    def read_publication_type(self, my_dict):
        publication_type = my_dict['publication_type']
        publication_type_lower = publication_type.lower().strip()

        if publication_type_lower == 'news':
            publication_type = 'News'
        elif publication_type_lower == 'private ad':
            publication_type = 'Private Ad'
        elif publication_type_lower == 'self notes':
            publication_type = 'Self Notes'
        if publication_type_lower not in ('news', 'private ad', 'self notes'):
            print('There is incorrect publication type value in file')
            quit()

        return publication_type

    def read_text(self, my_dict):
        user_text = my_dict['user_text']
        return user_text

    def read_city(self, my_dict):
        city_name = my_dict['additional_data']
        return city_name

    def read_date(self, my_dict):
        from datetime import datetime
        actual_until_date = my_dict['additional_data']

        try:
            datetime.strptime(actual_until_date, '%Y-%m-%d')
        except ValueError:
            print('Incorrect format of date. Should be "yyyy-mm-dd"')
            quit()

        return actual_until_date

    def read_tip_wish(self, my_dict):
        is_tip_wish = my_dict['additional_data']
        is_tip_wish = is_tip_wish.lower().strip()
        if is_tip_wish != 'yes':
            is_tip_wish = 'no'
        return is_tip_wish

    def delete_source_file(self, input_file_path):
        from os import remove
        remove(input_file_path)


class Publish(GetInputFromConsole, GetInputFromFile):

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
    data_providing_way = GetInputFromConsole().read_data_providing_way()

    if data_providing_way == 'Console':
        publication_type = GetInputFromConsole().read_publication_type()
        user_text = GetInputFromConsole().read_text()

        if publication_type == 'News':
            input1 = News()
            city = input1.read_city()
            input1.publish_title(publication_type)
            input1.publish_text(user_text)
            input1.publish_city(city)
            input1.publish_current_date()
            input1.publish_last_block_line()
        elif publication_type == 'Private Ad':
            input2 = PrivateAd()
            date_until_actual = input2.read_date()
            input2.publish_title(publication_type)
            input2.publish_text(user_text)
            input2.publish_date(date_until_actual)
            input2.publish_days_left(date_until_actual)
            input2.publish_last_block_line()
        elif publication_type == 'Self Notes':
            input3 = Notes()
            tip_wish = input3.read_tip_wish()
            input3.publish_title(publication_type)
            input3.publish_text(user_text)
            input3.publish_tip(tip_wish)
            input3.publish_last_block_line()

    elif data_providing_way == 'File':

        input_file_path = GetInputFromFile().read_input_file_path()
        records_quantity = GetInputFromFile().read_records_quantity()

        if records_quantity == 'many':
            data = GetInputFromFile().read_many_rows_from_file(input_file_path)
        elif records_quantity == 'one':
            data = GetInputFromFile().read_one_row_from_file(input_file_path)

        for i in data:
            publication_type = GetInputFromFile().read_publication_type(i)
            user_text = GetInputFromFile().read_text(i)

            if publication_type == 'News':
                city = GetInputFromFile().read_city(i)
                input1 = News()
                input1.publish_title(publication_type)
                input1.publish_text(user_text)
                input1.publish_city(city)
                input1.publish_current_date()
                input1.publish_last_block_line()
            elif publication_type == 'Private Ad':
                date_until_actual = GetInputFromFile().read_date(i)
                input2 = PrivateAd()
                input2.publish_title(publication_type)
                input2.publish_text(user_text)
                input2.publish_date(date_until_actual)
                input2.publish_days_left(date_until_actual)
                input2.publish_last_block_line()
            elif publication_type == 'Self Notes':
                tip_wish = GetInputFromFile().read_tip_wish(i)
                input3 = Notes()
                input3.publish_title(publication_type)
                input3.publish_text(user_text)
                input3.publish_tip(tip_wish)
                input3.publish_last_block_line()
        else:
            GetInputFromFile().delete_source_file(input_file_path)


global file_to_save_data
file_to_save_data = open("MyFile.txt", "a")
main()
file_to_save_data.close()
