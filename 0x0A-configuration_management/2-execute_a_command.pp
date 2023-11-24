#kills a process named killmenow

exec { 'killmenow_process':
  command     => '/usr/bin/pkill killmenow',
  refreshonly => true,
  logoutput   => true,
  subscribe   => Exec['check_killmenow_process'],
}

exec { 'check_killmenow_process':
  command     => '/usr/bin/pgrep killmenow',
  returns     => [0, 1],
  refreshonly => true,
  logoutput   => false,
}

