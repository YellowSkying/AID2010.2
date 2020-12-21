"""
    业务逻辑层
""" 
from dal import HouseDao

class HouseManagerController:
    def __init__(self):
        self.__list_houses = HouseDao.load()

    @property
    def list_house(self):
        return self.__list_houses

    def get_most_expensive_house_info(self):
        return max(self.list_house, key=lambda item: item.total_price)

    def get_smallest_house_info(self):
        return min(self.list_house, key=lambda item: item.area)

    def ascending_house_info_by_total_price(self):
        return sorted(self.__list_houses,key = lambda item:item.total_price)

    def descending_house_info_by_area(self):
        return sorted(self.__list_houses,key = lambda item:item.area,reverse= True)

    def house_type_info(self):
        dict_house_tpye_info = {}
        for item in self.__list_houses:
            if item.house_type in dict_house_tpye_info:
                dict_house_tpye_info[item.house_type] += 1
            else:
                dict_house_tpye_info[item.house_type] = 1
        return dict_house_tpye_info





