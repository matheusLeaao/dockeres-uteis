FROM rabbitmq:3-management

RUN     apt-get update -y && apt-get install wget -y && apt-get install unzip -y
WORKDIR /plugins
RUN 	wget https://dl.bintray.com/rabbitmq/community-plugins/3.8.x/rabbitmq_delayed_message_exchange/rabbitmq_delayed_message_exchange-20191008-3.8.x.zip \
		&& unzip rabbitmq_delayed_message_exchange-20191008-3.8.x.zip \
		&& rm -f rabbitmq_delayed_message_exchange-20191008-3.8.x.zip
RUN 	rabbitmq-plugins enable rabbitmq_amqp1_0 \
		&& rabbitmq-plugins disable rabbitmq_auth_backend_cache \
		&& rabbitmq-plugins disable rabbitmq_auth_backend_http \
		&& rabbitmq-plugins disable rabbitmq_auth_backend_ldap \
		&& rabbitmq-plugins disable rabbitmq_auth_mechanism_ssl \
		&& rabbitmq-plugins enable rabbitmq_consistent_hash_exchange \
		&& rabbitmq-plugins enable rabbitmq_delayed_message_exchange \
		&& rabbitmq-plugins enable rabbitmq_event_exchange \
		&& rabbitmq-plugins enable rabbitmq_federation \
		&& rabbitmq-plugins enable rabbitmq_federation_management \
		&& rabbitmq-plugins disable rabbitmq_jms_topic_exchange \
		&& rabbitmq-plugins enable rabbitmq_management \
		&& rabbitmq-plugins enable rabbitmq_management_agent \
		&& rabbitmq-plugins disable rabbitmq_mqtt \
		&& rabbitmq-plugins disable rabbitmq_peer_discovery_aws \
		&& rabbitmq-plugins disable rabbitmq_peer_discovery_common \
		&& rabbitmq-plugins disable rabbitmq_peer_discovery_consul \
		&& rabbitmq-plugins disable rabbitmq_peer_discovery_etcd \
		&& rabbitmq-plugins disable rabbitmq_peer_discovery_k8s \
		&& rabbitmq-plugins disable rabbitmq_random_exchange \
		&& rabbitmq-plugins disable rabbitmq_recent_history_exchange \
		&& rabbitmq-plugins disable rabbitmq_sharding \
		&& rabbitmq-plugins enable rabbitmq_shovel \
		&& rabbitmq-plugins enable rabbitmq_shovel_management \
		&& rabbitmq-plugins disable rabbitmq_stomp \
		&& rabbitmq-plugins disable rabbitmq_top \
		&& rabbitmq-plugins enable rabbitmq_tracing \
		&& rabbitmq-plugins disable rabbitmq_trust_store \
		&& rabbitmq-plugins enable rabbitmq_web_dispatch \
		&& rabbitmq-plugins disable rabbitmq_web_mqtt \
		&& rabbitmq-plugins disable rabbitmq_web_mqtt_examples \
		&& rabbitmq-plugins disable rabbitmq_web_stomp \
		&& rabbitmq-plugins disable rabbitmq_web_stomp_examples \