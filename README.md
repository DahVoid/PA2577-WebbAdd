#
Store front and cart with mongodb database

# important commands
### Run kubernetes app
kubectl apply -f flask-apps.yaml.yaml
### Stop and delete app
kubectl get deployment
kubectl delete deployment <deployment name>
### Start volume 
docker compose up -d
### Stop volume
docker compose down 
### Docker build
docker build . -t oscced/flask-kubernetes
### Delete pods
kubectl drain --ignore-daemonsets docker-desktop --force
kubectl uncordon docker-desktop
### Build and run docker file
Note: The app is not actually running kubernetes here.
docker run oscced/flask-kubernetes 
docker run -p 5000:5000  oscced/flask-kubernetes
### stop all kube
kubectl delete --cascade="foreground" -f kubernetes/flask-apps.yaml
kubectl delete --cascade="foreground" -f kubernetes/mongodb-svc.yaml
kubectl delete --cascade="foreground" -f kubernetes/mongodb-statefulset.yaml
### Update container code
cd app
docker build . -t oscced/flask-kubernetes
docker push oscced/flask-kubernetes
cd ..
kubectl delete --cascade="foreground" -f kubernetes/flask-apps.yaml
kubectl apply -f kubernetes/flask-apps.yaml
### Start kube mongodb
kubectl apply -f kubernetes/mongodb-svc.yaml
kubectl apply -f kubernetes/mongodb-statefulset.yaml
kubectl apply -f kubernetes/flask-apps.yaml.yaml