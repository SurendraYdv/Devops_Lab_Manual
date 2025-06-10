#IN CMD

mkdir program4
cd program4

mvn archetype:generate -DgroupId=com.example -DartifactId=maven-example -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false

cd maven-example

#Step 2: Open The pom.xml File
notepad pom.xml

#OPTIONAL
#Step 3: Open Java Code (App.java) File


#Step 4: Run the Project
mvn clean install

mvn exec:java -Dexec.mainClass="com.example.App"

#Step 5: Migrate the Maven Project to Gradle
gradle init

# It will ask Found a Maven build. Generate a Gradle build from this? (default: yes) [yes, no]
Yes

# Select build script DSL:
1: Kotlin
2: Groovy
Enter selection (default: Kotlin) [1..2]
2

# Generate build using new APIs and behavior (some features may change in the next minor release)? (default: no) [yes, no]
No

#Navigate the project folder and open build.gradle
plugins {
    id 'java'
}

group = 'com.example'
version = '1.0-SNAPSHOT'

repositories {
    mavenCentral()
}

dependencies {
    testImplementation 'junit:junit:4.12'
}

task run(type: JavaExec) {
    main = 'com.example.App'
    classpath = sourceSets.main.runtimeClasspath
}

#Step 6: Run the Gradle Project

gradlew build

gradlew run

