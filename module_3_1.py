
calls = 0
def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    string_ = (len(string), string.lower(), string.upper())
    string = string_
    return string


def is_contains(string, list_to_search):
    count_calls()
    list_to_search = [a.lower() for a in list_to_search]
    return string.lower() in list_to_search


print(string_info('nonsense'))
print(string_info('ЛДhgfOP'))
print(is_contains('бред', ['5,8,7', 'БреД', 'Лпавыимс']))
print(is_contains('Kgfdsbv', ['hgffs', '1,9,325','EWdsTR']))
print(string_info('Kryakozyabra'))
print(calls)












