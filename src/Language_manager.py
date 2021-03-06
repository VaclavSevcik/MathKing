import sys

class LanguageManager:
    '''
    The class provides language mutations for other module.
    '''

    # Text constant language read in its language
    CZECH_NAME_OF_LANGUAGE = 'Česky'
    ENGLISH_NAME_OF_LANGUAGE = 'English'

    # the available language mutations
    language_dictionaries = {CZECH_NAME_OF_LANGUAGE: None, ENGLISH_NAME_OF_LANGUAGE: None}

    # list with all keywords using in program
    list_of_keys = ['title', 'number_of_examples', 'number_of_copies', 'number_range', 'text_range_from', 'text_range_to', 'generate',
                    'save_files', 'help', 'close', 'warning', 'type_of_sign', 'plus', 'minus', 'multiplication',
                    'division', 'saveText', 'saveLocation', 'nameOfProgramToFileName', 'parseExceptionFromIsInteger',
                    'parseExceptionToIsInteger', 'parseExceptionFromGreaterThenTo', 'parseExceptionAmountOfExampleIsInteger',
                    'parseExceptionAmountOfExampleIsGreaterThanZero', 'text_help']

    # initialize dictionaries
    czech = {}
    english = {}

    # Initialize actual dictionary
    actual_language_dictionary = czech

    def __init__(self):
        '''
        The method initializes dictionaries with records and check them.
        '''

        self.__init_czech_mutation()
        self.__init_english_mutation()
        self.__check_keywords_in_dictionaries()

    def __check_keywords_in_dictionaries(self):
        '''
        The method checks if all language has defined all keywords. If not, write log which keyword not defined to stderr.
        '''

        self.language_dictionaries = {self.CZECH_NAME_OF_LANGUAGE: self.czech, self.ENGLISH_NAME_OF_LANGUAGE: self.english}

        # check all language if is defined all keywords
        for language in self.language_dictionaries:

            # get list of language keys
            keywords = self.language_dictionaries[language]

            # check language keywords towards the list of keywords
            missing_word_in_language = list(set(self.list_of_keys) - set(keywords))

            # Write to terminal warning text which keyword is not defined in which language
            if missing_word_in_language:
                print("In language " + language + " is not defined this keywords " +
                      (', '.join([str(item) for item in missing_word_in_language])) + "!", file=sys.stderr)


    def set_language(self, language):
        ''' The method sets language of application.

        :param language: The new language to set.
        :return None:
        '''
        if language == self.ENGLISH_NAME_OF_LANGUAGE:
            self.actual_language_dictionary = self.english
        elif language == self.CZECH_NAME_OF_LANGUAGE:
            self.actual_language_dictionary = self.czech

    def get_string(self, key):
        ''' The method gets string according to written key.

        :param key: The key of dictionary.
        :return str: The sentence from dictionary.
        '''
        try:
            return self.actual_language_dictionary[key]
        except KeyError: # TODO try it
            return ""

    def get_supported_languages(self):
        ''' The method gets list with supported languages.

        :return [str]: The list with supported languages.
        '''
        return list(self.language_dictionaries.keys())

    def __init_czech_mutation(self):
        ''' The method sets dictionary with czech language.

        :return None:
        '''
        # czech mutation
        self.czech['title'] = 'Generátor krále počtů'
        self.czech['number_of_examples'] = 'Počet příkladů'
        self.czech['number_of_copies'] = 'Počet kopií'
        self.czech['number_range'] = 'Rozsah čísel'
        self.czech['text_range_from'] = 'Od'
        self.czech['text_range_to'] = 'Do'
        self.czech['generate'] = 'Generovat'
        self.czech['save_files'] = 'Uložit soubory'
        self.czech['help'] = 'Nápověda'
        self.czech['close'] = 'Zavřít'
        self.czech['warning'] = 'Upozornění'

        self.czech['type_of_sign'] = 'Znaménka'
        self.czech['plus'] = 'Sčítání (+)'
        self.czech['minus'] = 'Odčítání (-)'
        self.czech['multiplication'] = 'Násobení (*)'
        self.czech['division'] = 'Dělení (/)'

        self.czech['saveText'] = 'Vyberte složku'
        self.czech['saveLocation'] = 'Uložit do'

        self.czech['nameOfProgramToFileName'] = 'PocetniKral'

        self.czech['parseExceptionFromIsInteger'] = 'Ve volbě rozsahu číslo určující nejnižší generované číslo obsahuje znaky, které neodpovídají zápisu čísla.'
        self.czech['parseExceptionToIsInteger'] = 'Ve volbě rozsahu číslo určující nejvyšší generované číslo obsahuje znaky, které neodpovídají zápisu čísla.'
        self.czech['parseExceptionFromGreaterThenTo'] = 'Ve volbě rozsahu je číslo určující nejnižší generované číslo větší než číslo určující nejvyšší generované číslo.'
        self.czech['parseExceptionAmountOfExampleIsInteger'] = 'Počet generovaných příkladů není zadán číslem. Je v něm znak neodpovídající číslu.'
        self.czech['parseExceptionAmountOfExampleIsGreaterThanZero'] = 'Počet generovaných příkladů je nižší než nula, proto není možné je vygenerovat.'
        self.czech['parseExceptionAmountOfCopiesIsInteger'] = 'Počet generovaných kopií není zadán číslem. Je v něm znak neodpovídající číslu.'
        self.czech['parseExceptionAmountOfCopiesIsGreaterThanZero'] = 'Počet generovaných kopií je nižší než nula, proto není možné je vygenerovat.'

        self.czech['text_help'] = "Aplikace pro generování příkladů pro učitele prvního stupně základních škol." \
                                  " Generátor dokáže generovat příklady v rozsahu čísel nastavených uživatelem." \
                                  " Uživatel si může zvolit operace se kterými budou příklady generovány. \n" \
                                  "Autor: Václav Ševčík\n\n" \
                                  "Popis:\n" \
                                  "Pro využítí generátoru lze zvolit množství příkladů, které se vygenerují a v kolika kopiích se tyto příklady uloží do PDF. " \
                                  "Lze zvolit rozsah čísel v kterém budou čísla generovány. Poté lze zvolit operace se kterýma budou příklady generovány. " \
                                  "Poté lze vybrat složku do kterého budou vygenerované soubory uloženy. Následuje tlačítko pro znovu vygenerování příkladu " \
                                  "a tlačítko pro uložení vygenerovaných příkladů. Poslední dvě tlačítka mají za úkol zavřít aplikaci a zobrazit nápovědu."

    def __init_english_mutation(self):
        ''' The method sets dictionary with english language.

        :return None:
        '''
        self.english['title'] = 'Math king generator'
        self.english['number_of_examples'] = 'Number of examples'
        self.english['number_of_copies'] = 'Number of copies'
        self.english['number_range'] = 'Number range'
        self.english['text_range_from'] = 'From'
        self.english['text_range_to'] = 'To'
        self.english['generate'] = 'Generate'
        self.english['save_files'] = 'Save files'
        self.english['help'] = 'Help'
        self.english['close'] = 'Close'
        self.english['warning'] = 'Warning'

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
        self.english['parseExceptionFromGreaterThenTo'] = 'The lower limit of generated number is greater than greater limit.'
        self.english['parseExceptionAmountOfExampleIsInteger'] = 'The number of example to generate is not write with digit or sign.'
        self.english['parseExceptionAmountOfExampleIsGreaterThanZero'] = 'The number of example to generate is lower than zero.'
        self.english['parseExceptionAmountOfCopiesIsInteger'] = 'The number of copies to generate is not write with digit or sign.'
        self.english['parseExceptionAmountOfCopiesIsGreaterThanZero'] = 'The number of copies to generate is lower than zero.'

        self.english['text_help'] = "The generator of examples (basic math) for elementary school teachers." \
                                    "Author: Václav Ševčík\n\n" \
                                    "Description:\n" \
                                    "The user chooses scope of generated numbers and operation which will be between them." \
                                    " The user can choose how many examples and how many copies will be generated to save PDF." \
                                    " The user can choose scope of generated numbers and operation which will be use." \
                                    " The user can choose the folder to save. When the user do not choose folder, the file will be saved to project directory." \
                                    " The buttons bottom consists of the button for generating example, save example to file, closing app button and button to show help."
