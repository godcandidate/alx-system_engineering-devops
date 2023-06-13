# changes the maximum request to 2046
exec { 'task-0':
  provider => 'shell',
  command  => "sed -i 's/15/2048/g' /etc/default/nginx; service nginx restart",
}
