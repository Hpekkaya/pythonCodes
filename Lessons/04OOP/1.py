#  position, name, age, level, salary

# se1 =["Software engineer", "Max", 20, "Junior", 5000]
# se2 =["Software engineer", "Lisa", 25, "Senior", 7000]


#  Take the year
year = 1508


def isloop(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


# Check the year
if isloop(year):
    print(f"{year} is loop")
else:
    print(f"{year} isnot loop")
