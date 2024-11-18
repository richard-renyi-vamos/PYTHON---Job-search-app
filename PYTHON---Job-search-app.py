import requests
from bs4 import BeautifulSoup

# Job portals to search
job_portals = {
    "LinkedIn": "https://www.linkedin.com/jobs/search/",
    "Glassdoor": "https://www.glassdoor.com/Job/jobs.htm",
    "Indeed": "https://www.indeed.com/jobs",
}

def search_linkedin(job_title, location):
    """
    Searches LinkedIn for jobs.
    This example uses a placeholder as LinkedIn scraping often requires advanced methods or paid APIs.
    """
    print("Searching LinkedIn...")
    params = {"keywords": job_title, "location": location}
    response = requests.get(job_portals["LinkedIn"], params=params)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        jobs = soup.find_all("div", class_="base-card__full-link")  # Adjust class as per LinkedIn's current structure
        for job in jobs[:5]:  # Print first 5 jobs
            print(job.text.strip())
    else:
        print("LinkedIn search failed. Status code:", response.status_code)


def search_glassdoor(job_title, location):
    """
    Searches Glassdoor for jobs.
    """
    print("Searching Glassdoor...")
    params = {"sc.keyword": job_title, "locT": "C", "locId": location}  # Adjust params as per Glassdoor's query structure
    response = requests.get(job_portals["Glassdoor"], params=params)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        jobs = soup.find_all("li", class_="jl")  # Adjust as per Glassdoor's structure
        for job in jobs[:5]:
            title = job.find("a", class_="jobLink").text.strip()
            print(f"Job Title: {title}")
    else:
        print("Glassdoor search failed. Status code:", response.status_code)


def search_indeed(job_title, location):
    """
    Searches Indeed for jobs.
    """
    print("Searching Indeed...")
    params = {"q": job_title, "l": location}
    response = requests.get(job_portals["Indeed"], params=params)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        jobs = soup.find_all("div", class_="job_seen_beacon")  # Adjust as per Indeed's structure
        for job in jobs[:5]:
            title = job.find("h2", class_="jobTitle").text.strip()
            print(f"Job Title: {title}")
    else:
        print("Indeed search failed. Status code:", response.status_code)


def main():
    job_title = input("Enter the job title: ")
    location = input("Enter the location: ")

    # Search jobs on different portals
    search_linkedin(job_title, location)
    search_glassdoor(job_title, location)
    search_indeed(job_title, location)


if __name__ == "__main__":
    main()
