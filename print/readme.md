# Printing from Domjudge

In case that the Domjudge is deployed on a unreachable server,
we can't directly connect a printer to it.
It's why this folder exists.

You need cups, paps, ps2pdf installed to print,
as well as python3 and pip3 to run the server.

Following is how to use it:

1. Connect your printer to your PC, config it in CUPS and set as the default
printer so that **lp** command will print. You could test with the
**printsrc** script.

2. Make a venv and install the **requirement.txt**.

3. Execute the **start** script.

4. Upload the **printcode** script in client folder to a proper place in
Domjudge server. If Domjudge is running in Docker, move the script into
domserver container. 

5. Set the print command in Domjudge to

> printcode [teamname] [location] [original] [file]

6. Test with a demo team.
