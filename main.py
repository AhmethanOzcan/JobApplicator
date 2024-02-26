import get_application
import gpt_creator
import url_collector
import mail_sender
from dotenv import load_dotenv
from email_validator import validate_email, EmailNotValidError

def check(email):
    try:
      # validate and get info
        v = validate_email(email) 
        # replace with normalized form
        email = v["email"]  
        return email
    except EmailNotValidError as e:
        # email is not valid, exception message is human-readable
        print("Problem:",str(e),"\tEmail:",email)
        return None

def main(pdf_route):
    load_dotenv()
    # Extract urls
    url = url_collector.collect()
    
    # Get all job1
    job_info_list = []
    reference_file = open("references.txt", "a+")
    reference_file.seek(0)
    reference_list = reference_file.readlines()

    for i in url:
        job_dict = get_application.get_from_url(i)
        # job_info_list.append(job_dict)
        if check(job_dict["email"]) != None:
            if job_dict["reference_number"]+"\n" not in reference_list:
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
    

# cv_name = input("What is your cv file name?")
cv_name = 'Ozcan_Ahmethan_CV.pdf'
main(cv_name)