import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('todo.db')
cursor = conn.cursor()

# Create table
cursor.execute('''CREATE TABLE IF NOT EXISTS tasks
              (id INTEGER PRIMARY KEY, task TEXT, priority INTEGER, status TEXT)''')

def add_task(task, priority):
    cursor.execute("INSERT INTO tasks (task, priority, status) VALUES (?, ?, ?)", (task, priority, 'Pending'))
    conn.commit()

def delete_task(task_id):
    cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()

def update_task(task_id, task, priority):
    cursor.execute("UPDATE tasks SET task=?, priority=?, status='Pending' WHERE id=?", (task, priority, task_id))
    conn.commit()

def mark_complete(task_id):
    cursor.execute("UPDATE tasks SET status='Complete' WHERE id=?", (task_id,))
    conn.commit()

def view_tasks():
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    for task in tasks:
        print(task)

# Command-line interface
while True:
    print("\nOptions: add, delete, update, complete, view, exit")
    choice = input("Enter choice: ").strip().lower()
    
    if choice == 'add':
        task = input("Enter task: ")
        priority = int(input("Enter priority: "))
        add_task(task, priority)
    
    elif choice == 'delete':
        task_id = int(input("Enter task ID to delete: "))
        delete_task(task_id)
    
    elif choice == 'update':
        task_id = int(input("Enter task ID to update: "))
        task = input("Enter new task: ")
        priority = int(input("Enter new priority: "))
        update_task(task_id, task, priority)
    
    elif choice == 'complete':
        task_id = int(input("Enter task ID to mark complete: "))
        mark_complete(task_id)
    
    elif choice == 'view':
        view_tasks()
    
    elif choice == 'exit':
        break

conn.close()
