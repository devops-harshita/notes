import boto3

def get_caller_identity():
    sts_client = boto3.client('sts')
    caller_identity = sts_client.get_caller_identity()
    print("Caller Identity:")
    print(f"Account: {caller_identity['Account']}")
    print(f"User ARN: {caller_identity['Arn']}")
    print(f"User ID: {caller_identity['UserId']}")

if __name__ == "__main__":
    get_caller_identity()
