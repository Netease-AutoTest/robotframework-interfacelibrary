# coding: utf-8
import json
import sys
import random
import re
import datetime
import mysql.connector
from mysql.connector import errorcode

reload(sys)
sys.setdefaultencoding('utf-8')


class CheckResult():
    """docstring for CheckResult"""
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self):
        self.cnx = None

    def check_code(self, response, expectcode):
        """Check HTTP response code.
        `response` application/json type

        Examples usage:
        | Check | {"data":"null","code":"200","msg":"添加成功"}| 200 |
        """
        try:
            dic = json.loads(response)
        except Exception, e:
            print 'Http response can not transfer to dict,pelease check data format'
            raise e
        else:
            code = dic['code']
            if str(code) == expectcode:
                print 'response code ' + str(code) + ' is expectcode ' + expectcode
            else:
                raise AssertionError('response code ' + str(code) + ' is not expectcode ' + expectcode)

    def mysql_select(self, sql):
        """ Execute mysql SELECT statement,now it default handle the fist row of the select datas,
        if select one element,it return a string,if select multiple elements,it return a list.

        Examples usage:
        | Mysql Select | SELECT name FROM elf_activity_tab WHERE ID = 3|
        this examples return a string 

        | Mysql Select | SELECT name,remark FROM elf_activity_tab WHERE ID = 3|
        this examples return a list 

         """    
        try:
            cursor = self.cnx.cursor(dictionary=True)
            self._execute_sql(cursor,sql)
        except mysql.connector.Error as err:
            print err

        else:
            rows = cursor.fetchall()
             
            """判断查询内容"""
            endn = sql.find('FROM')
            cutstr = sql[7:endn - 1]
            spstr = cutstr.split(',')

            """判断是否是全部查询，返回记录总数"""
            if spstr[0] == '*':
                return len(rows)

            """判断是否有数据返回"""
            if len(rows) == 0:
                print 'no data return'
                return
            if len(spstr) == 1:
                if len(rows) > 1:
                    lists = []
                    for element in rows:
                        lists.append(rows[0][spstr[0]])
                    return lists
                else:
                    print 'the value of ' + str(spstr[0]) + ' is ' + str(rows[0][spstr[0]])
                    return rows[0][spstr[0]]
            else:
                listdata = []
                for element in spstr:
                    print 'value of ' + element + ' is ' + str(rows[0][element])
                    listdata.append(rows[0][element])
                return listdata
        finally:
            #cursor.close()
            #self.cnx.close()
            #avoid cache
            if cursor:
                self.cnx.rollback()


    def execute_mysql_script(self, sqlScriptFileName):
        """Executes the sql sript file of the `sqlScriptFileName` as SQL commands.
        lines that starts with a number sign (`#`,`--`) are treated as a commented line.
        The sql script can include `begin` `end` function.

        Examples usage:
        | Execute Mysql Script | ${CURDIR}\\test_script\sqlfile.sql |

        """ 
        sqlScriptFile = open(sqlScriptFileName)
        try:
            cursor = self.cnx.cursor()
            sqlStatement = ''
            for line in sqlScriptFile:
                line = line.strip()
                if line.startwith('#'):
                    continue
                if line.startwith('--'):
                    continue
                if (line.startwith('--') == 0 and line.find('--')!=-1):
                    line = line[:line.find('--')]
                if line == '':
                   continue
                sqlStatement += line + ' '
                sqlStatement = sqlStatement.replace('\n', ' ')
                print sqlStatement
                if len(sqlStatement) != 0:
                    self._execute_sql(cursor, sqlStatement)
                self.cnx.commit()
        finally:
            if cur:
                self.cnx.rollback()

    def delete_rows_from_table(self, condition, table):
        """Delte all the rows within a given table and condition.
        
        Example usage:
        | Delete Rows FROM Table | id=337 | elf_activity_tab |
        """
        sql = ("DELETE FROM %s WHERE %s" % (table, condition))
        try:
            cursor = self.cnx.cursor()
            result = self._execute_sql(cursor, sql)
            if result is not None:
                self.cnx.commit()
                return result
            self.cnx.commit()
        finally:
            if cursor:
                self.cnx.rollback()

    def check_if_not_exists_in_database(self,sql):
        """
        Check if no rows would be returned by given the input
        `selectStatement`. If there are any results, then this will
        throw an AssertionError.

        Example usage:
        | Check If Not Exists In Database | SELECT name,remark FROM elf_activity_tab WHERE id=337 |
        If the id is not exist, the output is:No date return #pass

        """
        queryResults = self.mysql_select(sql)
        if queryResults:
            raise AssertionError("Expected to have no results from '%s', but got some results: '%s'." % (sql, queryResults))
        else:
            print 'The records do not exist in this table!'

    def check_if_exists_in_database(self, sql):
        """
        Check if no rows would be returned by given the input
        'SQL'statement. If there are any results, then this will
        throw an AssertionError.

        Example usage:
        | Check If Not Exists In Database | SELECT name,company_id FROM elf_staff_tab WHERE id=337 |

        """
        queryResults = self.mysql_select(sql)
        if not queryResults:
            raise AssertionError("Expected to have at least one row from '%s', but got 0 rows" % sql)
        else:
            print 'The records exist in this table!'
    
    def connect_to_database(self, dbname, dbusername, dbpassword, dbhost, dbport=3306):
        """
        Example usage:
        | Connect To Database | dbname | dbusername | dbpassword | dbhost |
        """
        try:
            self.cnx = mysql.connector.connect(user=dbusername, password=dbpassword, host=dbhost, database=dbname, port=dbport)
        except  mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print 'Something is wrong with your user name or password'
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print 'Database does not exist'
            else:
                print (err)
        else:
            print 'connect to database successful!'
      
    def _execute_sql(self, cursor, sql):
        """ execute sql statement """
        print "Executing : %s" %sql
        return cursor.execute(sql)
        

    def generate_date(self,days=0):
        """
        generate date based on current date
        Example usage:
        | Generate Date | 5 |
        # Generate the date after 5 days from today
        | Generate Date | -5 |
        # Generate the date before 5 days from today

        """
        days = int(days)
        timer = datetime.datetime.now() + datetime.timedelta(days)
        return timer.strftime('%Y-%m-%d %H:%M:%S')

    def generate_random_int(self, n2, n1=1):
        """ generate random int between n1 and n2

        Examples usage:
        | Generate Random Int | 100 |

        | Generate Random Int | 100 | 5
        """
        print type(n2)
        randomInt = random.randint(int(n1), int(n2))
        print 'generate random int is ' + str(randomInt)
        return randomInt

    def random_index(self, str, key):
        """generate random int from http response keyword

        Examples usage:
        | Random Index | ${res} | id |
        this examples return a int between 0 and id term length - 1
        
        """
        p = re.compile(key)
        return random.randint(0, p.findall(str).__len__() - 1)

    def json_to_dict(self,jsondata):
        """Convert json form data to dict type
        """
        return json.loads(jsondata)
