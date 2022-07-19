from student_impl import StudentImpl


class Account(StudentImpl):

    def __init__(self, name, dept, sem, credit, fees):
        StudentImpl.__init__(self, name, dept, sem)
        self.__credit = credit
        self.__fees = fees
        self.__waiver = 0.0
        self.__has_waiver = False
        self.__is_registered = False
        self.__total_fees = credit * fees

    def first_payment_amount(self):
        return (self.__total_fees * 30) / 100

    def waiver_amount(self, result):
        if result >= 3.50:
            self.__total_fees -= ((self.__total_fees * 15) / 100)
            self.__has_waiver = True
            return self.__total_fees
        else:
            return "No Waiver"

    def reg_status(self):
        return self.__is_registered

    def register(self, payment):
        if payment >= self.first_payment_amount():
            self.__is_registered = True
            print("Successfully registered")
            self.__total_fees -= payment
            print("Your payment is done, rest of the amount is ", self.__total_fees)
            print("registraion status {}".format(self.reg_status()))
        else:
            print("Insufficient Balance. You Have to pay for your successfull reg {}".format(
                self.first_payment_amount() - payment))

    def __str__(self):
        return self.get_name() + " " + self.get_dept() + " " + str(self.__credit) + " " + str(self.__total_fees)
