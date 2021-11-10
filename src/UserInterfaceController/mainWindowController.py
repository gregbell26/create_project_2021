class UserInterfaceController:
    def __init__(self, _display):
        self.m_currentExpression = ""
        self.m_currentNumber = ""
        self.m_display = _display
        self.m_sessionResults = []
        self.m_sessionExpression = []

    def __addNumberToExpression__(self, _number):
        if self.m_currentNumber == "ERROR":
            return

        # TODO handle more error states
        if _number == '.' and self.m_currentNumber.count('.') > 0:
            self.m_currentNumber = "ERROR"
        else:
            self.m_currentNumber += str(_number)
        self.m_display.display(self.m_currentNumber)
        print(self.m_currentNumber)

    def __flipSign__(self):
        # TODO handle empty edge case
        if float(self.m_currentNumber) > 0:
            self.m_currentNumber = '-' + self.m_currentNumber
        else:
            self.m_currentNumber = self.m_currentNumber[1:]


    def no_0_wrapper(self):
        self.__addNumberToExpression__(0)

    def no_1_wrapper(self):
        self.__addNumberToExpression__(1)

    def no_2_wrapper(self):
        self.__addNumberToExpression__(2)

    def no_3_wrapper(self):
        self.__addNumberToExpression__(3)

    def no_4_wrapper(self):
        self.__addNumberToExpression__(4)

    def no_5_wrapper(self):
        self.__addNumberToExpression__(5)

    def no_6_wrapper(self):
        self.__addNumberToExpression__(6)

    def no_7_wrapper(self):
        self.__addNumberToExpression__(7)

    def no_8_wrapper(self):
        self.__addNumberToExpression__(8)

    def no_9_wrapper(self):
        self.__addNumberToExpression__(9)

    def dec_wrapper(self):
        self.__addNumberToExpression__('.')

    def sign_wrapper(self):
        self.__flipSign__()


