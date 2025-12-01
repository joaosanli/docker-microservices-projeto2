FROM alpine:3.20

RUN apk add --no-cache curl

WORKDIR /app

COPY ping.sh .

RUN chmod +x ping.sh

CMD ["./ping.sh"]
