'''
You are required to build a Personal Budget Management application. The application will manage budget categories like food, 
entertainment, utilities, etc., ensuring that budget details remain private and are accessed or modified through public methods.
'''

class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
        self.__remaining_budget = allocated_budget

    def get_category_name(self):
        return self.__category_name

    def set_category_name(self, new_name):
        self.__category_name = new_name

    def get_allocated_budget(self):
        return self.__allocated_budget

    def set_allocated_budget(self, new_budget):
        if new_budget >= 0:
            self.__allocated_budget = new_budget
        else:
            print("Error: Budget should be a positive number.")

    def add_expense(self, amount):
        if amount >= 0:
            if amount <= self.__remaining_budget:
                self.__remaining_budget -= amount
                print(f"${amount} expense added to {self.__category_name} category.")
            else:
                print("Error: Expense exceeds remaining budget.")
        else:
            print("Error: Expense should be a positive number.")

    def display_category_summary(self):
        print("Category:", self.__category_name)
        print("Allocated Budget: $", self.__allocated_budget)
        print("Remaining Budget: $", self.__remaining_budget)


if __name__ == "__main__":
    food_category = BudgetCategory("Food", 500)
    food_category.add_expense(100)
    food_category.display_category_summary()
