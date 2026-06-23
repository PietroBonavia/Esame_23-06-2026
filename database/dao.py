from database.DB_connect import DBConnect
from model.user import User

class Dao:
    def __init__(self):
        pass

    @staticmethod
    def read_all_users():
        print("Executing read from database using SQL query")

        results = []
        cnx = DBConnect.get_connection()

        if cnx is None:
            print("Connection failed")
            return None

        cursor = cnx.cursor(dictionary=True)

        query = """ SELECT * FROM Users """

        cursor.execute(query)

        for row in cursor:
            user = User(
                row["user_id"],
                row["votes_funny"],
                row["votes_useful"],
                row["votes_cool"],
                row["name"],
                row["average_stars"],
                row["review_count"]
            )

            results.append(user)

        cursor.close()
        cnx.close()

        return results


    @staticmethod
    def get_nodi(n_bus):
        print("Executing read from database using SQL query")

        results = []
        cnx = DBConnect.get_connection()

        if cnx is None:
            print("Connection failed")
            return None

        cursor = cnx.cursor(dictionary=True)

        query = """select distinct r.user_id as id, count(*) as tot
                   from reviews r 
                   group by r.user_id 
                   having tot >= %s

 """

        cursor.execute(query, (n_bus, ))

        for row in cursor:
            results.append((row["id"], row["tot"]))

        cursor.close()
        cnx.close()

        return results

    @staticmethod
    def get_archi():
        print("Executing read from database using SQL query")

        results = []
        cnx = DBConnect.get_connection()

        if cnx is None:
            print("Connection failed")
            return None

        cursor = cnx.cursor(dictionary=True)

        query = """select r1.user_id as id1, r2.user_id as id2, count(*) as tot_recensioni
                    from reviews r1, reviews r2
                    where r1.business_id = r2.business_id 
                    and r1.user_id < r2.user_id 
                    group by r1.user_id , r2.user_id 

                """

        cursor.execute(query)

        for row in cursor:
            results.append((row["id1"], row["id2"], row["tot_recensioni"]))

        cursor.close()
        cnx.close()

        return results

