import f_decorators as fd
import c_decorators as cd

if __name__ == "__main__":

    # Function decorators

    print(f"{'Function decorators': ^60}")

    # Task 1

    print(f"{'Task #1':-^60}")

    @fd.decor_count
    def add(a, b):
        return a + b

    @fd.decor_count
    def sub(a, b):
        return a - b

    print(add(1, 2), add(2, 5), add(7, 10), sub(7, 10), sep=", ")
    print(fd.func_call_num)

    # Task 2

    print(f"{'Task #2':-^60}")

    @fd.decor_reg
    def mul(a, b):
        return a * b

    @fd.decor_reg
    def sub(a, b):
        return a - b

    mul(4, 2)
    sub(4, 2)

    print(fd.decorated_functions)

    # Task 3

    print(f"{'Task #3':-^60}")


    class Task3:

        def __init__(self):
            self.number = 3

        @fd.decor_str
        def __str__(self):
            return f"This is a test class of task No. {self.number}"


    task_1 = Task3()
    # print(task_1)
    print(f"See file \"{type(task_1).__name__}.txt\"")

    # Task 4

    print(f"{'Task #4':-^60}")

    task_4_name_file = "Task4.txt"

    @fd.timing(30_000_000, task_4_name_file)
    def div(a, b):
        return a / b

    div(5, 2)

    print(f"See file \"{task_4_name_file}\"")
    print("-"*60)

    # Class decorators

    print(f"{'Class decorators': ^60}")

    # Task 1

    print(f"{'Task #1':-^60}")

    @cd.DecoratorReg
    class Test1:

        def __init__(self, name):
            self.name = name

    @cd.DecoratorReg
    class Test2:

        def __init__(self, name):
            self.name = name

    test_1 = Test1("Test 1")
    test_2 = Test1("Test 2")
    test_2_2 = Test2("Test 2")

    print("List of decorated classes -> ", cd.DecoratorReg.decorated_classes)

    # Task 2

    print(f"{'Task #2':-^60}")

    @cd.add_str("**")
    class Test3:

        def __init__(self, name):
            self.name = name

        def __str__(self):
            return f"This is the class {self.name}"

    test_3 = Test3("Test No.3")
    print(test_3)
    # test_3.name = ""
    # print(test_3)

    # Task 3

    print(f"{'Task #3':-^60}")

    box_1 = cd.Box(10, 20, 20)

    box_2 = cd.Box(25, 25, 25)

    total = cd.Box.total_volume(box_1, box_2)
    print(f"The total volume of the two boxes {total} cm\u00b3")
