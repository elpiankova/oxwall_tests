from selenium.webdriver.common.by import By

# locator = (By.XPATH, "//li[contains(@id, 'action-feed')]")
# number = 7


# def presence_of_N_elements_located(driver):
#     els = driver.find_elements(*locator)
#     if len(els) == number:
#         return els

# def presence_of_N_elements_located(locator, number):
#
#     def func(driver):
#         els = driver.find_elements(*locator)
#         if len(els) == number:
#             return els
#
#     return func

class presence_of_N_elements_located:
    def __init__(self, locator, number):
        self.locator = locator
        self.number = number

    def __call__(self, driver):
        els = driver.find_elements(*self.locator)
        if len(els) == self.number:
            return els


if __name__ == '__main__':
    class A:
        def __init__(self, n):
            print("init of class")
            self.n = n

        # def __add__(self, other):
        #     pass

        def __call__(self, d):
            print("my call", d, self.n)

        # def my_methon(self):
        #     print("my_methon")


    a = A(5)
    a(10)
    a(12)

    a = A(100)
    a(12)
