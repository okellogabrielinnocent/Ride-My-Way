import psycopg2





class Database:
        conn = psycopg2.connect(database="postgres", user="postgres", password="moschinogab", host="127.0.0.1",
                                port="5432")
        print("Opened database successfully")


        conn.autocommit = True
        cur = conn.cursor()
               
        cur.execute('''CREATE TABLE IF NOT EXISTS rides
                    (
                    ride_id        serial not null,            
                    origin         varchar(200),
                    d_name         varchar(200),
                    destination    varchar(200),
                    departure_time varchar,
                    cost           integer,
                    date           varchar(200),
                    ride_status         boolean);'''
                    )


        cur.execute('''CREATE TABLE IF NOT EXISTS requests
                    (
                    ride_id        serial not null,            
                    user_id         integer);'''
                    )


        cur.execute('''CREATE TABLE IF NOT EXISTS users
                    (
                    id serial not null,
                    username varchar(200) not null,
                    email    varchar(200),
                    password varchar(200)
                    );'''
                    )

        
        
