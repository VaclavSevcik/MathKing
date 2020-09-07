import PySimpleGUI as sg
import src.PDFCreator as PDFCreator
import src.NumberEngine as NumberEngine
import src.Language_manager as Language_manager
from src.exceptions import ParseConfigException

def get_layout(language_manager):
    ''' The method sets layout to return.

    :param Language_manager language_manager: Manager of language mutation and translation of sentence.
    :return: The method returns layout of generator.
    '''
    return [[sg.Combo(language_manager.get_supported_languages(), default_value="Česky", enable_events=True, key="language")],
              [sg.Text(language_manager.get_string('number_of_examples'), key='number_of_examples', size=(16, 1)), sg.InputText(key="amount_of_examples", size=(6, 1), default_text=30),
               sg.Text(language_manager.get_string('number_of_copies'), key='number_of_copies', size=(15, 1)), sg.InputText(key="amount_of_copies", size=(6, 1), default_text=20) ],
              [sg.Text(language_manager.get_string('number_range'), key='number_range', size=(12,1))],
              rangeForm,
              [sg.Text(language_manager.get_string('type_of_sign'), key='type_of_sign', size=(12,1))],
              listOfSigns,
              [sg.Text(language_manager.get_string('saveLocation'), key='saveLocation', size=(15,1)), directoryButton],
              listOfButtons]


def actualize_window_layout(language_manager):
    ''' The method actualize text in window layout according set language.

    :param Language_manager language_manager: Manager of language mutation and translation of sentence.
    :return: None
    '''

    window.TKroot.title(language_manager.get_string('title'))
    window.elem('number_of_examples').update(language_manager.get_string('number_of_examples'))
    window.elem('number_of_copies').update(language_manager.get_string('number_of_copies'))
    window.elem('number_range').update(language_manager.get_string('number_range'))
    window.elem('text_range_from').update(language_manager.get_string('text_range_from'))
    window.elem('text_range_to').update(language_manager.get_string('text_range_to'))

    window.elem('generate').update(language_manager.get_string('generate'))
    window.elem('save_files').update(language_manager.get_string('save_files'))
    window.elem('help').update(language_manager.get_string('help'))
    window.elem('close').update(language_manager.get_string('close'))

    window.elem('type_of_sign').update(language_manager.get_string('type_of_sign'))
    window.elem('plus').update(text=language_manager.get_string('plus'))
    window.elem('minus').update(text=language_manager.get_string('minus'))
    window.elem('multiplication').update(text=language_manager.get_string('multiplication'))
    window.elem('division').update(text=language_manager.get_string("division"))

    window.elem('saveText').update(language_manager.get_string('saveText'))
    window.elem('saveLocation').update(language_manager.get_string('saveLocation'))
    window.refresh()


def check_copies_input(number_of_copies):
    # check the amount of copies is number
    try:
        int(number_of_copies)
    except:
        raise ParseConfigException('parseExceptionAmountOfCopiesIsInteger')

    # check the amount of copies is greater than zero
    if int(number_of_copies) < 0:
        raise ParseConfigException('parseExceptionAmountOfCopiesIsGreaterThanZero')

    return int(number_of_copies)

if __name__ == '__main__':

    # create object for printing to PDF
    pdf_creator = PDFCreator.PDFCreator()
    number_engine = NumberEngine.NumberEngine()
    language_manager = Language_manager.LanguageManager()

    # set color theme for application
    sg.theme('SystemDefaultForReal')
    #print(sg.theme_list()) # to print themes to choose one

    # list of check boxes
    rangeForm = [sg.Text(language_manager.get_string('text_range_from'), key='text_range_from', size=(5, 1)),
                 sg.InputText(key="range_from", size=(10, 1), default_text=1),
                 sg.Text(language_manager.get_string('text_range_to'), key='text_range_to', size=(5, 1)),
                 sg.InputText(key="range_to", size=(10, 1), default_text=10)]

    # Choose of signs
    listOfSigns = [sg.Checkbox(language_manager.get_string('plus'), key='plus', default=True),
                   sg.Checkbox(language_manager.get_string('minus'), key='minus', default=True),
                   sg.Checkbox(language_manager.get_string('multiplication'), key='multiplication', default=True),
                   sg.Checkbox(language_manager.get_string('division'), key="division", default=True)]

    directoryButton = sg.FolderBrowse(button_text=language_manager.get_string('saveText'), key='saveText', initial_folder="./")


    # set list of buttons
    listOfButtons = [sg.Button(language_manager.get_string('generate'), key='generate'),
    sg.Button(language_manager.get_string('save_files'), key='save_files'),
    sg.Button(language_manager.get_string('close'), key='close'),
    sg.Help(language_manager.get_string('help'), key='help')]

    # Create the Window
    window = sg.Window(language_manager.get_string('title'), get_layout(language_manager), auto_size_text=True)

    # Initialize generated examples to empty string
    generated_examples = ""

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        try:
            # Read events and configuration information from window
            event, configurationInformation = window.read()

            # Catch event to close window
            if event == sg.WIN_CLOSED or event == 'close':  # if user closes window or clicks cancel
                break

            # set language before do action
            if configurationInformation['language'] in language_manager.get_supported_languages():
                language_manager.set_language(configurationInformation['language'])

            if event == "generate":
                generated_examples = number_engine.generateExamples(configurationInformation)

            if event == 'save_files':
                pdf_creator.printExampleToPDF(generated_examples, language_manager, configurationInformation['saveText'], check_copies_input(configurationInformation['amount_of_copies']))

            if event == 'help':
                sg.Popup(language_manager.get_string('text_help'), title=language_manager.get_string('help'),
                         non_blocking=True)

            # actualize language window layout
            actualize_window_layout(language_manager)

        except ParseConfigException as Error:
            sg.Popup(language_manager.get_string(Error.message), title=language_manager.get_string('warning'), non_blocking=True)

    window.close()

# TODO feature - replace classic (*,/) to symbols (X, and the other one) - automatic in czech language
# TODO feature - turn on division with reminder - advanced option
# TODO count with negative integer?
# TODO mend is operation with integer values
# TODO support plugin - interfaces
# TODO dynamic layout after change language - gaps etc.

