# // XYZService 4-Regions 3-AZ 1000-Servers hourly-log
# // Name : xyzservice-instanceid-region-az-hour.log

# // Given list of file names
# // ("file1", "file20", "file13", "file100", "file50ac", "file10", "file50b", "file50", "file50a")
# // Sort them
# // Print Output should be
# // ("file1", "file10", "file13", "file20", "file50", "file50a", "file50ac", "file50b", "file100")

# // file1
# // file10
# // file13
# // file20
# // file50
# // file50a
# // file50ac
# // file50b
# // file100

class FileName:

    @staticmethod
    def parse_str_name(name: str):
        """
        Good move, invoking a static method from inside the constructor

        TBD: is there a better way to parse out numbers from a String
        :param name:
        :return:
        """
        # strip file prefix
        num_suffix = name[4:]
        # print("num_suffix = ", num_suffix)

        if num_suffix.isnumeric():
            return int(num_suffix), ""

        i = 1
        while True:
            number = num_suffix[0: i]
            # print("number  = ", number)

            if number.isnumeric():
                i = i + 1
                continue
            else:
                number = num_suffix[0: i - 1]
                suffix = num_suffix[i - 1:]

                return int(number), suffix

    def __init__(self, name: str):

        if name is None or len(name) < 5:
            raise ValueError("Invalid filename")

        number, suffix = FileName.parse_str_name(name)
        self.number = number
        self.suffix = suffix
        self.file_name = name

    def __str__(self):
        return self.file_name


def comp_file_names(a: FileName):
    """
    Function for custom sorting
    :param a:
    :return:
    """

    return a.number, a.suffix


def sort_file_names():
    file_list = ["file1", "file20", "file13", "file100", "file50ac", "file10", "file50b", "file50", "file50a"]

    file_obj_list = []

    for file_name in file_list:
        obj = FileName(file_name)
        # print("deciphered obj = ", obj.number, ", ", obj.suffix)
        file_obj_list.append(obj)

    # Custom sorting of a list.
    sorted_objects = sorted(file_obj_list, key=comp_file_names)

    for x in sorted_objects:
        print(x)


sort_file_names()
"""
print(FileName.parse_str_name("file50ac"))
print(FileName.parse_str_name("file100"))
print(FileName.parse_str_name("file50a"))
"""

