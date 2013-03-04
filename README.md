Planet Terasi Aggregator
========================

This is the code that runs [Planet Terasi](http://planet.terasi.net).


Deploy to production
--------------------

```
(push changes in master to origin)
git checkout production
git merge origin/master
git push origin production
git push heroku production:master
```


Modifying assets
----------------

```
modify files in aggregator/static/
python manage.py collectstatic
python manage.py compress --force
git commit
git push origin master
```

