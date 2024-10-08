# import lambda_function
# pylint: disable=line-too-long
import requests

event = {
    "Records": [
        {
            "kinesis": {
                "kinesisSchemaVersion": "1.0",
                "partitionKey": "1",
                "sequenceNumber": "49654063360103356676578297582363793261679183746014642178",
                "data": "ewogICAgInRleHQiOiAiSXRzIGxpa2UgdGhhdCwgaWYgeW91IHdhbnQgb3Igbm90LiBNRTogSSBoYXZlIG5vIHByb2JsZW0sIGlmIGl0IHRha2VzIGxvbmdlci4gQnV0IHlvdSBhc2tlZCBteSBmcmllbmQgZm9yIGhlbHAgYW5kIGxldCBoaW0gd2FpdCBmb3Igb25lIGhvdXIgYW5kIHRoZW4geW91IGhhdmVu4oCZdCBwcmVwYXJlZCBhbnl0aGluZy4gVGhhdHMgbm90IHdoYXQgeW91IGFza2VkIGZvci4gSW5zdGVhZCBvZiAzIGhvdXJzLCBoZSBoZWxwZWQgeW91IGZvciAxMCBob3VycyB0aWxsIDVhbS4uLiIsCiAgICAibGV4X2xpd2NfVG9uZSI6IDUuOTUsCiAgICAibGV4X2xpd2NfaSI6IDUuNDUsCiAgICAibGV4X2xpd2NfbmVnZW1vIjogMS44MiwKICAgICJsZXhfbGl3Y19DbG91dCI6IDU3LjIyLAogICAgInNlbnRpbWVudCI6IDAuMAp9",
                "approximateArrivalTimestamp": 1721373667.521,
            },
            "eventSource": "aws:kinesis",
            "eventVersion": "1.0",
            "eventID": "shardId-000000000000:49654063360103356676578297582363793261679183746014642178",
            "eventName": "aws:kinesis:record",
            "invokeIdentityArn": "arn:aws:iam::511900348839:role/lambda-kinesis-role",
            "awsRegion": "eu-north-1",
            "eventSourceARN": "arn:aws:kinesis:eu-north-1:511900348839:stream/stress_events",
        }
    ]
}


# result = lambda_function.lambda_handler(event, None)
# print(result)

url = "http://localhost:8080/2015-03-31/functions/function/invocations"
response = requests.post(url, json=event)
print(response.json())
