# Author
## `Roy Aziz Barera`

## Install
`Docker`
`Kubernets`
![alt text](images/kubernets.png)
## Environtment
`Node`
``` bash
  mkdir zero-downtime-app
  cd zero-downtime-app
  npm init -y
  npm install express
```
![alt text](images/code.png)

## Experiment
Setup Code first then create 3 version images for experiment \
Create deployment.yaml for applying kubernets into project

``` bash
  docker build -t zero-downtime-app:v1 .
  docker build -t zero-downtime-app:v2 .
  docker build -t zero-downtime-app:v3 .
```

![alt text](images/image.png)

For applying update, changes the image version in deployment.yaml
``` bash
  kubctl apply -f deployment.yaml
``` 

## Testing
Make requests to the server using python continuously, then capture the result.

- v1
![alt text](images/v1.png)

- rolling update
![alt text](images/v2.png)

- v3 with downtime
![alt text](images/pods-3.png)
![alt text](images/down.png)