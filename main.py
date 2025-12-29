import csv
import pandas
program_is_on=True
set_budget=0
continue_prog=""
def continue_program():
    global continue_prog
    global program_is_on
    try:
        continue_prog = input("Do you wish to continue? (Y/N) ")
        continue_prog=continue_prog.upper()
        if continue_prog=="Y":
            program_is_on=True
        else:
            program_is_on=False
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")
        program_is_on=False

  

while program_is_on:
  try:
   choice=input("Choose an option:\n1. Add expense\n2. View all expenses\n3. Total spending calculation\n4. Category-wise summary\n5. Set budget\n6. Check budget\n7. Reset data\n8. Exit\n--> ")
   if choice=="1":
        amount=float(input("Enter amount in rupees : "))
        category=input("Enter the category: ")
        category=category.upper()
        note=input("Enter a note: ")
        note=note.upper()
        with open("expenses.csv","a",newline="") as file:
             writer = csv.writer(file)
             writer.writerow([amount,category,note])
        print("Expense added")
        continue_program()

   elif choice=="2":
        try:
         expense_data=pandas.read_csv("expenses.csv")
         if expense_data.empty:
              print("No expenses found")
         else:
              print(expense_data)
         continue_program()
        except FileNotFoundError:
             print("No data found")
             

   elif choice=="3":
        expense_data=pandas.read_csv("expenses.csv")
        total_expenses=float(sum(expense_data.AMOUNT))
        print(f"Your total expenses is Rs.{total_expenses}")
        continue_program()

   elif choice=="4":
        expense_data=pandas.read_csv("expenses.csv")
        expense_data['AMOUNT'] = pandas.to_numeric(expense_data['AMOUNT'], errors='coerce').fillna(0)
        expense_data['CATEGORY'] = expense_data['CATEGORY'].str.upper()
        summary = expense_data.groupby("CATEGORY")["AMOUNT"].sum().reset_index()
        print(summary)
        continue_program()

   elif choice=="5":
        set_budget=float(input("Enter the budget you want to set in rupees: "))
        continue_program()

   elif choice=="6":
        expense_data=pandas.read_csv("expenses.csv")
        total_expenses=float(sum(expense_data.AMOUNT))
        if set_budget==0:
             print("You are yet to set a budget")
        elif set_budget>=total_expenses:
             print(f"Your total expenses is Rs.{total_expenses}\nYour set budget was Rs.{set_budget}\nYou are under your budget! ")
        else:
             print(f"Your total expenses is Rs.{total_expenses}\nYour set budget was Rs.{set_budget}\nYou have gone over your budget by {total_expenses-set_budget} ")
        continue_program()

   elif choice=="7":
    
        with open("expenses.csv", "w", newline="") as file:
             writer = csv.writer(file)
             writer.writerow(["AMOUNT", "CATEGORY", "NOTE"])
             print("✅ Expenses data reset successfully!")
             continue_program()

   elif choice=="8":
        program_is_on=False

             
   else:
        print("Invalid input")
  except KeyboardInterrupt:
      print("\nProgram interrupted.")
