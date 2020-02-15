def get_summ(one, two, delimiter='&'):
    result = one.capitalize() + delimiter + two.capitalize()
    return result
a = get_summ("learn","python")
print(a)