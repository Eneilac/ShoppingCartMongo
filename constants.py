import os

DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "root")
CLUSTER_NAME = os.getenv("CLUSTER_NAME", "cluster0")
DATABASE_NAME = os.getenv("DATABASE_NAME", "shoppingCart")
