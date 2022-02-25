# Return the century of the input year. The input will always be a 4 digit string, so there is no need for validation.


def what_century(year):
    year = int(year)
    century = (year-1) // 100 + 1
    century = str(century)
    if int(century) > 10 and int(century) <=20:
        return f"{str(century)}th"
    elif century[1] == '1':
        return  f"{century}st"
    elif century[1]=='2':
        return  f"{century}nd"
    elif century[1]=='3':
        return  f"{century}rd"
    else:
        return  f"{century}th"