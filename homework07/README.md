# homework07

Click [here](https://coe-332-sp21.readthedocs.io/en/main/homework/homework07.html) to go to the prompt for homework 7.

First, deploy the containers:

```bash
[homework07]$ kubectl apply -f .
deployment.apps/jmmason-hw7-flask-deployment configured
deployment.apps/jmmason-hw7-redis-deployment configured
persistentvolumeclaim/jmmason-hw7-redis-pvc configured
service/jmmason-hw7-redis-service configured
deployment.apps/jmmason-hw7-worker-deployment configured
```

Now, use curl to check if your program is functioning correctly:

```bash
[root@py-debug-deployment]$ curl 10.244.15.195:5000/jobs -X POST -d '{"start": "now","end":"later"}'
{"id": "eac207e2-bfe1-41a0-a840-f454583f23d1", "status": "submitted", "start": "now", "end": "later"}
```

Check the status of the job using the following Python code:
```python3
# read_db.py
import redis

rd = redis.StrictRedis(host='10.97.128.183', port=6379, db=0)

for key in rd.keys():
    print( rd.hmget(key, 'status') )
    print( rd.hmget(key, 'worker') )
    print()
```

```bash
[root@py-debug-deployment]$ python3 read_db.py
[b'complete']
```

After scaling up to multiple worker nodes, `read_db.py` will show you the IP of the worker node which processed our data.  You will see that submitted jobs are split between worker nodes.

```bash
[root@py-debug-deployment]$ python3 read_db.py
[b'complete']
[b'10.244.15.196']

[b'complete']
[b'10.244.10.176']

[b'complete']
[b'10.244.15.196']

[b'complete']
[b'10.244.15.196']

[b'complete']
[b'10.244.15.196']

[b'complete']
[b'10.244.10.176']

[b'complete']
[b'10.244.10.176']

[b'complete']
[b'10.244.15.176']

[b'complete']
[b'10.244.15.196']

[b'complete']
[b'10.244.15.176']
```
