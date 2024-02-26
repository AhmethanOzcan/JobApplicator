import requests
from bs4 import BeautifulSoup

def get_from_url(url):
    # Get html
    req  = requests.get(url)
    text = req.text
    soup = BeautifulSoup(text, "html.parser")

    # Get specifics needed
    firm_name           = soup.find_all(class_ = "head__children head__children--job h5")[0].text
    job_title           = soup.find_all(class_ = "h3")[0].text
    reference_number    = soup.find_all(class_ = "h5 overview__reference-number")[0].text
    application_detail  = soup.find_all(class_ = "text detail-page__description")[0].text
    additional_detail   = soup.find_all(class_ = "detail-page__additional detail-page__additional--row-position additional")[0].text
    email_s_pos         = additional_detail.find("E-mail: ")+8
    email_f_pos         = additional_detail.find(" ",email_s_pos)
    email               = additional_detail[email_s_pos:email_f_pos]
    # Create a dic and return it
    output_model = {
        "firm_name"          : firm_name,
        "job_title"          : job_title,
        "reference_number"   : reference_number,
        "application_detail" : application_detail,
        "additional_detail"  : additional_detail,
        "email"              : email
    }

    return output_model

# x = get_from_url("https://www.make-it-in-germany.com/en/working-in-germany/job-listings/job/job-10000-1195867127-S")

# print(x)