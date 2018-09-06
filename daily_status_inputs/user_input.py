from sphinx_demo.validation import DataValidation as dv


class InputData:
    """
    InputData class take inputs from user and have different methods for different input
    """
    status_list = []    # empty list

    def getTopic(self):
        """
        getTopic method take topic from user and validateAlphaNumeric method
        is call from DataValidation class

        :param self:
        :param topic:
        :type topic:string
        :return: none
        """
        self.topic = input("Enter Topic")[:255]
        if (dv.validateAlphaNumeric(self.topic) == False):
            self.getTopic()
        else:
            self.status_list.append(self.topic)

    def getContent(self):
        """
         getContent method take content from user and validateAlphaNumeric method
         is call from DataValidation class

        :param self:
        :param content:
        :type content:string
        :return: none
        """
        self.content = input("Enter Content")[:255]
        if (dv.validateAlphaNumeric(self.content) == False):
            self.getContent()
        else:
            self.status_list.append(self.content)

    def getStart_Date(self):
        """
         getStart_Date method take start-date from user and validateDate method
         is call from DataValidation class

        :param self:
        :param start_date:
        :type start_date:date time
        :return:none
        """
        self.start_date = input("Enter Start_Date In [DD/MM/YYYY]")
        if (dv.validateDate(self.start_date) == False):
            self.getStart_Date()
        else:
            self.status_list.append(self.start_date)

    def getEnd_Date(self):
        """
         getEnd_Date method take end-date from user and validateStartAndEndDate method
         is call from DataValidation class

        :param:self
        :param end_date:
        :type end_date:date time
        :return:none
        """
        self.end_date = input("Enter End_Date In [DD/MM/YYYY]")
        if (dv.validateDate(self.end_date) == False):
            self.getEnd_Date()
        elif (dv.validateStartAndEndDate(self.start_date,self.end_date) == False):
                self.getEnd_Date()
        else:
            self.status_list.append(self.end_date)

    def getProgress(self):
        """
         getProgress method take progress from user and validateProgress method
         is call from DataValidation class

        :param:self
        :param:progress
        :type progress:string
        :return:none
        """
        self.progress = input("Enter Progress Status Is'Completed  ' or 'In-Progress '")[:255]
        if (dv.validateProgress(self.progress) == False):
            self.getProgress()
        else:
            self.status_list.append(self.progress)

    def getConfidence_level(self):
        """
         getConfidence_level method take confidence_level from user and validateProgress method
         is call from DataValidation class

        :param:self
        :param confidence_level:
        :type confidence_level:string
        :return: none
        """
        self.confidence_level=input("Enter Confidence_level And It Should Be 'high','low'or 'medium'")[:255]
        if (dv.validateConfidence_level(self.confidence_level) == False):
            self.getConfidence_level()
        else:
            self.status_list.append(self.confidence_level)

    def getTeam_Member_Name(self):
        """
         getTeam_Member_Name method take team_member_name from user and validateProgress method
         is call from DataValidation class
         :param self:
         :param team_member_name:
         :type team_member_name:string
         :return: none
        """
        self.team_member_name = input("Enter Team_member_name")[:100]
        if (dv.validateAlphaNumeric(self.team_member_name) == False):
            self.getTeam_Member_Name()
        else:
            self.status_list.append(self.team_member_name)

    def getComments(self):
        """
        getComments method take comment from user and validateProgress method
         is call from DataValidation class
         :param self:
         :param comment:
         :type comment:string
         :return: none
        """
        self.comment = input("Enter Comment")[:1024]
        if (dv.validateAlphaNumeric(self.comment) == False):
            self.getComments()
        else:
            self.status_list.append(self.comment)

    def callAllMethod(self):
        """
        callAllMethod method call all previous methods to get input from user
        :return:
        """
        self.getTopic()
        self.getContent()
        self.getStart_Date()
        self.getEnd_Date()
        self.getProgress()
        self.getConfidence_level()
        self.getTeam_Member_Name()
        self.getComments()

print(InputData.__doc__)
print(InputData.getTopic.__doc__)
print(InputData.getContent.__doc__)
print(InputData.getStart_Date.__doc__)
print(InputData.getEnd_Date.__doc__)
print(InputData.getProgress.__doc__)
print(InputData.getConfidence_level.__doc__)
print(InputData.getTeam_Member_Name.__doc__)
print(InputData.getComments.__doc__)



