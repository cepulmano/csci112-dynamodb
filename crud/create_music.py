import boto3

def create_table(table_name,partition_key,sort_key):
    dynamodb = boto3.resource('dynamodb')
    
    table = dynamodb.create_table(
            TableName=table_name,
            KeySchema= [
                    {"AttributeName":partition_key,"KeyType":"HASH"},
                    {"AttributeName":sort_key,"KeyType":"RANGE"}
                ],
            AttributeDefinitions= [
                    {"AttributeName": partition_key, "AttributeType": "S" },
                    {"AttributeName": sort_key, "AttributeType": "S"}
                ],
            ProvisionedThroughput= {
                    "ReadCapacityUnits": 5,
                    "WriteCapacityUnits": 10
                }
        )
        
    table.wait_until_exists()
    
    return table
    
def delete_table(name):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(name)
    table.delete()

if __name__ == "__main__":
    music_table = create_table("music","artist","song")

    # delete_table('music')