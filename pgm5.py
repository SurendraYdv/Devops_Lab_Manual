# 1. Installing Jenkins Locally

# Step-by-Step Guide (Window):

# 1.Prerequisites:
    #   Ensure that Java (JDK) is installed on your system. Jenkins requires Java 21. If not then click here.
    # You can check if Java is installed by running java -version in the terminal.
# 2.Install Jenkins on Window System):
    *Download the Jenkins Windows installer from the official Jenkins website.
    *Run the installer and follow the on-screen instructions. While installing choose login system: run service as LocalSystem (not recommended).
    *After then use default port or you can configure you own port like I’m using port 3030 then click on test and next.
    *After then change the directory and choose java jdk-21 path look like C:\Program Files\Java\jdk-21\.
    *After then click next, next and then it will ask permission click on yes and it will start installing.
    *After successfully installed, Jenkins will be running on port either default port or chosen port like i choose port 3030 by default (you can access it in your browser at http://localhost:8080) or http://localhost:3030.


# 2. Jenkins Setup in browser:

# After opening browser by visiting your local address the browser should look like below screenshot


It will ask administrator password so you have to navigate the above highlighted path and open that initialAdminPassword in notepad or any software to see the password.
Just copy that password and paste it and click on continue.
It will ask to customize Jenkins so click on install suggested plugin it will automatically install all required plugin.
After then create admin profile by filling all details then click on save and continue after then save and finish after then click on start using Jenkin.