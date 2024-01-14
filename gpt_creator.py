from openai import OpenAI
from PyPDF2 import PdfReader





def gpt_mail_coverletter(dict_list, pdf_route):
    liste = []
    # client = OpenAI()
    reader = PdfReader(pdf_route) 
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

            Important: In cover letter dont add 
                \"Ahmethan Özcan
                Istanbul, Turkey
                ahmethanozcancs@gmail.com
                +90(546) 233-3252

                [Date]

                Ms. Melanie Reuß
                Bundesanstalt für Verwaltungsdienstleistungen
                Germany

                Reference number: 10000-1197448504-S\"
                part. It should start with: 
                "Cover Letter:
                 Dear " 

                 You should finish mail with:
                 "\nWarm regards,\nAhmethan Özcan"
        """
        
        # completion = client.chat.completions.create(
        #     # model="gpt-3.5-turbo",
        #     # model="gpt-3.5-turbo-1106",
        #     # model="gpt-4",
        #     model="gpt-4-1106-preview",
        #     # model="gpt-4-vision-preview",
        #     messages=[
        #         {"role": "system", "content": "You are a cover letter assistant, skilled in creating cover letters and mails. You should always use the cv provided for creation."},
        #         {"role": "user", "content": [
        #             {"type": "text", "text": cv},
        #             {"type": "text", "text": gpt_prompt}
        #             ]
        #         }
        #     ]
        # )
        # content = completion.choices[0].message.content
        content='Cover Letter:\nDear Ms. Melanie Reuß,\n\nI am writing to express my interest in the Software Developer position with the Bundesamt für Seeschifffahrt und Hydrographie as advertised, reference code 20240105_9300. With a Bachelor of Computer Science on track for completion in 2024 from Sabancı University and practical experience gained through multiple internships, I am enthusiastic about the opportunity to contribute to the esteemed Zentralabteilung team.\n\nMy academic background has equipped me with solid technical knowledge in Data Structures, Operating Systems, and Software and Mobile Development. I have honed my coding skills in languages such as C, C++, C#, Java, and Python, and have developed proficiency in JavaScript frameworks like ReactJS and React Native.\n\nDuring my internship at Vodafone Telecommunications, I played a pivotal role in the Selfservis project, where I was instrumental in automating scripts for distributed systems. My commitment to enhancing network operations via script automation and security integration honed my capacity to work effectively in complex IT environments.\n\nWhile interning at Cmos Technology, my tasks included maintaining APIs for multiple games and developing reusable components that significantly improved user interfaces and back-end functionality. This experience, alongside my tenure at Webulos OG in Austria, where I engaged in front-end and back-end development for various projects, has provided me with a robust understanding of the software development lifecycle and the Agile methodology.\n\nMy commitment to continuous learning and improvement echoes the qualifications you seek, as does my experience with different programming environments and development projects, such as Rhomberg Sersa and the Bionic Reading App Mobile. I am confident that my skill set, combined with my adaptability and problem-solving capabilities, will make a valuable addition to the Bundesanstalt für Verwaltungsdienstleistungen team.\n\nAs for my linguistic skills, I am a native Turkish speaker with an advanced proficiency in English, and I am actively working to enhance my German language skills, currently at the B2 competence level.\n\nI am inspired by the prospect of joining an organization with a reputation for being a family-friendly employer that embraces diversity and professional development. I am eager to contribute my thorough technical know-how and a proven track record of successful project outcomes to the MDZ23 Development team.\n\nThank you for considering my application. I look forward to the opportunity to discuss how my skills, experience, and aspirations align with the needs of the Bundesanstalt für Verwaltungsdienstleistungen.\n\nYours sincerely,\nAhmethan Özcan\n\nMail:\nSubject: Application for Software Developer Position - Ref Code 20240105_9300\n\nDear Ms. Reuß,\n\nI am pleased to submit my application for the Software Developer position with the Bundesamt für Seeschifffahrt und Hydrographie, advertised under reference code 20240105_9300.\n\nPlease find attached my cover letter, detailed curriculum vitae, diploma certificates, and qualified references for your review. As instructed, I have also entered my application with the corresponding reference code via the Elektronisches Bewerbungsverfahren (EBV) system on http://www.bav.bund.de/Einstieg-EBV.\n\nIf you require any further information or materials regarding my application, please do not hesitate to contact me via email or phone.\n\nThank you for considering my application. I am looking forward to the opportunity to discuss my candidacy with you and the selection committee.\n\nWarm regards,\nAhmethan Özcan' 
        temp_start      = content.find("Cover Letter:\nD")+14
        temp_finish     = content.find("Mail:\nS")
        cover_letter    = content[temp_start:temp_finish]
        temp_start      = content.find("Mail:\nSubject: ") + 15
        temp_finish     = content.find("\n", temp_start)
        mail_subject    = content[temp_start:temp_finish]
        mail_content    = content[temp_finish+2:len(content)]
        mail_dict       = {
            "cover_letter": cover_letter,
            "mail_adress" : email,
            "firm_name"   : firm_name,
            "mail_subject": mail_subject,
            "mail_content": mail_content
        }
        liste.append(mail_dict)
        break
    return liste
