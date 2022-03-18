import os

APP_ENV = os.getenv('APP_ENV', 'dev')
DATABASE_USERNAME = os.getenv('DATABASE_USERNAME', 'postgres')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', '123123')
DATABASE_HOST = os.getenv('DATABASE_HOST','localhost')
DATABASE_NAME = os.getenv('DATABASE_NAME', 'myecapp')
TEST_DATABASE_NAME = os.getenv('DATABASE_NAME', 'myecapp')

