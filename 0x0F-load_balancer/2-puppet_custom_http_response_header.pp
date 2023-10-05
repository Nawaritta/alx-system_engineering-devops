# Automates the task of creating a custom HTTP header response using Puppet

exec { 'update':
  command => '/usr/bin/apt-get update',
} -> package { 'nginx':
  ensure => 'present',
} ~> service { 'nginx':
  ensure => 'running',
  enable => true,
} -> file_line { 'http_header':
  path  => '/etc/nginx/nginx.conf',
  match => 'http {',
  line  => "http {\n\tadd_header X-Served-By \"${hostname}\";",
 } -> exec { 'restart_nginx':
  command => '/usr/sbin/service nginx restart',
}