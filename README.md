# compute-s3-etag


AWS S3 ETag is not an ordinary MD5 hash (http://docs.aws.amazon.com/AmazonS3/latest/API/RESTCommonResponseHeaders.html).

The default chunk size is 8 MB used by the official `aws cli` tool.

```bash
$ aws s3api head-object --bucket chunj-ref --key vep86.tgz
{
  "AcceptRanges": "bytes",
  "ContentType": "application/x-tar",
  "LastModified": "Wed, 24 May 2017 15:22:46 GMT",
  "ContentLength": 17548232894,
  "ETag": "\"fbf3e61bc72ad19cf4d6e90a6c174687-2092\"",
  "Metadata": {}
}
```

```bash
$ python compute_s3_etag.py
"fbf3e61bc72ad19cf4d6e90a6c174687-2092"
```

