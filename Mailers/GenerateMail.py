
class MailGenerate():

    def generateMailBody(self,status_list,status_report_header):

        commonContent = """<!DOCTYPE html>
<html>
<head>
<style>
table {
    font-family: arial, sans-serif;
    border-collapse: collapse;
    width: 100%;
}

td, th {
    border: 1px solid #dddddd;
    text-align: left;
    padding: 8px;
}

tr:nth-child(even) {
    background-color: #dddddd;
}
</style>
</head>
<body>

<center><h2>Daily Status Report</h2></center>
"""
        commonContent += "<table><tr>"
        for header in status_report_header:
            commonContent += "<th>"+str(header)+"</th>"
        commonContent += "</tr><tr>"
        for value in status_list:
            commonContent += "<td>"+str(value)+"</td>"

        finalBody = commonContent+"</tr></table>"
        print(finalBody)
        return  finalBody
