from selenite.common.convert import zip_dict, format_decimal_number_with_commas, convert_sec_to_ms, copy_without_attrs


def test_zip_dict():
    keys = ['name', 'age']
    values = [['John', 25], ['Jane', 30]]
    expected_output = [{'age': 25, 'name': 'John'}, {'age': 30, 'name': 'Jane'}]
    assert zip_dict(keys, *values) == expected_output


def test_format_decimal_number_with_commas():
    number = 1234567.89
    expected_output = '1,234,567.89'
    assert format_decimal_number_with_commas(number) == expected_output


def test_convert_sec_to_ms():
    timeout = 2.5
    expected_output = 2500.0
    assert convert_sec_to_ms(timeout) == expected_output


def test_copy_without_attrs():
    class Person:
        def __init__(self, name: str = None, age: int = None):
            self.name = name
            self.age = age

    person = Person('John', 25)
    person_copy = copy_without_attrs(person, Person, 'age')
    assert person_copy.name == 'John'
    assert person_copy.age is None
