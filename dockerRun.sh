docker run --rm -it \
-v "$PWD/script":/script \
-v "$PWD/frontend":/frontend \
-p 8083:5000 \
--name CMbackend \
-e FLASK_DEBUG=true \
cm_backend:dev python3 main.py
