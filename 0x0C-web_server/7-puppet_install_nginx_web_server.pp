#  configuring your server with Puppet!
exec {'install':
      provider => shell,
      command  => 'sudo apt-get -y update ; sudo apt-get -y install nginx ; echo "Hello World!" | sudo tee /var/www/html/index.nginx-debian.html ; sudo sed -i "s/server_name _;/server_name _;\n\trewrite ^\/redirect_me https:\/\/www.youtube.com\/watch?v=QH2-TGUlwu4 permanent;\n\treturn 301;/" /etc/nginx/sites-available/default ; sudo service nginx start',
}
