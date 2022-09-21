# Add configuration lines to add private key and authenticate password

file_line { 'Set password authentication to no':
  line    => '  PasswordAuthentication no',
  path    => '/etc/ssh/ssh_config',
  replace => true,
}

file_line { 'Change identity to use the private key':
  line    => ' IdentityFile ~/.ssh/school',
  path    => '/etc/ssh/ssh_config',
  replace => true,
}
