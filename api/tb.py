import psycopg2
class Database:
        conn = psycopg2.connect(database = "postgres", user = "postgres", password = "moschinogab", host = "127.0.0.1", port = "5432")
        print ("Opened database successfully")

        
        cur = conn.cursor()
        if "rides" and "users" is None:
            cur.execute('''CREATE TABLE rides
                        (
                        user_id        serial not null,            
                        origin         varchar(200),
                        destination    varchar(200),
                        departure_time timestamp,
                        cost           integer,
                        status         boolean);'''
                        )


            cur.execute('''CREATE TABLE users
                        (
                        id serial not null,
                        email    varchar(200),
                        password varchar(200)
                        );'''
                        )

        else:
            conn.commit()
            

        
        