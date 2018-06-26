# Glacier Delete Archives
This script deletes all archives inside a given glacier vault. 

To run it, its necessary provide an glacier list archives job output

## Retrieving glacier vault archives list 

Start a Glacier JOB to list all archives inside

```bash
aws glacier initiate-job --job-parameters '{"Type": "inventory-retrieval"}' --vault-name YOUR_VAULT_NAME --account-id YOUR_ACCOUNT_ID --region us-east-1
```

Loop every 10 seconds to get job status (will take a long time to finish)
```bash
watch -n 10 "aws glacier list-jobs --vault-name YOUR_VAULT_NAME --region us-east-1 --account-id YOUR_ACCOUNT_ID"
``` 

generate a `output.json` file from job result 
```bash
aws glacier get-job-output --job-id ABOVE_JOB_ID --vault-name YOUR_VAULT_NAME --region us-east-1 ./output.json --account-id YOUR_ACCOUNT_ID
``` 

## Deleting Glacier Vault Archives
Fill script variables `profile_name` (if its not default) and `vault_name` 
```python
profile_name = 'default'
vault_name = 'TestVault'
```

And run python script
```bash
python glacier-delete-archive.py
```

Output example:
```bash
{'ResponseMetadata': {'RequestId': '0GDrO7u3SW3GrZ2nj8mMSW7JAXo4ZW_mxehkhRsluPgj7yI', 'HTTPStatusCode': 204, 'HTTPHeaders': {'x-amzn-requestid': '0GDrO7u3SW3GrZ2nj8mMSW7JAXo4ZW_mxehkhRsluPgj7yI', 'date': 'Tue, 26 Jun 2018 13:11:01 GMT'}, 'RetryAttempts': 0}}
{'ResponseMetadata': {'RequestId': 'z5i8mHCv_b16J_TXxL58LTr6f3C_ToaoMWEYMyLG1NVyl_k', 'HTTPStatusCode': 204, 'HTTPHeaders': {'x-amzn-requestid': 'z5i8mHCv_b16J_TXxL58LTr6f3C_ToaoMWEYMyLG1NVyl_k', 'date': 'Tue, 26 Jun 2018 13:11:01 GMT'}, 'RetryAttempts': 0}}
{'ResponseMetadata': {'RequestId': 'YiJhJ3_cteLHBhysns_eUO_JM6egbi3NE4t92f8zkHY-TT4', 'HTTPStatusCode': 204, 'HTTPHeaders': {'x-amzn-requestid': 'YiJhJ3_cteLHBhysns_eUO_JM6egbi3NE4t92f8zkHY-TT4', 'date': 'Tue, 26 Jun 2018 13:11:01 GMT'}, 'RetryAttempts': 0}}
{'ResponseMetadata': {'RequestId': 'rWUjs2lrrv0l4qkIAO05Gw8Abn5_NB84WmhvIjMyZi0hWUs', 'HTTPStatusCode': 204, 'HTTPHeaders': {'x-amzn-requestid': 'rWUjs2lrrv0l4qkIAO05Gw8Abn5_NB84WmhvIjMyZi0hWUs', 'date': 'Tue, 26 Jun 2018 13:11:01 GMT'}, 'RetryAttempts': 0}}
{'ResponseMetadata': {'RequestId': 'hDp-2KdZba5-Uktr4H9kw01tFEzVd642hamKviVPRZhdACc', 'HTTPStatusCode': 204, 'HTTPHeaders': {'x-amzn-requestid': 'hDp-2KdZba5-Uktr4H9kw01tFEzVd642hamKviVPRZhdACc', 'date': 'Tue, 26 Jun 2018 13:11:01 GMT'}, 'RetryAttempts': 0}}
```
