# CV


docker pull asciidoctor/docker-asciidoctor

docker tag adoc asciidoctor/docker-asciidoctor

docker run -it -v C:\Users\teodo\Documents\GitHub\CV:/documents/ adoc

docker rename inspiring_borg adoc

docker start adoc

docker atach adoc

asciidoctor src/cv.adoc -o index.html
