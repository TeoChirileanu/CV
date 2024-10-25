# CV
clone this repo and cd into it

docker pull asciidoctor/docker-asciidoctor

docker tag asciidoctor/docker-asciidoctor adoc

docker run -it -v C:\CV:/documents/ adoc

exit

docker ps -a

docker rename $CONTAINER_ID adoc

docker start adoc

docker attach adoc

asciidoctor src/cv.adoc -o index.html
