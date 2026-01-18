'''
git commands-------------->
1. git -v (to see the current version)
2. git init (to initialze a repository/folder)
3. git status (to see the current file status of file or code)
4. git add.  (to add files in the staging step)--------  STAGING STEP
   it restore --staged <file name> (this will remove the file from staging process), in this the changes are no reverted. so to revert it back to the original state run "git restore" command
   --------UNSTAGING STEP
5. git commit -m "inital commit" (this is to commit the files in the current repository) 
6. git commit -m "Redesigned Homepage" (this is to commit the files in the current repository) 
7. git log (to view the history of commited changes within a git repository)
8. git log --oneline (this is will display all the committed changes of log in a simplified manner) 
9. git config --list (show the added username,email, address etc and many other things)
10. git config --global user.name "shreyash" (adds the username)
11. git config --global user.email " shreyash.capricorn21@gmail.com"(adds the email)
12. git clone (copy paste url or link) ---(clone a repository)
13. git diff(shows the exact changes made in the file) press Q to exit this state
14. git restore <file name> (it restores the previous changes in the file you've made changes)

16. git restore . (this is very important command as this will restore all the file to its original state.)
17. git commit --amend -m " the message you want" (this will allow you to change an existing message of a specified file)
18. git reset HEAD~1 (This will revert one commit back of the file which was last committed )
19. .gitignore (this contains a file that will be ignored and won't be visible in the git bash terminal)
20. *.log (this will ignore all the log files)
21. node_modules/ (this will ignore the directories)
22. !important.log (this will show the log file which is not being ignore) 
23. git rm <filename> (remove file from repository and disk)
24. git rm --cached <filename> (remove file from repository but keep on disk)
25. git mv <oldfile name> then <new file name> (this "mv" will change the file name)
26. git switch -c ui-revolution (this will create a new branch named "ui -revolution")
27. git switch master (this will switch to the default branch called "branch master")
28. 
29.
30.
'''

