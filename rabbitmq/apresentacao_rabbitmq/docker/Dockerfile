FROM rabbitmq:3.6.0-management

RUN apt-get update -y && apt-get install apt-transport-https ca-certificates -y &&  apt-get install apt-transport-https -y && apt-get install wget -y && apt-get install unzip -y

WORKDIR /plugins
RUN wget https://dl.bintray.com/rabbitmq/community-plugins/3.8.x/rabbitmq_delayed_message_exchange/rabbitmq_delayed_message_exchange-20191008-3.8.x.zip \
    && unzip rabbitmq_delayed_message_exchange-20191008-3.8.x.zip \
    && rm -f rabbitmq_delayed_message_exchange-20191008-3.8.x.zip \
    && rabbitmq-plugins enable rabbitmq_management                                            
