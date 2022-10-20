from src.jobs import read


def get_unique_job_types(path):
    jobs = read(path)
    return {job["job_type"] for job in jobs}


def filter_by_job_type(jobs, job_type):
    return [job for job in jobs if job["job_type"] == job_type]


def get_unique_industries(path):
    jobs = read(path)
    return {job["industry"] for job in jobs if job["industry"] != ""}


def filter_by_industry(jobs, industry):
    return [job for job in jobs if job["industry"] == industry]


def get_max_salary(path):
    jobs = read(path)
    max_salaries = {
        int(job["max_salary"]) for job in jobs if job["max_salary"].isdigit()
    }
    return max(max_salaries)


def get_min_salary(path):
    jobs = read(path)
    min_salaries = {
        int(job["min_salary"]) for job in jobs if job["min_salary"].isdigit()
    }
    return min(min_salaries)


def matches_salary_range(job, salary):
    if (
        job.get("min_salary") is None
        or job.get("max_salary") is None
        or type(job["min_salary"]) != int
        or type(job["max_salary"]) != int
        or job["min_salary"] > job["max_salary"]
        or type(salary) != int
    ):
        raise ValueError()
    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    jobs_in_range = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                jobs_in_range.append(job)
        except ValueError:
            pass
    return jobs_in_range
