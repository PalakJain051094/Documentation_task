from Mailers.MailReport import Report_Mailer as rm
from daily_status_inputs.write_staus_file import WriteDailyStatus as w


class RunDailyStatus():
    """
    RunDailyStatus class is a main class of project to run project
    """
    def runAll(self):
        """
        runAll method call writestatus method from class WriteDailyStatus

        :param self:
        :return: none
        """
        w.writeStatus(self)
        #rm.send_mail(self,self.status_list, self.status_report_header)

r=RunDailyStatus()
r.runAll()