import sqlite3
conn = sqlite3.connect("userdata.db")

conn.execute("""
                    create table userrecord(age integer,
                        bmi integer,
                        child integer,
                        gender integer,
                        smoker integer,
                        region text,
                        northwest integer,
                        southeast integer,
                        northeast integer
                        )
                """)


print("you have successfully created table in database!")

conn.commit()
conn.close