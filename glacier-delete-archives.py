import sys
import boto3
import json

profile_name = 'default'
vault_name = ''

session = boto3.Session(profile_name=profile_name)
glacier = session.client('glacier')

with open('output.json', 'r') as json_file:

    json = json.load(json_file)

    for arch in json['ArchiveList']:

        response = glacier.delete_archive(
            vaultName=vault_name,
            archiveId=arch['ArchiveId']
        )

        print(response)