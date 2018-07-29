FROM golang as builder
RUN go get github.com/Lafeng/ezgoo && \
    cd /go/src/github.com/Lafeng/* && \
    go build --ldflags '-linkmode external -extldflags "-static"'

FROM alpine:3.8 
COPY --from=builder /go/src/github.com/Lafeng/*/ezgoo /app/
COPY dist /app/dist
RUN apk --no-cache add ca-certificates

WORKDIR /app
EXPOSE 80

CMD chmod +x /app/ezgoo && \
    /app/ezgoo -dir=dist 