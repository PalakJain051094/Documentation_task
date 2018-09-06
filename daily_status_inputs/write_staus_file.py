from os import path
from daily_status_inputs.user_input import*


class WriteDailyStatus():
    """
    WriteDailyStatus class having method to write data/status in file.

    """
    def writeStatus(self):
        """
        writeStatus method call InputData class method callAllmethod ,and call check_File method
        and write data in that file.

        :param self:
        :return:none
        """
        data=InputData()
        data.callAllMethod()
        try:
            if check_File(self):
                status_report=open('daily_status_report.csv', 'a')
                status_report_header=['Topic','Contents','Start-date','End-date','Progress(Completed or Inprogress)', \
                                  'ConfidenceLevel 1.High – Readytowork on deliverables \
                                  2.Medium – Understoodbuthavesomequeries 3.Low – Noconfidence','TeamMember','comments']
                for v in status_report_header:
                    status_report.writelines('%s,' % v)
                status_report.write('\n')
            else:
                for values in data.status_list:
                    status_report=open('daily_status_report.csv', 'a')
                    status_report.writelines('%s,' % values)
                status_report.write('\n')
            status_report.close()
        except Exception as e:
            print(e)

def check_File(self):
    """
    check_File method check that file is exist or not and if exist read data
     and return True or False

    :param self:
    :return: True or False
    :rtype:Boolean
    """
    fileName="daily_status_report.csv"
    try:
        status_report = open(fileName, 'r')
        if (path.exists(fileName)):
            read_data=status_report.read()
            if read_data=="":
                return True
            else:
                return False
        else:
            print("file not found")
    except Exception as e:
        print(e)

print(WriteDailyStatus.__doc__)
print(WriteDailyStatus.writeStatus.__doc__)
print(check_File.__doc__)