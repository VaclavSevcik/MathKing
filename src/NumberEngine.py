from src.exceptions import ParseConfigException
import random

# TODO constrain number of example
# TODO - constrain - more then EXAMPLE_TO_PAGE example overflow one page - need count page and write to previous page in method __writeExamplesToPDF
EXAMPLE_TO_PAGE = 132

class NumberEngine:
    '''
    The class NumberEngine provides generate examples according to configuration from application window.
    '''

    lowBoundNumber = 0
    highBoundNumber = 0

    addition = False
    subtraction = False
    multiplication = False
    division = False

    def __prepare_data(self, information_from_GUI):
        ''' The method sets all inner data from argument and check if their is regular.

        :param dict information_from_GUI: The dictionary with information passed from GUI.
        :return None:
        '''
        self.addition = information_from_GUI['plus']
        self.subtraction = information_from_GUI['minus']
        self.multiplication = information_from_GUI['multiplication']
        self.division = information_from_GUI['division']

        self.allowedOperation = []
        if self.addition:
            self.allowedOperation.append('addition')
        if self.subtraction:
            self.allowedOperation.append('subtraction')
        if self.multiplication:
            self.allowedOperation.append('multiplication')
        if self.division:
            self.allowedOperation.append('division')

        # check is lower range is number
        try:
            int(information_from_GUI['range_from'])
        except:
            raise ParseConfigException('parseExceptionFromIsInteger')

        # check is higher range is number
        try:
            int(information_from_GUI['range_to'])
        except:
            raise ParseConfigException('parseExceptionFromIsInteger')

        # check low boundary is lower than high boundary
        if information_from_GUI['range_from'] > information_from_GUI['range_to']:
            raise ParseConfigException('parseExceptionFromGreaterThenTo')

        # set boundary values
        self.lowBoundNumber = int(information_from_GUI['range_from'])
        self.highBoundNumber = int(information_from_GUI['range_to'])

        # check the amount of examples is number
        try:
            int(information_from_GUI['amount_of_examples'])
        except:
            raise ParseConfigException('parseExceptionAmountOfExampleIsInteger')

        # check the amount of examples is greater than zero
        if int(information_from_GUI['amount_of_examples']) < 0:
            raise ParseConfigException('parseExceptionAmountOfExampleIsGreaterThanZero')

        # Number of example to generate
        self.numberOfExample = int(information_from_GUI['amount_of_examples'])

        # set number of example to max number example which fill one page.
        if self.numberOfExample > EXAMPLE_TO_PAGE:
            self.numberOfExample = EXAMPLE_TO_PAGE

        self.listOfExamples = []

    def __create_example(self):
        ''' The method creates one example with expression (exp sign exp)

        :return str: The expression in string.
        '''

        # generate two random number from low bound to high bound
        first_number = self.__getRandomNumber(self.lowBoundNumber, self.highBoundNumber)
        second_number = self.__getRandomNumber(self.lowBoundNumber, self.highBoundNumber)

        # draw enable operator
        if not self.allowedOperation:
            return ""
        operation = random.choice(self.allowedOperation)

        # The string contains example
        example = ""

        # Addition case
        if operation == "addition":
            example = str(first_number) + " + " + str(second_number)

        # Multiplication case
        elif operation == "multiplication":
            example = str(first_number) + " * " + str(second_number)

        # Subtraction case
        elif operation == "subtraction":
            while second_number > first_number:
                first_number = self.__getRandomNumber(self.lowBoundNumber, self.highBoundNumber)
                second_number = self.__getRandomNumber(self.lowBoundNumber, self.highBoundNumber)
            example = str(first_number) + " - " + str(second_number)

        # Division case
        elif operation == "division":
            # generates new value when one of number is negative or division has reminder
            while (first_number < 0 and second_number <= 0) or first_number % second_number != 0:
                first_number = self.__getRandomNumber(self.lowBoundNumber, self.highBoundNumber)
                second_number = self.__getRandomNumber(self.lowBoundNumber, self.highBoundNumber)
            example = str(first_number) + " / " + str(second_number)
        return example

    def __getRandomNumber(self, start_int, stop_int):
        ''' The method generate one number from interval.
         The method uses library random which provides Mersenne Twister pseudorandom generator.

        :param int start_int: The lower limit.
        :param int stop_int: The higher limit.
        :return int: The pseudorandom number from range of limits in argument.
        '''
        return random.randint(start_int, stop_int)

    def generateExamples(self, information_from_GUI):
        ''' The method generate amount examples according to user input.

        :param dict information_from_GUI: The dictionary with information passed from GUI.
        :return [str]: The list with examples.
        '''

        # initialize number engine
        self.__prepare_data(information_from_GUI)

        # generate amount of example
        for i in range(self.numberOfExample):
            self.listOfExamples.append(self.__create_example())

        return self.listOfExamples