import mysql.connector as c
import numpy


class DB:
    def __int__(self):

            # we can connect it to aws aswell,
            # host = 'database-1.codzmntflx6t.ap-northeast-1.rds.amazonaws.com'
            # user = 'admin'
            # password = '911Pentagon'
            # database
            self.conn = c.connect(
                host='127.0.0.1',
                user='root',
                password='',
                database='indigo'
            )
            print('connection done')
            self.mycursor = self.conn.cursor()
    def fetch_city_names(self):
        city = []
        # print('hello')
        try:
            self.mycursor.execute('''
            Select distinct(Source) from flights
            union
            Select distinct(destination) from flights
            ''')
            data = self.mycursor.fetchall()
            for i in data:
                city.append(i[0])
            return city
        except Exception as e:
            print(e)

    def fetch_flight_data(self,source, destination):
        self.mycursor.execute('''
        Select airline, route,dep_time,duration,price from flights
        where source = '{}'
        and destination='{}'
        '''.format(source,destination))
        data = self.mycursor.fetchall()
        print(data)
        return data

    def piechart_data(self):
        airline = []
        frequency = []
        self.mycursor.execute('''
        select airline,count(*) from flights
        group by airline
        ''')
        data = self.mycursor.fetchall()
        for i in data:
            airline.append(i[0])
            frequency.append(i[1])

        return airline,frequency

    def busy_aiport(self):
        airport = []
        num=[]
        self.mycursor.execute('''
        select source, count(*) from (select source from flights
        union all
        select destination from flights
        ) t 
        group by t.source
        order by 2 desc
        ''')

        data = self.mycursor.fetchall()
        for i in data:
            airport.append(i[0])
            num.append(i[1])
        return airport, num

    def doj(self):
        date = []
        freq = []
        self.mycursor.execute('''
        select date_of_journey,count(*) from flights
        group by date_of_journey
        ''')
        data = self.mycursor.fetchall()
        for i in data:
            date.append(i[0])
            freq.append(i[1])
        return date, freq

