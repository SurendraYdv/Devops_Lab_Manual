#in cmd

mkdir pogram2
cd program2

mvn archetype:generate -DgroupId=com.example -DartifactId=myapp -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false

#Step 2

*open the pom.xml but don't make any chnages in code 

#again in cmd 

cd myapp
notepad pom.xml

#optional but if u want u can make the changes in this two
1. App.java
2. AppTest,java           #it's better don't make any changes


#To build and run the project
mvn compile

mvn test

mvn package
 
java -cp target/myapp-1.0-SNAPSHOT.jar com.example.App