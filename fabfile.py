from fabric.api import local

def test():
  local("./manage.py")
def commit():
  local("git add . && git commit -m 'testing 123' ")
def push():
  local("git push origin master")
def deploy():
  print "Excuting manage script."
  print "                       "
  test()
  print "commiting git code locally."
  print "                           "
  commit()
  print "pushing local git repository to github."
  print "                                       "
  push()


