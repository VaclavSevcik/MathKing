
class LanguageManager:
    ''' The class provides language mutations for other module.

    '''

    # the available language mutations
    list_of_languages = ['Česky', 'English']

    # initialize dictionaries
    czech = {}
    english = {}

    # Initialize actual dictionary
    language_dictionary = czech

    def __init__(self):
        '''
        The method nitializes dictionaries with records and check them.
        '''

        # TODO check all words are defined in all languages... All keyword in list and check in laguage all - first size - after find not defined...
        self.__init_czech_mutation()
        self.__init_english_mutation()

    def set_language(self, language):
        ''' The method sets language of application.

        :param language: The new language to set.
        :return None:
        '''
        if language == "English":
            self.language_dictionary = self.english
        elif language == "Česky":
            self.language_dictionary = self.czech

    def get_string(self, key):
        ''' The method gets string according to written key.

        :param key: The key of dictionary.
        :return str: The sentence from dictionary.
        '''
        try:
            return self.language_dictionary[key]
        except KeyError: # TODO try it
            return ""

    def get_supported_languages(self):
        ''' The method gets list with supported languages.

        :return [str]: The list with supported languages.
        '''
        return self.list_of_languages

    def __init_czech_mutation(self):
        ''' The method sets dictionary with czech language.

        :return None:
        '''
        # czech mutation
        self.czech['title'] = 'Generátor krále počtů'
        self.czech['number_of_examples'] = 'Počet příkladů'
        self.czech['number_range'] = 'Rozsah čísel'
        self.czech['text_range_from'] = 'Od'
        self.czech['text_range_to'] = 'Do'
        self.czech['generate'] = 'Generovat'
        self.czech['save_files'] = 'Uložit soubory'
        self.czech['help'] = 'Nápověda'
        self.czech['close'] = 'Zavřít'

        self.czech['type_of_sign'] = 'Znaménka'
        self.czech['plus'] = 'Sčítání (+)'
        self.czech['minus'] = 'Odčítání (-)'
        self.czech['multiplication'] = 'Násobení (*)'
        self.czech['division'] = 'Dělení (/)'

        self.czech['saveText'] = 'Vyberte složku'
        self.czech['saveLocation'] = 'Uložit do'

        self.czech['nameOfProgramToFileName'] = 'MatematickyKral'

        self.czech['parseExceptionFromIsInteger'] = 'Ve volbě rozsahu číslo určující nejnižší generované číslo obsahuje znaky, které neodpovídají zápisu čísla.'
        self.czech['parseExceptionToIsInteger'] = 'Ve volbě rozsahu číslo určující nejvyšší generované číslo obsahuje znaky, které neodpovídají zápisu čísla.'
        self.czech['parseExceptionFromGreaterThenTO'] = 'Ve volbě rozsahu je číslo určující nejnižší generované číslo větší než číslo určující nejvyšší generované číslo.'
        self.czech['parseExceptionAmountOfExampleIsInteger'] = 'Počet generovaných příkladů není zadán číslem. Je v něm znak neodpovídající číslu.'
        self.czech['parseExceptionAmountOfExampleIsGreaterThanZero'] = 'Počet generovaných příkladů je nižší než nula, proto není možné je vygenerovat.'

    def __init_english_mutation(self):
        ''' The method sets dictionary with english language.

        :return None:
        '''
        # TODO BUG not show all text in english
        self.english['title'] = 'Math king generator'
        self.english['number_of_examples'] = 'Number of examples'
        self.english['number_range'] = 'Number range'
        self.english['text_range_from'] = 'From'
        self.english['text_range_to'] = 'To'
        self.english['generate'] = 'Generate'
        self.english['save_files'] = 'Save files'
        self.english['help'] = 'Help'
        self.english['close'] = 'Close'

        self.english['type_of_sign'] = 'Type of signs'
        self.english['plus'] = 'Addition (+)'
        self.english['minus'] = 'Subtraction (-)'
        self.english['multiplication'] = 'Multiplication (*)'
        self.english['division'] = 'Division (/)'

        self.english['saveText'] = 'Browse'
        self.english['saveLocation'] = 'Choose directory'

        self.english['nameOfProgramToFileName'] = 'MathKing'

        self.english['parseExceptionFromIsInteger'] = 'The lower limit of number limit is not number. The string contain symbols which is not digit or sign.'
        self.english['parseExceptionToIsInteger'] = 'The higher limit of number limit is not number. The string contain symbols which is not digit or sign.'
        self.english['parseExceptionFromGreaterThenTO'] = 'The lower limit of generated number is greater than greater limit.'
        self.english['parseExceptionAmountOfExampleIsInteger'] = 'The number of example to generate is not write with digit or sign.'
        self.english['parseExceptionAmountOfExampleIsGreaterThanZero'] = 'The number of example to generate is lower than zero.'
