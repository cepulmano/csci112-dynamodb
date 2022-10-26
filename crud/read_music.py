import boto3
from boto3.dynamodb.conditions import Key
from pprint import pprint

# Query songs by artists
def query_by_artist(artist):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('music')
    response = table.query(
            KeyConditionExpression=Key('artist').eq(artist)
        )
    return response["Items"]

# Query by artist and song title
def query_by_artist_song(artist,song):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('music')
    response = table.query(
        KeyConditionExpression=Key('artist').eq(artist) & 
                                Key('song').eq(song)
        )
    return response["Items"]

if __name__ == "__main__":
    print("Query songs by Taylor Swift")
    pprint(query_by_artist('Taylor Swift'))
    
    print("Get song info of Love Story")
    pprint(query_by_artist_song("Taylor Swift","Love Story"))