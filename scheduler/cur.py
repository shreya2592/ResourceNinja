from django.db import connection
import MySQLdb



def callCurr():
    cur = connection.cursor()
    # execute the stored procedure passing in
    # search_string as a parameter
    print(cur)
    #sql="select Max(id) from scheduler_ordermodel"
    cur.execute("select Max(id) from scheduler_ordermodel")
#    for p in OrderModel.objects.raw('select Max(id) from scheduler_ordermodel'):
    p= cur.fetchone()
    print(p)
    args=[p,0]
    result=cur.callproc('ninja.quotePrice', args)
    cur.execute('select @price')


    print(cur.fetchone())
    #cur.callproc('ninja.quotePrice')
    #transaction.commit_unless_managed()
    # grab the results
    #results = cur.fetchall()
    cur.close()
    ##return results
