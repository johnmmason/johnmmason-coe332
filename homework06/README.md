# homework06

Click [here](https://coe-332-sp21.readthedocs.io/en/main/homework/homework06.html) to go to the prompt for homework 6.

### Launching homework06:

First, create the required services.
```bash
[homework06]$ kubectl apply -f jmmason-test-flask-service.yml
service/jmmason-test-flask-service created

[homework06]$ kubectl apply -f jmmason-test-redis-service.yml
service/jmmason-test-redis-service created
```

Now, get the redis service IP.  You will need this IP in the next step.
```bash
[homework06]$ kubectl get services
NAME                         TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
jmmason-test-flask-service   ClusterIP   10.104.44.117    <none>        5000/TCP         92s
jmmason-test-redis-service   ClusterIP   10.102.191.125   <none>        6379/TCP         72s
```

Set the environment variable `REDIS_HOST` in `jmmason-test-flask-deployment.yml` to the value of `CLUSTER-IP` for your redis app.
```bash
[homework06]$ emacs jmmason-test-flask-deployment.yml
```

Now, launch the deployments and PVC.
```bash
[homework06]$ kubectl apply -f .
deployment.apps/jmmason-test-flask-deployment created
service/jmmason-test-flask-service unchanged
deployment.apps/jmmason-test-redis-deployment created
persistentvolumeclaim/jmmason-test-redis-pvc created
service/jmmason-test-redis-service unchanged
```

