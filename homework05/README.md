# homework05

Click [here](https://coe-332-sp21.readthedocs.io/en/main/homework/homework05.html) to go to the prompt for Homework 4.

### Part A

##### 1. Using hello-a.yml, create a new pod:
```shell
[homework05]$ kubectl apply -f hello-a.yml
pod/hello created
```

##### 2. List running pods:
```shell
[homework05]$ kubectl get pods
NAME    READY   STATUS    RESTARTS   AGE
hello   1/1     Running   0          3m54s
```

##### 3. Get the pod's logs:
```shell
[homework05]$ kubectl logs pod/hello
Hello,
```

This is not the desired output because no name is given.

##### 4. Delete the pod:
```shell
[homework05]$ kubectl delete pods hello
pod "hello" deleted
```

### Part B

##### 1. Using hello-b.yml, create a new pod:
```shell
[homework05]$ kubectl apply -f hello-b.yml
pod/hello created
```

##### 2. Get the pod's logs:
```shell
[homework05]$ kubectl logs pod/hello
Hello, Matt
```

##### 3. Delete the pod:
```shell
[homework05]$ kubectl delete pods hello
pod "hello" deleted
```

### Part C

##### 1. Using hello-c.yml, create a new deployment:
```shell
[homework05]$ kubectl apply -f hello-c.yml
deployment.apps/hello-deployment created
```

##### 2. List the pods:
```shell
[homework05]$ kubectl get pods --output=wide
NAME                                READY   STATUS    RESTARTS   AGE    IP             NODE   NOMINATED NODE   READINESS GATES
hello-deployment-7ccfcd6b47-5mlc7   1/1     Running   0          7m3s   10.244.3.254   c01    <none>           <none>
hello-deployment-7ccfcd6b47-m4kk6   1/1     Running   0          5s     10.244.6.120   c03    <none>           <none>
hello-deployment-7ccfcd6b47-zbkd4   1/1     Running   0          5s     10.244.5.86    c04    <none>           <none>
```

##### 3. Get the pods' logs:
```shell
[homework05]$ kubectl logs hello-deployment-7ccfcd6b47-5mlc7
Hello, Matt from IP 10.244.3.254.

[homework05]$ kubectl logs hello-deployment-7ccfcd6b47-m4kk6
Hello, Matt from IP 10.244.6.120.

[homework05]$ kubectl logs hello-deployment-7ccfcd6b47-zbkd4
Hello, Matt from IP 10.244.5.86.
```

Notice that the IPs here match the container's assigned IP above.
