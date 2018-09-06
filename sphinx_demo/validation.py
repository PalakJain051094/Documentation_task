"""
.. module:: sphinx_demo
   :platform: Unix, Windows
   :synopsis: A useful module indeed.

.. moduleauthor:: palak


"""

from datetime import datetime
import re


class DataValidation():
    """
    DataValidation class is for validation of all inputs coming from user
    """
    def validateAlphaNumeric(text,optional=False):

        """

        validateAlphaNumeric method check the text(input from user) is alphanumeric or not
         and text is coming from user_input.py file having method getTopic.

        :param text:text coming from user_input.py
        :type text:string
        :param optional
        :type optional: Boolean
        :return: True Or False
        :rtype : Boolean

        """

        if(optional==True):
            return True
        valid_input = re.match("[a-zA-Z0-9_]{1,255}", text)
        if(valid_input):
           return True
        else:
           print("Please Enter Valid Topic (AlphaNumeric only)")
           return False

    def validateDate(text,optional=False):
        """
        validateDate method takes text as input form user_input file
          and check that date should be in d/m/y format

        :param:text
        :type text: Date Time
        :param optional
        :type optional: Boolean
        :return: True Or False
        :rtype : Boolean

        """
        try:
            if (optional == True):
                return True
            date_format = "%d/%m/%Y"
            start = datetime.strptime(text, date_format)
            present_date = datetime.now()
            if (start):
                if (start > present_date):
                    print("date should not be in future")
                    return False
                return True
        except:
            print("Please Enter Date in dd/mm/yyyy formate")
            return False
        else:
            print("Please Enter Date in dd/mm/yyyy fromate")
            return False

    def validateStartAndEndDate(start_date,end_date,optional=False):
        """
        validateStartAndEndDate method compare that start date and end date coming from
          user_input.py file , and check that end date should not be greater then
          start date.

        :param start_date:
        :type start_date :Date Time
        :param end_date:
        :type end_date :DateTime
        :param optional:False
        :type optional :Boolean
        :return: True or False
        :rtype :Boolean
        """
        if (optional == True):
            return True
        if (end_date < start_date):
            print("end date cant be previous then start-date")
            return False

    def validateProgress(text, optional=False):
        """
        validateProgress method take text as input parameter from user_input.py file
            and check that text should be completed or In-progress.

        :param text:
        :type text: string
        :param optional : False
        :type optional:Boolean
        :return: True or False
        :rtype: Boolean
        """
        if (optional == True):
            return True
        valid_progress=text
        progresslist = ['Completed', 'In-Progress']
        if (valid_progress in progresslist):
            return True
        else:
            print("progress status is requried and it should be 'Completed  ' or 'In-Progress  'only")
            return False

    def validateConfidence_level(level, optional=False):
        """
        validateConfidence_level method take level input from user_input.py file
            checks that level should be high ,low or medium only.

        :param level:
        :type level:String
        :param optional: False
        :type optional:Boolean
        :return: True or False
        :rtype:Boolean
        """
        if (optional == True):
            return True
        valid_confidence_level=level
        mode = ['high', 'low', 'medium']
        if (valid_confidence_level in mode):
            return True
        else:
            print("confidence_level is requried and it should be 'high','low'or 'medium'")
            return False

print(DataValidation.__doc__)
print(DataValidation.validateAlphaNumeric.__doc__)
print(DataValidation.validateDate.__doc__)
print(DataValidation.validateStartAndEndDate.__doc__)
print(DataValidation.validateProgress.__doc__)
print(DataValidation.validateConfidence_level.__doc__)



