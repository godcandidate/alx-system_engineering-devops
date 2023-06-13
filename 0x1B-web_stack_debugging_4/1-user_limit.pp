# configuring the os 
exec { 'hard limit':
  path    => ['/bin'],
  command => 'sed -i "s/hard nofile 5/hard nofile 1024/" /etc/security/limits.conf',
}

exec { 'soft limit':
  path    => ['/bin'],
  command => 'sed -i "s/soft nofile 4/soft nofile 1024/" /etc/security/limits.conf',
}
