# dockeres-uteis
### Desenvolvido por: Matheus Leão
Voltado à demanda de cliente envolvendo Docker, foi solicitado que em uma máquina CentOS-7 Linux com 600GB de disco acoplados,
4 placas de rede (10.0.1.110, 10.0.1.111, 10.0.1.112, 10.0.1.113), 4 vCPU e 8ram.

## Como foi feito?
Containers docker:
* RabbitMQ1 (10.0.1.110:15672)
* RabbitMQ2 (10.0.1.111:15672)
* RabbitMQ3 (10.0.1.112:15672)
* RabbitMQ4 (10.0.1.113:15672)
* MongoDB (10.0.1.110:27017)
* MySQL (10.0.1.110:3306)

É instalado 2 plugins do RabbitMQ no momento do "docker-compose up -d":
* rabbitmq_amqp1_0
* rabbitmq_auth_backend_cache 
* rabbitmq_auth_backend_http 
* rabbitmq_auth_backend_ldap
* rabbitmq_auth_mechanism_ssl 
* rabbitmq_consistent_hash_exchange 
* rabbitmq_delayed_message_exchange 
* rabbitmq_event_exchange 
* rabbitmq_federation 
* rabbitmq_federation_management 
* rabbitmq_jms_topic_exchange 
* rabbitmq_management 
* rabbitmq_management_agent 
* rabbitmq_mqtt 
* rabbitmq_peer_discovery_aws 
* rabbitmq_peer_discovery_common 
* rabbitmq_peer_discovery_consul 
* rabbitmq_peer_discovery_etcd 
* rabbitmq_peer_discovery_k8s 
* rabbitmq_random_exchange 
* rabbitmq_recent_history_exchange 
* rabbitmq_sharding 
* rabbitmq_shovel 
* rabbitmq_shovel_management 
* rabbitmq_stomp 
* rabbitmq_top 
* rabbitmq_tracing 
* rabbitmq_trust_store 
* rabbitmq_web_dispatch 
* rabbitmq_web_mqtt 
* rabbitmq_web_mqtt_examples 
* rabbitmq_web_stomp 
* rabbitmq_web_stomp_examples 
