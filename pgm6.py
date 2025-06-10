pwd                     # Check present working directory
cd Desktop              # Change directory to Desktop
mkdir gitproject        # Create a new folder named 'gitproject'
cd gitproject           # Move into the 'gitproject' directory
                



git config --global user.name "yourname"
git config --global user.email "you@example.com"
git config --global --list

git init   # Initialize an empty Git repository
git add .
git commit -m "Initial commit"

git remote add origin https://github.com/yourusername/yourrepo.git
git remote -v

git push -u origin master  # Or use main if your repo uses main branch