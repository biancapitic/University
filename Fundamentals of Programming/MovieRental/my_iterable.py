import copy


class MyIterable:
    def __init__(self):
        self.__data = {}

    class myIterable():
        def __init__(self, data):
            self.__data = data
            self.__index = 0

        def __next__(self):
            if self.__index == len(self.__data):
                raise StopIteration()
            key_value = list(self.__data)[self.__index]
            self.__index += 1
            return key_value

    def add(self, key, new_value):
        self.__data[key] = new_value
        print("add: ", self.__data)

    def __setitem__(self, key, value):
        if key not in self.__data.keys():
            raise KeyError()
        self.__data[key] = value
        print("change: ", self.__data)

    def __delitem__(self, key):
        if key not in self.__data.keys():
            raise KeyError()
        self.__data.pop(key)
        print("delete: ", self.__data)

    def __getitem__(self, item_key):
        return self.__data[item_key]

    def __iter__(self):
        return self.myIterable(self.__data)

    def sort(self, compare_function):

        sorted_data = {}
        list_data = list(self.__data.items())

        def get_next_gap(gap):
            gap = (gap*10)//13
            if gap < 1:
                return 1
            return gap

        swapped = False
        gap = len(self.__data)
        while gap != 1 or swapped is True:
            swapped = False
            gap = get_next_gap(gap)
            for index in range(0, len(self.__data) - gap):
                if compare_function(list_data[index][1], list_data[index+gap][1]):
                    list_data[index], list_data[index+gap] = list_data[index+gap], list_data[index]
                    swapped = True

        for index in range(0, len(list_data)):
            sorted_data[list_data[index][0]] = list_data[index][1]
        print("sorted: ", sorted_data)
        return sorted_data

    def filter(self, acceptance_function):
        filtered_data = {}
        for key in self.__data:
            if acceptance_function(self.__data[key]):
                filtered_data[key] = copy.deepcopy(self.__data[key])
        print("filtered: ", filtered_data)
        return filtered_data
