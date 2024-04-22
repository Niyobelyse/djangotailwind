import mysql.connector

class Todo:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="",
            password="",
            database="todo_app"
        )
        self.cursor = self.db.cursor()

    def add_task(self, task):
        sql = "INSERT INTO tasks (task) VALUES (%s)"
        self.cursor.execute(sql, (task,))
        self.db.commit()
        print("Task added successfully!")

    def remove_task(self, task_id):
        sql = "DELETE FROM tasks WHERE id = %s"
        self.cursor.execute(sql, (task_id,))
        self.db.commit()
        print("Task removed successfully!")

    def list_tasks(self):
        self.cursor.execute("SELECT * FROM tasks")
        tasks = self.cursor.fetchall()
        if tasks:
            print("Tasks:")
            for task in tasks:
                print(f"{task[0]}. {task[1]}")
        else:
            print("No tasks yet!")

def main():
    todo = Todo()

    while True:
        print("\n==== To-Do App ====")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. List Tasks")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            task = input("Enter the task: ")
            todo.add_task(task)
        elif choice == "2":
            task_id = int(input("Enter the ID of the task to remove: "))
            todo.remove_task(task_id)
        elif choice == "3":
            todo.list_tasks()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

    todo.db.close()

if __name__ == "__main__":
    main()