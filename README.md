Planet Terasi Aggregator
========================

This is the code that runs [Planet Terasi](http://planet.terasi.net).


Deploy to production
--------------------

```bash
# (push changes in master to origin)
git checkout production
git merge origin/master
git push origin production
git push -f heroku production:master
```


Modifying assets
----------------

```bash
# modify files in aggregator/static/
python manage.py collectstatic
python manage.py compress --force
git commit
git push origin master
```


Development
-----------

```bash
pip install virtualenvwrapper
# update shell to source /usr/local/bin/virtualenvwrapper.sh
mkvirtualenv planet-terasi
workon planet-terasi
brew install libmemcached    # for pylibmc
pip install -r requirements.txt
```
