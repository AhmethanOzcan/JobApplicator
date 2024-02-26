import get_application
import gpt_creator
import url_collector
import mail_sender
import re
from dotenv import load_dotenv

def main(pdf_route):
    load_dotenv()
    # Extract urls
    url = url_collector.collect()
    
    # Get all job1
    job_info_list = []
    reference_file = open("references.txt", "a+")
    reference_file.seek(0)
    reference_list = reference_file.readlines()
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    for i in url:
        job_dict = get_application.get_from_url(i)
        # job_info_list.append(job_dict)
        if job_dict["reference_number"]+"\n" not in reference_list and re.fullmatch(regex, job_dict["email"]):
            job_info_list.append(job_dict)
        else:
            print("Already sent mail to "+job_dict["reference_number"])
    # dicte= {
    #     "firm_name"          : "firm_name",
    #     "job_title"          : "job_title",
    #     "reference_number"   : "reference_number",
    #     "application_detail" : "application_detail",
    #     "additional_detail"  : "additional_detail",
    #     "email"              : "email"
    # }
    # job_info_list = []
    # job_info_list.append(dicte)
    # Generate cover letters and mails
    mail_dict_list = gpt_creator.gpt_mail_coverletter(job_info_list, pdf_route)
    # Send Mails with Cover Letters
    for count, mail in enumerate(mail_dict_list):
        print(mail)
        mail_sender.send(mail, reference_file)
        print(str(count+1)+"/"+str(len(mail_dict_list))+" is done!")
    reference_file.close()
    


main('Ozcan_Ahmethan_CV.pdf')