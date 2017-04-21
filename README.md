# s3toecs
Utility to transfer archived Docker images from your AWS S3 bucket to your ECS repository. 

## Requirements
- Properly configured AWS CLI with:
  - ReadAccess to the S3 bucket 
  - FullAccess to ECS 
- Docker Engine 

## Installation
You can install s3toecs via pip (depending on your distribution it might be named pip3 or pip)
```
pip3 install s3toecs
```
## Usage
If you install the tool via Pip, you're ready to go, as the tool provides a CLI. 

```
$ s3toecs
---------------- S3 to ECS transfer tool -----------------
S3 Url: <s3://s3-url-to your-tar-archive>
ECS Repository Name: <docker-repository-name>
Version Label: <docker-repository-tag>
```
**Notes**: 
- If the repository does not exist in ECS yet, it will be created for you. 
- The login to ECS registry is performed automatically. 
