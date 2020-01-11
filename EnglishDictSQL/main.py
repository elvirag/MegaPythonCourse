import mysql.connector

con = mysql.connector.connect(
    user="ardit700_student",
    password="ardit700_student",
    host="108.167.140.122",
    database="ardit700_pm1database"
)

cursor = con.cursor()

user_word = input("Enter a word: ")


def get_word(word):
    query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" % word)
    results = cursor.fetchall()

    if results:
        for result in results:
            print(result[1])
        return True
    else:
        return False


if not get_word(user_word):
    if not get_word(user_word.title()):
        if not get_word(user_word.upper()):
            print("No word found")
