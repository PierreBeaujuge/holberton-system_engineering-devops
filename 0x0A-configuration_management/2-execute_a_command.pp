# Manifest that kills a process named killmenow using Puppet

exec { 'killmenow':
  path    => 'usr/bin/',
  command => 'pkill killmenow',
}
