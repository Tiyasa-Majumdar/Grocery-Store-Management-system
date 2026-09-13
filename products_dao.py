import mysql.connector
from sql_connection import get_sql_connection

def get_all_products(connection):
 
    cursor = connection.cursor()

    query = ("select products.products_id,products.name,products.uom_id,products.price_per_unit,uom.uom_name  "
             "from gs.products inner join uom on products.uom_id=uom.uom_id")

    cursor.execute(query)

    response =[]

    for (products_id,name,uom_id,price_per_unit,uom_name) in cursor:
        response.append(
            {
                'products_id':products_id,                
                'name':name,
                'uom_id':uom_id,
                'price_per_unit':price_per_unit,
                'uom_name':uom_name
            }
        )

    cursor.close()

    return response




'''if __name__=='__main__':
    connection = get_sql_connection()
    print(get_all_products(connection))'''




def insert_new_product(connection, product):

    cursor = connection.cursor()

    query = ("Insert Into products"
             "(name, uom_id, price_per_unit)"
             "Values (%s, %s, %s)")

    data = (product['product_name'], product['uom_id'], product['price_per_unit'])
    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid




'''if __name__=='__main__':
    connection = get_sql_connection()
    print(insert_new_product(connection, {
        'product_name':'cabbage',
        'uom_id':'1',
        'price_per_unit':'10'
    }))'''




def delete_product(connection, product_id):

    cursor = connection.cursor()

    query = ("Delete From products where products_id= %s")

    cursor.execute(query, (product_id,))
    connection.commit()
    cursor.close()
 
    return product_id

    
if __name__=='__main__':
    connection = get_sql_connection()
    print(delete_product(connection, 12))