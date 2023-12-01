kubectl delete --cascade="foreground" -f kubernetes/flask-apps.yaml  
kubectl delete --cascade="foreground" -f kubernetes/mongodb-svc.yaml
kubectl delete --cascade="foreground" -f kubernetes/mongodb-statefulset.yaml

cd app_front
docker build . -t oscced/flask-kubernetes-front
docker push oscced/flask-kubernetes-front
cd ..

cd app_back
docker build . -t oscced/flask-kubernetes-back
docker push oscced/flask-kubernetes-back
cd ..

kubectl apply -f kubernetes/mongodb-svc.yaml
kubectl apply -f kubernetes/mongodb-statefulset.yaml
kubectl apply -f kubernetes/flask-apps.yaml