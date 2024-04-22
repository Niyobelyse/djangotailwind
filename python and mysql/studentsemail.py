import mysql

def get_user_info():
  """Prompts the user for ID, name, and email, and returns a dictionary containing the information."""
  user_id = int(input("Enter your ID: "))
  name = input("Enter your Name: ")
  email = input("Enter your email: ")
  return {"id": user_id, "name": name, "email": email}

def insert_user(user_info):
  """Inserts the user information into the studentsemail table in the database."""
  conn = mysql.connect('alu_db.db')
  c = conn.cursor()

  # Prepare INSERT statement with placeholders for values
  insert_query = """INSERT INTO studentsemail (Id, Name, Email) VALUES (?, ?, ?)"""

  # Execute the query with user information as parameters
  c.execute(insert_query, (user_info["id"], user_info["name"], user_info["email"]))

  # Save changes to the database
  conn.commit()
  conn.close()

# Get user information and store it in a dictionary
user_info = get_user_info()

# Insert user information into the database
insert_user(user_info)

print("User information saved to studentsemail table")