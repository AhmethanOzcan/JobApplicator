import get_application

url = [
    "https://www.make-it-in-germany.com/en/working-in-germany/job-listings/job/job-10000-1195867127-S",
    "https://www.make-it-in-germany.com/en/working-in-germany/job-listings/job/job-10000-1195532983-S",
    "https://www.make-it-in-germany.com/en/working-in-germany/job-listings/job/job-10000-1194641479-S",
    "https://www.make-it-in-germany.com/en/working-in-germany/job-listings/job/job-10000-1194561133-S",
    "https://www.make-it-in-germany.com/en/working-in-germany/job-listings/job/job-10000-1194557915-S",
    "https://www.make-it-in-germany.com/en/working-in-germany/job-listings/job/job-10000-1193159370-S",
    "https://www.make-it-in-germany.com/en/working-in-germany/job-listings/job/job-10000-1197448504-S",
    "https://www.make-it-in-germany.com/en/working-in-germany/job-listings/job/job-10000-1196661436-S",
    "https://www.make-it-in-germany.com/en/working-in-germany/job-listings/job/job-10000-1197272801-S",
    "https://www.make-it-in-germany.com/en/working-in-germany/job-listings/job/job-10000-1189688731-S"
    ]

def main():
    for i in url:
        job_dict = get_application.get_from_url(i)
        print(job_dict)


main()