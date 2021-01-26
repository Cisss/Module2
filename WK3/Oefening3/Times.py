class Times:
    def execute_function(self):
        success = True
        try:
            first_number = int(input("We gaan een deling maken, kies je eerste getal:"))
            second_number = int(input("en het tweede getal:"))
            result = first_number / second_number
            print("\033[1mHet antwoord is {}\033[0m".format(result))
        except ValueError:
            success = False
            print("\033[1mvul alsjeblieft een HEEL getal in\033[0m")

        except RecursionError:
            success = False
            print("\033[1mDeze functie kan zulke grote getalen niet aan\033[0m")

        except ZeroDivisionError:
            success = False
            print("\033[1mDelen door het getal nul (0) is niet mogelijk!\033[0m")

        finally:
            if (success == False):
                self.execute_function()