#in cmd

#Working with Gradle Project (Kotlin DSL)

mkdir pgm3
cd prm3

gradle init --type java-application

# while creating project it will ask necessary requirement:

Enter target Java version (min: 7, default: 21): 17

# Project name (default: program3-kotlin): kotlinProject
# Select application structure:
1: Single application project
2: Application and library project
Enter selection (default: Single application project) [1..2] 1

# Select build script DSL:
1: Kotlin
2: Groovy
Enter selection (default: Kotlin) [1..2] 1

# Select test framework:
1: JUnit 4
2: TestNG
3: Spock
4: JUnit Jupiter
Enter selection (default: JUnit Jupiter) [1..4] 1

# Generate build using new APIs and behavior (some features may change in the next minor release)? (default: no) [yes, no]
no


#OPTIONAL
Step 2: build.gradle.kts (Kotlin DSL)
Step 3: Main.kt (Change file name and update below 
Step 4: MainTest.kt (JUnit Test) (Change file name and update below code)                 


#Step 5: Run Gradle Commands

gradle build

gradle run

gradle test