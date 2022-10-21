import pytest
from src.sorting import sort_by


@pytest.fixture
def jobs():
    return [
        {
            "job_title": "job1",
            "min_salary": 20000,
            "max_salary": 60000,
            "date_posted": "2020-05-02",
        },
        {
            "job_title": "job2",
            "min_salary": 30000,
            "max_salary": 75000,
            "date_posted": "2021-05-02",
        },
        {
            "job_title": "job3",
            "min_salary": 45000,
            "max_salary": 97000,
            "date_posted": "2022-05-02",
        },
    ]


def test_sort_by_criteria(jobs):
    sort_by(jobs, "min_salary")
    assert jobs[0]["min_salary"] == 20000

    sort_by(jobs, "max_salary")
    assert jobs[0]["max_salary"] == 97000

    sort_by(jobs, "date_posted")
    assert jobs[0]["date_posted"] == "2022-05-02"
