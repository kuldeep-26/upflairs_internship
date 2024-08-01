import sqlite3
conn = sqlite3.connect("userdata.db")

conn.execute("""
                    create table userrecord(age integer,
                        flight_distance integer,
                        inflight_entertainment integer,
                        baggage_handling integer,
                        cleanliness integer,
                        departure_delay integer,
                        arrival_delay integer,
                        gender integer,
                        customer_type integer,
                        class_type text,
                        type_of_travel integer,
                        Class_Eco integer,
                        Class_Eco_Plus integer
                        )
                """)


print("you have successfully created table in database!")

conn.commit()
conn.close