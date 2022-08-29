import mariadb
import sys

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="team_data",
        password="KTQhkLYfP3nV33MH",
        host="51.161.115.210",
        port=3306#,
        #database="jdbc:mysql://51.161.115.210:3306/prl_quanh_mainnet"
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()
test_name = 'abc'
cur.execute(
    "SELECT _id,token_id FROM prl_quanh_mainnet.box_boxes limit 10"
    )
for(_id,token_id) in cur:
    print("Id : ",_id," | Token id",token_id)
print("Done")
