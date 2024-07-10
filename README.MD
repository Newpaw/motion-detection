docker build -t motion-detection .
docker run -it --rm --device /dev/video0:/dev/video0 motion-detection


Pokud potřebujete přístup k více video zařízením, můžete přidat další parametry --device, například:
docker run -it --rm --device /dev/video0:/dev/video0 --device /dev/video1:/dev/video1 motion-detection
