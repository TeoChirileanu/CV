# CV
clone this repo and cd into it

docker pull asciidoctor/docker-asciidoctor

docker tag asciidoctor/docker-asciidoctor adoc

docker run -it -v $PWD:/documents/ adoc

exit

docker ps -a

docker rename $CONTAINER_ID adoc

open repo in vscode

docker start adoc

docker attach adoc

asciidoctor src/cv.adoc -o index.html
