from distutils.core import setup

setup(
  name = 'S3toECS',
  packages = ['S3toECS'], # this must be the same as the name above
  version = '0.0.1',
  description = 'Tool that transfer Docker images from S3 to your ECS repository.',
  author = 'Antonio Maiolo',
  author_email = 'maiolo.antonio@territory.de',
  url = 'https://github.com/territory-webguerillas/s3toecs/', # use the URL to the github repo
  download_url = 'https://github.com/territory-webguerillas/s3toecs/archive/0.1.1.tar.gz', # I'll explain this in a second
  keywords = ['s3', 'ecs', 'aws', 's3 to ecs'], # arbitrary keywords
  classifiers = [],
)
