class UserInterfaceController:
    def __init__(self, _display):
        self.m_currentExpression = ""
        self.m_currentNumber = ""
        self.m_display = _display
        self.m_sessionResults = []
        self.m_sessionExpression = []

    @staticmethod
    def __checkIfLastValueIsOperand__(_lastChar):
        if _lastChar == '/' or _lastChar == '*' or _lastChar == '+' or _lastChar == '-':
            return True
        return False

    def __updateDisplay__(self):
        print(self.m_currentExpression)
        self.m_display.display(self.m_currentNumber)

    def __addNumberToExpression__(self, _number):
        if self.m_currentNumber == "ERROR":
            return

        if self.m_currentNumber.find("res") != -1:
            self.m_currentNumber = ""

        # TODO handle more error states
        if _number == '.' and self.m_currentNumber.count('.') > 0:
            self.m_currentNumber = "ERROR"
        else:
            self.m_currentNumber += str(_number)

        self.m_currentExpression += str(_number)
        self.__updateDisplay__()

    def __flipSign__(self):
        # System error case
        if self.m_currentNumber == "ERROR":
            return

        if not self.m_currentNumber or self.m_currentNumber == '0':  # Empty case
            self.m_currentNumber = '-'

        elif self.m_currentNumber == '-':  # If only character is a neg
            self.m_currentNumber = '0'

        elif float(self.m_currentNumber) > 0:
            self.m_currentNumber = '-' + self.m_currentNumber

        else:
            self.m_currentNumber = self.m_currentNumber[1:]

        self.__updateDisplay__()

    def __addOperationToExpression__(self, _operation):
        if self.m_currentNumber == "" or self.m_currentNumber == "-":
            return

        elif UserInterfaceController.__checkIfLastValueIsOperand__(
                self.m_currentExpression[len(self.m_currentExpression) - 1]):
            self.m_currentNumber = "ERROR"
            self.__updateDisplay__()
            return

        elif self.m_currentNumber == "ERROR":
            return

        self.m_currentNumber = ""
        self.m_currentExpression += _operation
        self.__updateDisplay__()

    def __evaluate__(self):
        if self.m_currentNumber == "ERROR":
            self.m_currentNumber = ""
            return

        self.m_sessionExpression.append(self.m_currentExpression)
        self.m_currentNumber = f"res: {eval(self.m_currentExpression)}"
        self.m_sessionResults.append(eval(self.m_currentExpression))
        self.m_currentExpression = ""
        self.__updateDisplay__()

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

    def add_wrapper(self):
        self.__addOperationToExpression__('+')

    def subtract_wrapper(self):
        self.__addOperationToExpression__('-')

    def divide_wrapper(self):
        self.__addOperationToExpression__('/')

    def multiply_wrapper(self):
        self.__addOperationToExpression__('*')

    def eval_wrapper(self):
        self.__evaluate__()
