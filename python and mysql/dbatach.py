import mysql.connector  # Import the correct library

def get_user_info():
  """Prompts the user for ID, Name, and Email, and returns a dictionary containing the information."""
  Id = int(input("Enter your ID: "))
  Name = input("Enter your Name: ")
  Email = input("Enter your Email: ")
  print(f"ID: {Id}, Name: {Name}, Email: {Email}")  # Print for verification
  return {"Id": Id, "Name": Name, "Email": Email}

def insert_user(user_info):
    """Inserts the user information into the studentsemail table in the database."""
    # Replace with your actual database connection details
    conn = mysql.connector.connect(
        host="localhost",  # Use keyword argument "host"
        user="root",
        password="root",
        database="alu_db"
    )
    c = conn.cursor()

    # Prepare INSERT statement with placeholders for values
    insert_query = """INSERT INTO studentsemail(Id,Name,Email) VALUES(%s,%s,%s)"""

    # Execute the query with user information as parameters
    c.execute(insert_query, (user_info["Id"], user_info["Name"], user_info["Email"]))

    # Save changes to the database
    conn.commit()
    conn.close()

# Get user information and store it in a dictionary
user_info = get_user_info()

# Insert user information into the database
insert_user(user_info)

print("User information saved to studentsemail table")
