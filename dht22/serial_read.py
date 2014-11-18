import serial
import time
import datetime
import sqlite3

dbname='humy.db'


# serial read
def serial_read():
    ser = serial.Serial('/dev/ttyACM0', 9600)
    ser_read = ser.readline().decode('utf-8')
    today = datetime.datetime.now().strftime("%y-%m-%d")
    now = datetime.datetime.now().strftime("%H:%M")
    
    try :
        humy = float(ser_read.split()[2].strip(','))
        temp = float(ser_read.split()[3].strip(','))
    except (ValueError, IndexError) :
        pass # sensor fail, nothing to do
    ser.close()
    return (humy, temp, today, now)

# store the temperature in the database
def log_temp(humy, temp, today, now):

    conn=sqlite3.connect(dbname)
    curs=conn.cursor()

    curs.execute("INSERT INTO humytemp values((?), (?), (?), (?))", (today, now, humy, temp,))

    # commit the changes
    conn.commit()

    conn.close()

# display the contents of the database
def display_data():

    conn=sqlite3.connect(dbname)
    curs=conn.cursor()

    for row in curs.execute("SELECT * FROM humytemp"):
        print(str(row[0]), str(row[1]), str(row[2]), str(row[3]))

    conn.close()

def main():
    while datetime.datetime.now().strftime("%H:%M") != '07:00' :
        (humy, temp, today, now) = serial_read()
        log_temp(humy, temp, today, now)
        time.sleep(60)

if __name__=="__main__":
    main()
