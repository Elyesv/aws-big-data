import boto3
from decimal import Decimal
from boto3.session import Session 
from boto3.dynamodb.conditions import (
    Key, Attr
)


TABLE_NAME = "Movies"
PROFILE_NAME = "default"

class DynamoDB:
    def __init__(self):
        
        self.table_name = 'Movies'
        self._session = Session(profile_name=PROFILE_NAME)
        self.ressource = self._session.resource('dynamodb')
        table = self.ressource.Table(TABLE_NAME)
        
        try:
            table.load()
            print(f"Table {self.table_name} already exists.")
        except:
            self.create_table()
            print(f"Creating table {self.table_name}.")

    def create_table(self):
        self.ressource.create_table(
            TableName='Movies',
            KeySchema=[
                {
                    'AttributeName': 'movie_id',
                    'KeyType': 'HASH'  # Partition key
                },
                {
                    'AttributeName': 'release_year',
                    'KeyType': 'RANGE'  # Sort key
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'movie_id',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'release_year',
                    'AttributeType': 'N'
                },
                {
                    'AttributeName': 'genre',
                    'AttributeType': 'S'
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 10,
                'WriteCapacityUnits': 10
            },
            GlobalSecondaryIndexes=[
                {
                    'IndexName': 'GenreIndex',
                    'KeySchema': [
                        {
                            'AttributeName': 'genre',
                            'KeyType': 'HASH'
                        },
                    ],
                    'Projection': {
                        'ProjectionType': 'ALL',
                    },
                    'ProvisionedThroughput': {
                        'ReadCapacityUnits': 10,
                        'WriteCapacityUnits': 10,
                    }
                },
            ]
        )
        print(f"Table {self.table_name} created.")
        
    def insert_movie(self):
        table = self.ressource.Table(self.table_name)
        response = table.put_item(
        Item={
                'movie_id': "uuid-1",
                'title': "Inception",
                'release_year': 2010,
                'genre': "Sci-Fi",
                'rating': Decimal('8.8'),
                'details': {"director": "Christopher Nolan", "duration": 148}
            }
        )
        return response
    
    def insert_movies(self, movies):
        table = self.ressource.Table(self.table_name)
        try:
            with table.batch_writer() as batch:
                for movie in movies:
                    batch.put_item(Item=movie)
            print("Movies inserted successfully.")
        except Exception as e:
            print("Error inserting movies: ", e)
        
    def get_movie(self, movie_id, release_year):
        table = self.ressource.Table(self.table_name)
        try:
            response = table.get_item(
                Key={
                    'movie_id': movie_id,
                    'release_year': release_year
                }
            )
        except Exception as e:
            print(e.response['Error']['Message'])
        else:
            return response['Item']    
        
    def get_movies_by_genre(self, genre):
        table = self.ressource.Table(self.table_name)
        response = table.query(
            IndexName='GenreIndex',
            KeyConditionExpression=Key('genre').eq(genre)
        )
        return response['Items']    
        
    def get_movies_after_year(self, year):
        table = self.ressource.Table(self.table_name)
        regex = Attr('release_year').gt(year)
        response = table.scan(
            FilterExpression=regex
        )
        return response['Items'] 

    def get_movies_with_high_rating(self, rating):
        table = self.ressource.Table(self.table_name)
        regex = Attr('rating').gt(Decimal(str(rating)))
        response = table.scan(
            FilterExpression=regex
        )
        return response['Items']
    
    def update_movie(self):
        table = self.ressource.Table(self.table_name)
        response = table.update_item(
            Key={
                'movie_id': "uuid-1",
                'release_year': 2010
            },
            UpdateExpression="set rating = :r",
            ExpressionAttributeValues={
                ':r': Decimal(str(9.0))
            },
            ReturnValues="UPDATED_NEW"
        )
        return response
    
    def delete_movie(self):
        table = self.ressource.Table(self.table_name)
        try:
            response = table.delete_item(
                Key={
                    'movie_id': "uuid-2",
                    'release_year': 1999
                }
            )
        except Exception as e:
            print(e.response['Error']['Message'])
        else:
            return response

    def add_movie_awards(self, movie_id, release_year, awards):
        table = self.ressource.Table(self.table_name)
        response = table.update_item(
            Key={
                'movie_id': movie_id,
                'release_year': release_year
            },
            UpdateExpression="set awards = :a",
            ExpressionAttributeValues={
                ':a': awards
            },
            ReturnValues="UPDATED_NEW"
        )
        return response
    
    def get_long_movies(self, ):
        table = self.ressource.Table(self.table_name)
        regex = Attr('details.duration').gt(Decimal(str(150)))
        response = table.scan(
            FilterExpression=regex
        )
        return response['Items']
    
    def count_movies(self):
        table = self.ressource.Table(self.table_name)
        response = table.scan()
        return response['Count']
    
    def get_movies_by_genre_and_year(self, genre, year):
        table = self.ressource.Table(self.table_name)
        response = table.query(
            IndexName='GenreIndex',
            KeyConditionExpression=Key('genre').eq(genre),
            FilterExpression=Attr('release_year').gt(Decimal(str(year)))
        )
        return response['Items']
    
    def get_movies_starting_with_I(self, letter='I'):
        table = self.ressource.Table(self.table_name)
        filtering_exp = Attr('title').begins_with(letter)
        response = table.scan(
            FilterExpression=filtering_exp
        )
        return response['Items']
    
    def add_release_date_index(self):
        client = boto3.client('dynamodb')
        response = client.update_table(
            TableName=self.table_name,
            AttributeDefinitions=[
                {
                    'AttributeName': 'movie_id',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'release_year',
                    'AttributeType': 'N'
                },
                {
                    'AttributeName': 'genre',
                    'AttributeType': 'S'
                }
            ],
            GlobalSecondaryIndexUpdates=[
                {
                    'Create': {
                        'IndexName': 'GenreYearIndex',
                            'KeySchema': [
                                {
                                    'AttributeName': 'genre',
                                    'KeyType': 'HASH'
                                },
                                {
                                    'AttributeName': 'release_year',
                                    'KeyType': 'RANGE'
                                }
                            ],
                            'Projection': {
                                'ProjectionType': 'ALL',
                            },
                            'ProvisionedThroughput': {
                                'ReadCapacityUnits': 10,
                                'WriteCapacityUnits': 10,
                            }
                    },
                    
                },
            ],
        )
        return response

    
def main():
    ddb = DynamoDB()
    ddb.insert_movie()
    
    movies = [
        {
            "movie_id": "uuid-2",
            "title": "The Matrix",
            "release_year": 1999,
            "genre": "Action",
            "rating": Decimal('8.7'),
            "details": {
                "director": "Wachowski",
                "duration": 136
            }
        },
        {
            "movie_id": "uuid-3",
            "title": "Interstellar",
            "release_year": 2014,
            "genre": "Sci-Fi",
            "rating": Decimal('8.6'),
            "details": {
                "director": "Christopher Nolan",
                "duration": 169
            }
        }
    ]
    
    # ddb.insert_movies(movies)
    
    # movie = ddb.get_movie("uuid-1", 2010)
    # print(movie)
    
    # movies = ddb.get_movies_by_genre("Sci-Fi")
    # for movie in movies:
    #     print(movie)
    
    # movies = ddb.get_movies_after_year(2000)
    # for movie in movies:
    #     print(movie)
    
    # movies = ddb.get_movies_with_high_rating(8.5)
    # for movie in movies:
    #     print(movie)
    
    # ddb.update_movie()

    # ddb.delete_movie()
    
    # ddb.add_movie_awards("uuid-1", 2010, {"oscars": 4})

    # movies = ddb.get_long_movies()
    # for movie in movies:
    #     print(movie)
    
    # count = ddb.count_movies()
    # print(f"Total number of movies: {count}")
    
    # ddb.add_release_date_index()
    
    # movies = ddb.get_movies_by_genre_and_year("Sci-Fi", 2000)
    # for movie in movies:
    #     print(movie)
    
    # movies = ddb.get_movies_starting_with_I()
    # for movie in movies:
    #     print(movie)
    
if __name__ == "__main__":
    main()