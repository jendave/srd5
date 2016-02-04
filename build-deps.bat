ECHO "Entering docbook-build directory"
cd docbook-build

ECHO "Starting clean build"
.\gradlew.bat clean build uploadArchives

ECHO "Complete"