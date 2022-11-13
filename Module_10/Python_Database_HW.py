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
    def read_input_file_format(self):
        input_file_format = input('Please specify what is the format of file? \nPlease enter "txt", "json" or "xml" : ')
        input_file_format = input_file_format.lower().strip()

        if input_file_format not in ('txt', 'json', 'xml'):
            print('You entered incorrect value')
            quit()

        return input_file_format

    def read_input_file_path(self, input_file_format):
        input_file_path = input('Please specify path to the file containing data? '
                                '\nPlease enter file path or press "Enter" to use the default way: ')

        if input_file_format == 'txt' and input_file_path == '':
            input_file_path = 'input_from_file.txt'
        elif input_file_format == 'json' and input_file_path == '':
            input_file_path = 'input_from_file.json'
        elif input_file_format == 'xml' and input_file_path == '':
            input_file_path = 'input_from_xml.xml'

        return input_file_path

    def read_data_from_txt_file(self, input_file_path):
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

    def read_data_from_json_file(self, input_file_path):
        from json import load
        try:
            file_with_data = open(input_file_path, "r")
            json_data = load(file_with_data)
            list_for_all_publications = []

            for one_publication in json_data:
                additional_field = [*one_publication.keys()][2]
                one_publication_data = {'publication_type': one_publication['publication type'],
                                        'user_text': one_publication['text'],
                                        'additional_data': one_publication[additional_field]}
                list_for_all_publications.append(one_publication_data)
            file_with_data.close()

            return list_for_all_publications

        except FileNotFoundError:
            print('Incorrect path to file')
            quit()

    def read_data_from_xml_file(self, input_file_path):
        import xml.etree.ElementTree as ET
        try:
            tree = ET.parse('input_from_xml.xml')
            root = tree.getroot()
            list_for_all_publications = []

            for publication in root.findall('item'):
                list_for_one_publication = []
                for field in publication:
                    field_value = field.text.strip()
                    list_for_one_publication.append(field_value)
                one_publication_data = {'publication_type': list_for_one_publication[0],
                                        'user_text': list_for_one_publication[1],
                                        'additional_data': list_for_one_publication[2]}
                list_for_all_publications.append(one_publication_data)

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

    def publish_title(self, publication_type, file_to_save_data):
        file_to_save_data.write(publication_type + ' ' + (30 - len(publication_type) - 1) * '-')

    def publish_text(self, user_text, file_to_save_data):
        file_to_save_data.write('\n' + user_text)

    def publish_last_block_line(self, file_to_save_data):
        file_to_save_data.write('\n' + 30 * '-' + '\n\n\n')


class News(Publish):

    def publish_city(self, city_name, file_to_save_data):
        file_to_save_data.write('\n' + city_name)

    def get_current_date(self):
        from datetime import datetime
        return str(datetime.today())

    def publish_current_date(self, current_date, file_to_save_data):
        file_to_save_data.write(', ' + current_date)


class PrivateAd(Publish):

    def publish_date(self, actual_until_date, file_to_save_data):
        file_to_save_data.write('\n' + 'Actual until: ' + actual_until_date)

    def get_days_left(self, actual_until_date):
        from datetime import date, datetime

        actual_until_date = datetime.strptime(actual_until_date, "%Y-%m-%d")
        current_date = datetime.strptime(str(date.today()), "%Y-%m-%d")

        if actual_until_date < current_date:
            print('Please, note: Actual until date is earlier than the current date')

        days_left = str((actual_until_date - current_date).days)
        return days_left

    def publish_days_left(self, days_left, file_to_save_data):
        file_to_save_data.write(', ' + days_left + ' days left')


class Notes(Publish):

    def get_tip(self, tip_wish):
        if tip_wish == 'yes':
            return 'You are doing great! Keep going ;-;'

    def publish_tip(self, tip_wish, file_to_save_data):
        if tip_wish == 'yes':
            file_to_save_data.write('\n' + 'You are doing great! Keep going ;-;')


class ProvideFileContentStatistics:

    def publish_letters_statistics(self, file_to_save_data):
        from string import ascii_lowercase
        import csv

        with open(file_to_save_data, 'r') as input_file:
            file_content = input_file.read()

        count_all_letters = 0
        for i in file_content:
            if i.lower() in ascii_lowercase:
                count_all_letters += 1

        with open('Letters_Statistics.csv', 'w', newline='') as output_file:
            headers = ['letter', 'count_all', 'count_uppercase', 'percentage']
            row_to_write = csv.DictWriter(output_file, fieldnames=headers, delimiter='|')
            row_to_write.writeheader()

            for i in ascii_lowercase:
                letter = i
                count_letter = 0
                count_upper = 0
                percentage = 0

                for j in file_content:
                    if i == j.lower():
                        count_letter += 1
                        if i.upper() == j:
                            count_upper += 1

                if count_all_letters != 0:
                    percentage = round(count_letter / count_all_letters * 100, 2)

                if count_letter > 0:
                    row_to_write.writerow({'letter': letter,
                                           'count_all': count_letter,
                                           'count_uppercase': count_upper,
                                           'percentage': percentage})

    def publish_words_statistics(self, file_to_save_data):
        import csv

        with open(file_to_save_data, 'r') as input_file:
            file_content = input_file.read()

        for character_to_replace in [',', '.', '!', '?', '-', ':', ';']:
            if character_to_replace in file_content:
                file_content = file_content.replace(character_to_replace, '')

        words_list_from_file = []
        all_words_statistics = {}

        for word in file_content.split():
            if not word.isdigit():
                words_list_from_file.append(word.lower())

        for i in words_list_from_file:
            dict_key = i
            if dict_key in all_words_statistics.keys():
                for one_word_dict_key in all_words_statistics:
                    if one_word_dict_key == dict_key:
                        all_words_statistics[dict_key] = all_words_statistics.get(dict_key) + 1
            else:
                all_words_statistics[dict_key] = 1

        with open('Words_Statistics.csv', 'w', newline='') as output_file:
            for i in all_words_statistics:
                writer = csv.writer(output_file, delimiter='-')
                writer.writerow([i, all_words_statistics[i]])


class DBConnection:
    def __init__(self, database_name):
        import pyodbc
        with pyodbc.connect('Driver=SQLite3 ODBC Driver;'
                            f'Database={database_name}') as self.connection:
            self.cursor = self.connection.cursor()

            self.cursor.tables()
            all_tables = self.cursor.fetchall()

            table_names = []
            for table in all_tables:
                table_names.append(table.table_name)

            if 'News' not in table_names:
                self.cursor.execute('create table News (text, city, current_date)')
                self.connection.commit()
            if 'Private_Ad' not in table_names:
                self.cursor.execute('create table Private_Ad (text, actual_until, days_left)')
                self.connection.commit()
            if 'Self_Notes' not in table_names:
                self.cursor.execute('create table Self_Notes (text, tip)')
                self.connection.commit()

    def select(self, field_name, table_name):
        self.cursor.execute(f'select {field_name} from {table_name}')
        return self.cursor.fetchall()

    def insert(self, field_values, table_name):
        self.cursor.execute(f'insert into {table_name} values ({field_values})')
        self.connection.commit()
        return "DB was updated"

    def select_all(self, table_name):
        self.cursor.execute(f"select * from {table_name}")
        return self.cursor.fetchall()


def main():
    data_providing_way = GetInputFromConsole().read_data_providing_way()
    connection = DBConnection('test.db')

    if data_providing_way == 'Console':
        publication_type = GetInputFromConsole().read_publication_type()
        user_text = GetInputFromConsole().read_text()

        file_to_save_data = open(filename, "a")
        if publication_type == 'News':
            input1 = News()
            city = input1.read_city()
            current_date = input1.get_current_date()
            input1.publish_title(publication_type, file_to_save_data)
            input1.publish_text(user_text, file_to_save_data)
            input1.publish_city(city, file_to_save_data)
            input1.publish_current_date(current_date, file_to_save_data)
            input1.publish_last_block_line(file_to_save_data)
            field_values = f"'{user_text}', '{city}', '{current_date}'"
            result_all = connection.select('text', 'News')
            result = []
            for j in result_all:
                result.append(j[0])
            if user_text not in result:
                connection.insert(field_values, 'News')
            else:
                print("This row is already present in DB")
        elif publication_type == 'Private Ad':
            input2 = PrivateAd()
            date_until_actual = input2.read_date()
            days_left = input2.get_days_left(date_until_actual)
            input2.publish_title(publication_type, file_to_save_data)
            input2.publish_text(user_text, file_to_save_data)
            input2.publish_date(date_until_actual, file_to_save_data)
            input2.publish_days_left(days_left, file_to_save_data)
            input2.publish_last_block_line(file_to_save_data)
            field_values = f"'{user_text}', '{date_until_actual}', '{days_left}'"
            result_all = connection.select('text', 'Private_Ad')
            result = []
            for j in result_all:
                result.append(j[0])
            if user_text not in result:
                connection.insert(field_values, 'Private_Ad')
            else:
                print("This row is already present in DB")
        elif publication_type == 'Self Notes':
            input3 = Notes()
            tip_wish = input3.read_tip_wish()
            tip = input3.get_tip(tip_wish)
            input3.publish_title(publication_type, file_to_save_data)
            input3.publish_text(user_text, file_to_save_data)
            input3.publish_tip(tip_wish, file_to_save_data)
            input3.publish_last_block_line(file_to_save_data)
            field_values = f"'{user_text}', '{tip}'"
            result_all = connection.select('text', 'Self_Notes')
            result = []
            for j in result_all:
                result.append(j[0])
            if user_text not in result:
                connection.insert(field_values, 'Self_Notes')
            else:
                print("This row is already present in DB")
        file_to_save_data.close()

    elif data_providing_way == 'File':

        file_format = GetInputFromFile().read_input_file_format()
        input_file_path = GetInputFromFile().read_input_file_path(file_format)

        if file_format == 'txt':
            data = GetInputFromFile().read_data_from_txt_file(input_file_path)
        elif file_format == 'json':
            data = GetInputFromFile().read_data_from_json_file(input_file_path)
        elif file_format == 'xml':
            data = GetInputFromFile().read_data_from_xml_file(input_file_path)

        for i in data:
            publication_type = GetInputFromFile().read_publication_type(i)
            user_text = GetInputFromFile().read_text(i)
            file_to_save_data = open(filename, "a")

            if publication_type == 'News':
                city = GetInputFromFile().read_city(i)
                input1 = News()
                current_date = input1.get_current_date()
                input1.publish_title(publication_type, file_to_save_data)
                input1.publish_text(user_text, file_to_save_data)
                input1.publish_city(city, file_to_save_data)
                input1.publish_current_date(current_date, file_to_save_data)
                input1.publish_last_block_line(file_to_save_data)
                field_values = f"'{user_text}', '{city}', '{current_date}'"
                result_all = connection.select('text', 'News')
                result = []
                for j in result_all:
                    result.append(j[0])
                if user_text not in result:
                    connection.insert(field_values, 'News')
                else:
                    print("This row is already present in DB")
            elif publication_type == 'Private Ad':
                date_until_actual = GetInputFromFile().read_date(i)
                input2 = PrivateAd()
                days_left = input2.get_days_left(date_until_actual)
                input2.publish_title(publication_type, file_to_save_data)
                input2.publish_text(user_text, file_to_save_data)
                input2.publish_date(date_until_actual, file_to_save_data)
                input2.publish_days_left(days_left, file_to_save_data)
                input2.publish_last_block_line(file_to_save_data)
                field_values = f"'{user_text}', '{date_until_actual}', '{days_left}'"
                result_all = connection.select('text', 'Private_Ad')
                result = []
                for j in result_all:
                    result.append(j[0])
                if user_text not in result:
                    connection.insert(field_values, 'Private_Ad')
                else:
                    print("This row is already present in DB")
            elif publication_type == 'Self Notes':
                tip_wish = GetInputFromFile().read_tip_wish(i)
                input3 = Notes()
                tip = input3.get_tip(tip_wish)
                input3.publish_title(publication_type, file_to_save_data)
                input3.publish_text(user_text, file_to_save_data)
                input3.publish_tip(tip_wish, file_to_save_data)
                input3.publish_last_block_line(file_to_save_data)
                field_values = f"'{user_text}', '{tip}'"
                result_all = connection.select('text', 'Self_Notes')
                result = []
                for j in result_all:
                    result.append(j[0])
                if user_text not in result:
                    connection.insert(field_values, 'Self_Notes')
                else:
                    print("This row is already present in DB")
            file_to_save_data.close()

        else:
            GetInputFromFile().delete_source_file(input_file_path)

    file_statistics = ProvideFileContentStatistics()
    file_statistics.publish_letters_statistics(filename)
    file_statistics.publish_words_statistics(filename)

    print(connection.select_all('News'))
    print(connection.select_all('Private_Ad'))
    print(connection.select_all('Self_Notes'))


filename = 'MyFile.txt'
main()
