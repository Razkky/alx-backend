import kue from 'kue';

const queue = kue.createQueue();

const data = {
  phoneNumber: '08166706020',
  message: 'This is my phone number to verify my account',
};

const job = queue.create('push_notification_code', data).save(
  (error) => {
    if (!error) console.log(`Notification job created: ${job.id}`);
  });

job.on('complete', () => console.log('Notification job completed'));
job.on('failed', () => console.log('Notification job failed'));
