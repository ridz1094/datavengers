server {
	listen       8080;
	server_name  {{inventory_hostname}};

	location / {
	  root   /var/www/{{inventory_hostname}}/html/;
	  index  index.html index.html;
	} 
}