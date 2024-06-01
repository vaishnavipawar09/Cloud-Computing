Author: Vaishnavi Vishwas Pawar (vpawar@iu.edu)
1. Folder Structure:
	VaishnaviP_Assignment3 has three files in it.
	VaishnaviP_Assignment3/ - serverFile/ - DockerFile.server - server.py 
	VaishnaviP_Assignment3/ - clientFile/ - DockerFile.client - client.py 
	VaishnaviP_Assignment3/ -docker-compose.yml

2. Build and Start Containers: Navigate to the VaishnaviP_Assignment3/ directory in the Ubuntu terminal. Build and start the Docker containers using below commands.
	docker-compose build 
	docker-compose up -d
3. Execute Scripts in Containers: Execute scripts within the server and client containers.
	docker-compose exec server sh 
	docker-compose exec client sh
4. To check if everything is working and verify logs:
	docker-compose ps 
	docker-compose logs server
	docker-compose logs client
	
All the packages to be downloaded are mentioned in docker file.
