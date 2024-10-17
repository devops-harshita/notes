import boto3
import json

# Initialize the Secrets Manager client
client = boto3.client('secretsmanager')

# Replace with your secret name
secret_name = "<secret_name_or_arn>"

# Fetch the secret value from AWS Secrets Manager
response = client.get_secret_value(SecretId=secret_name)

# The secret string contains the JSON with your key-value pairs
secret = json.loads(response['SecretString'])

# Extract 'token' and 'username'
token = secret['token']
username = secret['username']

# Print or use token and username as needed
print(f"Token: {token}")
print(f"Username: {username}")
