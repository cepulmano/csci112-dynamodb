import boto3

if __name__ == "__main__":
    dynamodb = boto3.resource('dynamodb')
    
    music_table = dynamodb.Table('music')
    
    songs = [
        {
            "artist": "Taylor Swift",
            "song": "Love Story",
            "year": 2012,
            "feat": ["Other artists"]
        }, 
        {
            "artist": "Bruno Mars",
            "song": "24K Magic",
            "year": 2015
        },
        {
            "artist": "Salbakuta",
            "song": "Stupid Love",
            "year": 2000
        }
    ]
    
    for song in songs:
        music_table.put_item(
            Item=song
        )