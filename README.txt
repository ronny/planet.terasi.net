Deploy to production
====================

- (push changes in master to origin)
- git checkout production
- git merge origin/master
- git push origin production
- git push heroku production:master


Modifying assets
================

- modify files in aggregator/static/
- python manage.py collectstatic
- git commit
- git push origin master

