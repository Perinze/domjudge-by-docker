# Domjudge by Docker

This is a note written to make it easier to deploy Domjudge.

1. Install Docker as well as Docker-Compose to your server.

2. Upload **docker-compose.yml** to the server.

3. Replace all the **$variable** with proper value. Notice that the
same **$variable** should have the same value. You can leave those
in cds to be modified later.

4. Run **docker compose up -d mariadb domserver**.

5. Get the admin password and restapi key. They are in
**/opt/domjudge/domserver/etc/** in domserver container,
**initial_admin_password.secret** and **restapi.secret**
respectively.

6. Edit **docker-compose.yml**, replace all **$restapi_key**
with the restapi key in the previous step.

7. Login to the admin account, create cds account and contest for
test. Then edit the **$variable** in cds.

8. Edit **accounts.yaml**. It's accounts in cds.

9. Execute **docker compose up -d** to run all containers.

## Tips

1. Check the Config checker in Domjudge.

2. Cds is running observing exactly one contest. If you create a new
contest, please modify or add one cds container.

3. If you can't connect your printer to the server, check the
**print** folder.
