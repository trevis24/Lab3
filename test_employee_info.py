import employee_info


def test_get_employees_by_age_range():
    result = employee_info.get_employees_by_age_range(25, 35)

    assert [item["name"] for item in result] == ["John", "Mike"]


def test_calculate_average_salary():
    result = employee_info.calculate_average_salary()

    assert result == 361000 / 6


def test_get_employees_by_dept():
    result = employee_info.get_employees_by_dept("Marketing")

    assert [item["name"] for item in result] == ["Jane", "Mary"]
