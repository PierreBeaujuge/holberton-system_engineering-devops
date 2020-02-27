# script that take care of http requests in high volume adressed to Nginx
exec { 'sed increase ULIMIT number in concerned etc/default/nginx file':
  command => "sed -i 's/15/1024/g' /etc/default/nginx; service nginx restart",
  path    => ['/bin', '/usr/bin', '/usr/sbin']
}
