import get_application
import gpt_creator
import url_collector
import mail_sender

def main(pdf_route):

    # Extract urls
    url = url_collector.collect()
    
    # Get all job1
    job_info_list = []
    for i in url:
        job_dict = get_application.get_from_url(i)
        job_info_list.append(job_dict)

    # Generate cover letters and mails
    mail_dict_list = gpt_creator.gpt_mail_coverletter(job_info_list, pdf_route)

    # Send Mails with Cover Letters
    for mail in mail_dict_list:
        mail_sender.send(mail)
        break
    


main('Ozcan_Ahmethan_CV.pdf')