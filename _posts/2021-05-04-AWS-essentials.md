---
hide: false
toc: true
layout: post
description: AWS cli commands I use (and forget) often
categories: [tools]
title: AWS essentials 
---

- To create a new bucket, use `aws s3 mb bucketname`.

- To add a subfolder to a bucket, use `aws s3api put-object --bucket bucketname
  --key foldername`

