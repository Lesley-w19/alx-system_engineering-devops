# find the issue, fix and then automate using Puppet

exec {'replace':
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  provider => shell
}
