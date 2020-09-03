from fpdf import FPDF
from datetime import datetime, date

# TODO advanced option set - bigger number may overlap bigger number = less columns
NUMBER_OF_COLUMN = 4
FONT_SIZE = 16
WIDTH_OF_RESULT = 20  # TODO try to different size of result
LINE_OF_EXAMPLE_HIGH = 8

class PDFCreator:
    ''' The class provides creation of PDF and write sth to it.

    '''

    def printExampleToPDF(self, examplesToPrint, language_manager, nameOfDirectory, numberOfCopies):
        ''' The method print example to PDF.

        :param [str] examplesToPrint: The list with math examples.
        :param Language_manager language_manager: Manager of language mutation and translation of sentence.
        :param str nameOfDirectory: Name of the user chosen output directory.
        :param int numberOfCopies: The number of copies to print.
        :return None:
        '''

        # when the path to folder is empty. The files saves to working directory
        if nameOfDirectory == '':
            nameOfDirectory = '.'

        # create PDFs
        pdfExamples = FPDF('P', 'mm', 'A4')
        pdfResults = FPDF('P', 'mm', 'A4')

        # cofigurate PDFs
        self.__configuratePDF(pdfExamples)
        self.__configuratePDF(pdfResults)


        # width of page without margins
        effective_page_width = pdfExamples.w - 2 * pdfExamples.l_margin

        # width of example with place for result
        width_of_example = (effective_page_width / NUMBER_OF_COLUMN) - WIDTH_OF_RESULT

        # Y position before start writing
        y_before = pdfExamples.get_y()



        # Measure high of examples block. Need for making copies.
        y_size = self.__measure_high_of_examples(examplesToPrint, width_of_example)

        # write example and results to PDF
        self.__writeExamplesToPDF(y_before, y_size, pdfExamples, examplesToPrint, width_of_example, effective_page_width, numberOfCopies)
        self.__writeResultsToPDF(y_before, pdfResults, examplesToPrint, width_of_example, effective_page_width)

        # save pdf to directory
        pdfExamples.output(nameOfDirectory + "/" + self.__create_name_of_file(language_manager) + "_examples.pdf", 'F')
        pdfResults.output(nameOfDirectory + "/" + self.__create_name_of_file(language_manager) + "_results.pdf", 'F')

    def __measure_high_of_examples(self, examplesToPrint, width_of_example):
        ''' Stub function to simulate high of one column with examples.

        :param [string] examplesToPrint: The list with math examples.
        :param float width_of_example: The width of one example.
        :return float: High of first column the examples write in columns.
        '''

        # open and configure PDF for measurement
        pdfMeasurement = FPDF('P', 'mm', 'A4')
        self.__configuratePDF(pdfMeasurement)

        # iterate through examples and write first column
        for example_index in range(0, len(examplesToPrint), NUMBER_OF_COLUMN):

            # set actual width for writing
            pdfMeasurement.set_x(pdfMeasurement.l_margin)
            # write the example with symbol assign
            pdfMeasurement.multi_cell(width_of_example, LINE_OF_EXAMPLE_HIGH, examplesToPrint[example_index] + " =",
                                   align="R")

        # get actual y position in PDF
        size_y_block = pdfMeasurement.get_y()
        pdfMeasurement.close()

        return size_y_block

    def __writeExamplesToPDF(self, y_before, y_size, pdfExamples, examplesToPrint, width_of_example, effective_page_width, numberOfCopies):
        ''' The method writes all examples to PDF. The method write them so many times as numberOfCopies defined.
        The sample with example never divide into two pages. When the sample crosses the edge of page, the sample is placed in new page.

        :param float y_before: The high before writing (initial high in PDF document).
        :param float y_size: The high of one sample of examples.
        :param FPDF pdfExamples: The PDF to write.
        :param [str] examplesToPrint: The list with math examples.
        :param float width_of_example: The width of one example.
        :param float effective_page_width: The width of page without margins.
        :return None:
        '''

        # current and predict new position of beginning a new sample
        position_in_PDF = y_before
        new_position_in_PDF = y_before

        # generate number of copies with examples
        for examplesCopy in range(numberOfCopies + 1):

            # predict if the sample with examples is over edge of list
            new_position_in_PDF += y_size
            if new_position_in_PDF > pdfExamples.h:
                position_in_PDF = y_before
                new_position_in_PDF = position_in_PDF
                # create new page - the high coordinate relations to new page
                pdfExamples.add_page()

            # write columns to PDF with examples
            for column in range(NUMBER_OF_COLUMN):
                self.__createColumnToExamplePDF(column, examplesToPrint, pdfExamples, width_of_example, effective_page_width, position_in_PDF)

            # actualize value in position_in_PDF
            position_in_PDF = new_position_in_PDF

    def __createColumnToExamplePDF(self, column, examplesToPrint, pdfExamples, width_of_example, effective_page_width, y_before):
        ''' The method create one column with examples in PDF.

        :param int column: The number of columns in PDF.
        :param [str] examplesToPrint: The list with math examples.
        :param FPDF pdfExamples: The PDF to write.
        :param float width_of_example: The width of one example.
        :param float effective_page_width: The width of page without margins.
        :param float y_before: The high before writing (initial high in PDF document).
        :return None:
        '''

        # Set x,y axes for new column
        pdfExamples.set_xy(pdfExamples.l_margin + (WIDTH_OF_RESULT + width_of_example) * (column + 1), y_before)

        # iterate through examples
        for example_index in range(column, len(examplesToPrint), NUMBER_OF_COLUMN):

            pdfExamples.set_x((column * (effective_page_width / NUMBER_OF_COLUMN)) + pdfExamples.l_margin)
            pdfExamples.multi_cell(width_of_example, LINE_OF_EXAMPLE_HIGH, examplesToPrint[example_index] + " =",
                                   align="R")

    def __writeResultsToPDF(self, y_before, pdfResults, examplesToPrint, width_of_example, effective_page_width):
        '''

        :param float y_before: The high before writing (initial high in PDF document).
        :param FPDF pdfResults: The PDF to write.
        :param [str] examplesToPrint: The list with math examples.
        :param float width_of_example: The width of one example.
        :param float effective_page_width: The width of page without margins.
        :return None:
        '''

        for column in range(NUMBER_OF_COLUMN):
            self.__createColumnToResultPDF(column, examplesToPrint, pdfResults, width_of_example, effective_page_width, y_before)

    def __createColumnToResultPDF(self, column, examplesToPrint, pdfResults, width_of_example, effective_page_width, y_before):
        ''' The method write one column of examples with their results. The examples are centered with assignments.

        :param int column: The number of columns in PDF.
        :param [str] examplesToPrint: The list with math examples.
        :param FPDF pdfResults: The PDF to write.
        :param float width_of_example: The width of one example.
        :param float: The width of page without margins.
        :param float y_before: The high before writing (initial high in PDF document).
        :return None:
        '''

        # Set x,y axes for new column
        pdfResults.set_xy(pdfResults.l_margin + (WIDTH_OF_RESULT + width_of_example) * (column + 1), y_before)

        # iterate through examples
        for example_index in range(column, len(examplesToPrint), NUMBER_OF_COLUMN):

            # save coordinates example
            pdfResults.set_x((column * (effective_page_width / NUMBER_OF_COLUMN)) + pdfResults.l_margin)
            current_y = pdfResults.get_y()
            current_x = pdfResults.get_x()

            # write expression with assignment
            pdfResults.multi_cell(width_of_example, LINE_OF_EXAMPLE_HIGH, examplesToPrint[example_index] + " = ",
                                  align="R")

            # restore coordinates and set pointer after assignment
            pdfResults.set_y(current_y)
            pdfResults.set_x(current_x + width_of_example)

            # write result of expression
            pdfResults.multi_cell(WIDTH_OF_RESULT, LINE_OF_EXAMPLE_HIGH,
                                  self.__evaluation_example(examplesToPrint[example_index]), align="L")

    def __configuratePDF(self, pdf):
        ''' The method configures PDF (font of writing).

        :param pdf: The PDF to configure.
        :return None:
        '''
        # add page for generate
        pdf.add_page()

        # Set font and size
        pdf.set_font('Arial', 'B', FONT_SIZE)


    def __evaluation_example(self, example):
        ''' The method interpret the example expression in string. The method replace division to integer division too.

        :param str example: The string with expression to evaluate.
        :return str: The result in string.
        '''

        # integer division instead of division
        exampleInString = str(example).replace('/', '//')
        return str(eval(exampleInString))

    def __create_name_of_file(self, language_manager):
        ''' The method makes original name of file to saving. The method combines the name of app, date and saving time.

        :param Language_manager language_manager: Manager of language mutation and translation of sentence.
        :return str: The name of new file.
        '''
        now = datetime.now()
        current_time = now.strftime("%H_%M_%S")
        today = date.today()
        today_date = today.strftime("%d_%m_%Y")
        return language_manager.get_string('nameOfProgramToFileName') + '-' + today_date + "_" + current_time

    # TODO font - size of writing - big, normal, small
    # TODO support format A5
    # TODO On/Off title of generated PDF
    # TODO feature - different range of first and second number
    # TODO feature - exclude number list ()
    # TODO feature - turn off margins - for print without margins