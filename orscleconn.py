import cx_Oracle
conn=cx_Oracle.Connection('system/manager@mother')
cur=conn.cursor()
def createtable():
    query='''create table mcaprathap(
    id number(2) primary key,
    name varchar(60)
    )
    '''
    cur.execute(query)
def insertrecord(sid,name):
    record={'id':str(sid),'name':name}
    cur.excute("insert into mcaprathap(id ,name) values(:id,:name)",record)
    conn.commit()
    #insertrecord(3,'kataramma')
    #insertrecord(4,'kanaka')
    #insertrecord(5,'kamalakshi')
    #insertrecord(6,'kamakshi')
    #insertrecord(7,'kavya')
def read_records():
    query = 'select * from mcaprathap'
    cur.execute(query)
    records = cur.fetchall()
    for row in records:
        print(row)
    #with open('records.csv','w',newline='') as csvfile:
        #data=csv.writer(csvfile)
        #data.writerow(['id','name'])
        #for row in records:
            #data.writerow(row)

def read_record():
    record={'id':str(sid)}
    query = 'select * from mcaprathap'
    cur.execute(query)
    record=cur.fatchall()
    for row in record:
        print(row)

def truncate():
    query ='truncate table mcaprathap'
    cur.execute(query)

def insert_from_csv():
    with open('records.csv','r') as csvfile:
        data=csv.reader(csvfile)
        data= list(data)
        for row in range(1,len(data)):
            insertrecord(*data[row])
        



