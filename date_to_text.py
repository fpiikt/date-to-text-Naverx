"""
    Автор: Макаров Павел, группа №P3355

    Программа конвертирует дату в формате DD.MM.YYYY HH:MM:SS в диапазоне
    от 01.01.1001 00:00:00 до 31.12.2999 59:59:59 в прописной текст
"""




class DateToText:    
    """   
    Класс, в котором происходит преобразование даты формата
    DD.MM.YYYY HH:MM:SS в текст
    date:str - поле, заополняемое принимаемым значением
    """



    under_20 = ['ноль', 'один', 'два', 'три', 'четыре', 'пять',
                'шесть', 'семь','восемь','девять','десять','одиннадцать',
                'двенадцать','тринадцать','четырнадцать','пятнадцать',
                'шестнадцать','семьнадцать','восемьнадцать','девятнадцать']
    
    tens = ['','','двадцать','тридцать','сорок','пятьдесят','шестьдесят','семьдесят','восемьдестя','девяносто']

    hundreds = ['','сто','двести','триста','четыреста','пятьсот','шестьсот','семьсот','восемьсот','девятьсот']


    def __init__(self, date):
        self.date = date
        

    def date_to_text(self):
        """
        Функция преобразующая полученную дату из поля date в прописной текст
        и возвращающая его в переменной date_as_words: str
        """
        
        #try:
        #    self.check_format(self.date)
        #except:
        #    print(self.date, "Неверный формат")
        #   return None
        
            
        date = self.date.split(' ')[0].split('.') + self.date.split(' ')[1].split(':')
        
        date_as_words = ''
        date_as_words += self.convert_day(date[0])
        date_as_words += ' '+ self.convert_month(date[1])
        date_as_words += ' '+ self.convert_year(date[2])
        date_as_words += ' '+ self.convert_hour(date[3])
        date_as_words += ' '+ self.convert_minute(date[4])
        date_as_words += ' '+ self.convert_second(date[5])

        print(self.date, date_as_words, '\n')

        return date_as_words

    
    def convert_day(self,day):
        """
        Функция принимает day : str - число месяца в виде строки и возвращает
        его запись прописью 
        """
        
        days = ['никакое', 'первое', 'второе', 'третье', 'четвёртое',
        'пятое', 'шестое', 'седьмое', 'восьмое',
        'девятое', 'десятое', 'одиннадцатое', 'двенадцатое',
        'тринадцатое', 'четырнадцатое', 'пятнадцатое', 'шестнадцатое',
        'семнадцатое', 'восемнадцатое', 'девятнадцатое', 'двадцатое',
        'двадцать первое', 'двадцать второе', 'двадцать третье',
        'двадацать четвёртое', 'двадцать пятое', 'двадцать шестое',
        'двадцать седьмое', 'двадцать восьмое', 'двадцать девятое',
        'тридцатое', 'тридцать первое']

        return days[int(day)]
    
    

    def convert_month(self, month):
        """
        Функция принимает month : str - номер месяца в виде строки и возвращает
        его запись прописью 
        """
        
        months = ['','января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
           'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
        return months[int(month)]
    
    def convert_year(self, year):
        """
        Функция принимает year : str - год  в виде строки и возвращает
        его запись прописью 
        """
        between_1_and_10 = ['', 'первого','второго','третьего','четвёртого','пятого','шестого','седьмого','восьмого','девятого']
        year_tens = ['','десятого','двадцатого','тридцатого','сорокового','пятидесятого','шестидесятого','семидесятого','восьмидесятого','девяностого']
        between_11_and_20 = ['-','одиннадцатого','двенадцатого','тринадцатого','четырнадцатого','пятнадцатого',
                             'шестнадцатого','семнадцатого','восемнадцатого','девятнадцатого']
        string = ''
        string += 'одна тысяча ' if year[0] == '1' else 'две тысячи '
        string += '' if year[1] == '0' else self.hundreds[int(year[1])] + ' '
        if int(year[2]+year[3]) in range(11,20):
            string += between_11_and_20[int(year[3])]
        elif year[3] == '0':
            string += year_tens[int(year[2])]
        else:
            string += self.tens[int(year[2])] + ' ' + between_1_and_10[int(year[3])]
        
        if int(year) ==2000:
            string = 'двухтысячного'
        string += ' года'
        return string
        
    def convert_hour(self, hour):
        """
        Функция принимает hour : str - число часы в виде строки и возвращает
        его запись прописью 
        """

        hour = int(hour)
        
        if hour%10 == 1 and hour !=11:
            form = 'час'
        elif hour%10 == 0 or hour%10 in range(5,10) or hour in range(10,20):
            form = 'часов'
        else:
            form = 'часа'
        number = self.under_20[hour] if hour in range(1,20) else self.tens[hour//10] +' '*(hour and True)+ self.under_20[hour%10]         
 
        return number + ' ' + form
    
    def convert_minute(self, minute):
        """
        Функция принимает minute : str - минуты в виде строки и возвращает
        его запись прописью 
        """

        minute = int(minute)
        if minute%10 == 1 and minute !=11:
            form = 'минута'
        elif minute%10 == 0 or minute%10 in range(5,10) or minute in range(10,20):
            form = 'минут'
        else:
            form = 'минуты'
        number = self.under_20[minute] if minute in range(1,20) else self.tens[minute//10] +' '*(minute and True)+ self.under_20[minute%10]         
 
        return number + ' ' + form
    
    def convert_second(self, second):
        """
        Функция принимает second : str - секунды в виде строки и возвращает
        его запись прописью 
        """

        second = int(second)
        if second%10 == 1 and second != 11:
            form = 'секунда'
        elif second%10 in [0] or second%10 in range(5,10) or second in range(10,20):
            form = 'секунд'
        else:
            form = 'секунды'
        number = self.under_20[second] if second in range(1,20) else self.tens[second//10] + ' '*(second and True) + self.under_20[second%10]         
 
        return number + ' ' + form
    
    
    def check_format(self, date):
        """Функция принимает дату date и проверяет её соответствие формату и диапазону"""
        
        date = self.date.split(' ')[0].split('.')+self.date.split(' ')[1].split(':')
        
        day, month, year, hour, minute, second = int(date[0]), int(date[1]), int(date[2]), int(date[3]), int(date[4]), int(date[5]), 
        
        assert day in range(1,32)
        assert month in range(1,13)
        assert year in range(1001,3000)
        assert hour in range(0, 25)
        assert minute in range(0,61)
        assert second in range(0,61)

            

        
if __name__ == '__main__':
    date_1 = DateToText('27.09.2019 23:24:12')
    assert date_1.date_to_text() == "двадцать седьмое сентября две тысячи девятнадцатого года двадцать три часа двадцать четыре минуты двенадцать секунд", "ошибка в тесте 1"
    
    date_2 = DateToText('06.10.1990 23:45:06')
    assert date_2.date_to_text() == 'шестое октября одна тысяча девятьсот девяностого года двадцать три часа сорок пять минут шесть секунд', "ошибка в тесте 2"  

    date_3 = DateToText('11.11.1111 11:11:11')
    assert date_3.date_to_text() == 'одиннадцатое ноября одна тысяча сто одиннадцатого года одиннадцать часов одиннадцать минут одиннадцать секунд', "ошибка в тесте 3"  

    date_4 = DateToText('01.01.2000 00:00:00')
    assert date_4.date_to_text() == "первое января двухтысячного года ноль часов ноль минут ноль секунд", "ошибка в тесте 4"

    date_5 = DateToText('31.12.2999 23:59:59')
    assert date_5.date_to_text() == "тридцать первое декабря две тысячи девятьсот девяносто девятого года двадцать три часа пятьдесят девять минут пятьдесят девять секунд", "ошибка в тесте 5"

    date_6 = DateToText('23.02.2077 12:34:45')
    assert date_6.date_to_text() == "двадцать третье февраля две тысячи семьдесят седьмого года двенадцать часов тридцать четыре минуты сорок пять секунд", "ошибка в тесте 6"

    print('Ошибок не обнаружено')
    
    #date_4 = DateToText('qwertyu')
    #assert date_4.date_to_text() == '' 
    
    #date_5 = DateToText('9999.09.1333 45:17:59')
    #assert date_5.date_to_text() == '' 
    
    
