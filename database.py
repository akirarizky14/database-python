import sqlite3

# Connect to database
con = sqlite3.connect('akira.db')

# Create a cursor
c = con.cursor()

# Query the Database
c.execute("SELECT * FROM akira")

items = c.fetchall()

# simple loop for tidy up the data
for item in items:
    print(items)

# Create a lot of table
    # many_akira = [
    #                ('akira' ,'asad','akira@gmailm'),
    #                ('semangka','shiap','adasd@gas'),
    #                ('asdad','oke','aki@gma.com'),
    #            ]

# Create a table
    #c.execute("""CREATE TABLE akira (
    #    first_name text ,
    #    last_name text,
    #    email text
    #    )""")

    # DATATYPE
    # 1. NULL
    # 2. INTEGER
    # 3. REAL
    # 4. TEXT
    # 5. BLOB

# Create a normal data
    #c.execute("INSERT INTO akira VALUES ('akira','adsasd','asd@adsa')")

# Create a lot of data
    # c.executemany("INSERT INTO akira VALUES (?,?,?)", many_akira)

print("Success")
con.commit()

con.close()