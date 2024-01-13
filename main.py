import get_application
import gpt_creator
import url_collector


def main():

    # Extract urls
    url = url_collector.collect()
    
    # Get all job1
    job_info_list = []
    for i in url:
        job_dict = get_application.get_from_url(i)
        job_info_list.append(job_dict)

    gpt_creator.gpt_mail_coverletter(job_info_list)
    


main()