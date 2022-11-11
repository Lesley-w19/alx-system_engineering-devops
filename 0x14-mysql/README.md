## 0x14-mysql


### TASKS
0. Install MySQL
---- Install MySQL --version 5.7* to web-01 and web-02
1. Let us in!
----
Create a MySQL user named holberton_user on both web-01 and web-02 with the host name set to localhost and the password projectcorrection280hbtn. This will allow us to access the replication status on both servers.
----
Make sure that holberton_user has permission to check the primary/replica status of your databases.

2. If only you could see what I've seen with your eyes
-----
Create a database named tyrell_corp.
----
Within the tyrell_corp database create a table named nexus6 and add at least one entry to it.
----
Make sure that holberton_user has SELECT permissions on your table so that we can check that the table exists and is not empty.

3. Quite an experience to live in fear, isn't it?
----
The name of the new user should be replica_user, with the host name set to %, and can have whatever password you’d like.
----
replica_user must have the appropriate permissions to replicate your primary MySQL server.
----
holberton_user will need SELECT privileges on the mysql.user table in order to check that replica_user was created with the correct permissions.

