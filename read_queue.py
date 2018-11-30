import boto3

# Get the service resource
sqs = boto3.resource('sqs')


def read_queue():
    queue = sqs.get_queue_by_name(QueueName='events-data')
    while 1:
        for message in queue.receive_messages(WaitTimeSeconds=10, MaxNumberOfMessages=1):
            # Print out the body of the message
            print('  Message Body: {0}'.format(message.body))
            print('  Queue Url: {0}'.format(message.queue_url))
            print('  Receipt handle: {0}'.format(message.receipt_handle))
            # Let the queue know that the message is processed
            message.delete()

read_queue()
