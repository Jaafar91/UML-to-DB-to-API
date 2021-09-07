FROM mcr.microsoft.com/mssql/server:2017-latest

RUN mkdir -p /ddaa/config
WORKDIR /ddaa/config

COPY config /ddaa/config

RUN chmod +x /ddaa/config/entrypoint.sh
RUN chmod +x /ddaa/config/setup.sh

ENTRYPOINT ["./entrypoint.sh"]
