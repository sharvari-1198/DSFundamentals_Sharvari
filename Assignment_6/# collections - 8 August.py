# collections - 8 August 
import pymysql
from pymongo import MongoClient
from pymongo.errors import BulkWriteError

# MySQL database connection details
mysql_host = 'localhost'
mysql_user = 'root'
mysql_password = 'root'
mysql_db = 'ecom'

# MongoDB database connection details
mongo_host = 'localhost'
mongo_port = 27017
mongo_db = 'ecom'

# Connect to MySQL database
mysql_conn = pymysql.connect(
    host=mysql_host,
    user=mysql_user,
    password=mysql_password,
    db=mysql_db
)

# Connect to MongoDB
mongo_client = MongoClient(mongo_host, mongo_port)
mongo_database = mongo_client[mongo_db]

try:
    with mysql_conn.cursor(pymysql.cursors.DictCursor) as cursor:
        # Fetch data from MySQL category table
        cursor.execute("SELECT * FROM category")
        categories = cursor.fetchall()

        print("Categories from MySQL:", categories)  # Debug print

        # Check for missing keys
        for category in categories:
            if 'category_id' not in category or 'category_name' not in category:
                print("Missing keys in category:", category)

        # Clear existing MongoDB category collection to avoid duplicates
        category_collection = mongo_database['category']
        category_collection.delete_many({})  # Deletes all documents in the collection

        try:
            # Insert data into MongoDB category collection
            category_collection.insert_many(categories, ordered=False)
        except BulkWriteError as bwe:
            print("Bulk Write Error:", bwe.details)

        # Create a mapping from MySQL category_id to MongoDB _id
        category_mapping = {category['category_id']: category['_id'] for category in category_collection.find()}

        # Check category mapping
        print("Category Mapping:", category_mapping)

        # Fetch data from MySQL product table
        cursor.execute("SELECT * FROM product")
        products = cursor.fetchall()

        # Debug print for products fetched
        print("Products from MySQL:", products)

        # Check for missing keys in products
        for product in products:
            if 'product_id' not in product or 'product_name' not in product or 'category_id' not in product:
                print("Missing keys in product:", product)

        # Clear existing MongoDB product collection to avoid duplicates
        product_collection = mongo_database['product']
        product_collection.delete_many({})  # Deletes all documents in the collection

        try:
            # Insert data into MongoDB product collection
            product_collection.insert_many(products, ordered=False)
        except BulkWriteError as bwe:
            print("Bulk Write Error:", bwe.details)

        # Display migrated data
        print("\n=== Categories Migrated to MongoDB ===\n")
        for category in categories:
            print(f"Category ID: {category.get('category_id')} | Name: {category.get('category_name')}")

        print("\n=== Products Migrated to MongoDB ===\n")
        for product in products:
            print(f"Product ID: {product['product_id']} | Name: {product['product_name']} | Category ID: {product['category_id']}")

finally:
    mysql_conn.close()
    mongo_client.close()

print("\nData migration from MySQL to MongoDB completed successfully.\n")