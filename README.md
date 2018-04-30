# file-based-producer-consumer
Single Producer Consumer, which are interacting with each other via file, instead of message broker. Current Implementation at present supports only single producer-consumer.

There're several ways to solve producer and consumer problem. The industry standard way is to use message brokers like RabbitMQ. This's is the simple implementation, where a shared  file is used between producer and consumer.  At presents, it supports only single producer and consumer. Producer restarts will lead to loss of messages, as file will be wiped out. Consumer restarts will lead to reading of same messages again.
