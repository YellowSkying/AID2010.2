"""
HouseManagerView
"""
from bll import HouseManagerController


class HouseManagerView:
    def __init__(self):
        self.__controller = HouseManagerController()

    def __display_menu(self):
        print("按1键显示所有房源信息")
        print("按2键显示总价最高的房源信息")
        print("按3键显示面积最小的房源信息")
        print("按4键根据总价升序显示房源信息")
        print("按5键根据面积降序显示房源信息")
        print("按6键查找所有户型信息")

    def __select_menu(self):
        selection = input("请输入您的选择：")
        if selection == "1":
            self.__display_all_house_info()
        elif selection == "2":
            self.__display_most_expenseve_house_info()
        elif selection == "3":
            self.__display_smallest_house_info()
        elif selection == "4":
            self.__display_ascending_house_info_by_total_price()
        elif selection == "5":
            self.__display_descending_house_info_by_area()
        elif selection == "6":
            self.__display_all_house_type_info()

    def __display_all_house_info(self):
        for item in self.__controller.list_house:
            print(item)

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

    def __display_most_expenseve_house_info(self):
        print(self.__controller.get_most_expensive_house_info())

    def __display_smallest_house_info(self):
        print(self.__controller.get_smallest_house_info())

    def __display_ascending_house_info_by_total_price(self):
        for item in self.__controller.ascending_house_info_by_total_price():
            print(item)

    def __display_descending_house_info_by_area(self):
        for item in self.__controller.descending_house_info_by_area():
            print(item)

    def __display_all_house_type_info(self):
        for key,value in self.__controller.house_type_info().items():
            print(key,value)
