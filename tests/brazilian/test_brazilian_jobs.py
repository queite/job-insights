from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    result = read_brazilian_file("tests/mocks/brazilians_jobs.csv")
    for job in result:
        assert job.get("titulo") is None
        assert job.get("salario") is None
        assert job.get("tipo") is None
