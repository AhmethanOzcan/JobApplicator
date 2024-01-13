from openai import OpenAI
from PyPDF2 import PdfReader





def gpt_mail_coverletter(dict_list):
    liste = []
    client = OpenAI()
    reader = PdfReader('Ozcan_Ahmethan_CV.pdf') 
    cv = "Here is my cv as a text:\n"
    for i in reader.pages:
        cv += i.extract_text()
  
    for i in dict_list:
        firm_name           = i["firm_name"]
        job_title           = i["job_title"]
        reference_number    = i["reference_number"]
        application_detail  = i["application_detail"]
        additional_detail   = i["additional_detail"]
        email               = i["email"]

        gpt_prompt = f"""
            I want you to create a cover letter and e-mail using my cv.
            You shouldn't ask me any question and just generate both.
            You can find the info about the firm and application below.
            Position Name: {job_title}
            Firm Name: {firm_name}
            Reference Number: {reference_number}
            Email Adress: {email}
            Application Detail:
            {application_detail}
            Additional Info:
            {additional_detail}
            For your answer DON'T WRITE any additional thing only:
            Cover Letter:
            <YOUR COVER LETTER>
            Mail:
            <YOUR MAIL>
        """
        
        completion = client.chat.completions.create(
            # model="gpt-3.5-turbo",
            # model="gpt-3.5-turbo-1106",
            # model="gpt-4",
            # model="gpt-4-1106-preview",
            # model="gpt-4-vision-preview",
            messages=[
                {"role": "system", "content": "You are a cover letter assistant, skilled in creating cover letters and mails. You should always use the cv provided for creation."},
                {"role": "user", "content": [
                    {"type": "text", "text": cv},
                    {"type": "text", "text": gpt_prompt}
                    ]
                }
            ]
        )
        print(completion)
        break
        liste.append(gpt_prompt)
