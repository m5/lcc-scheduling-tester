
schedule_box=/home/mfivecoa/src/pylons/schedule_box CD=. filter="*" {
 MANIFEST.in
 README.txt
 development.ini
 ez_setup.py
 setup.cfg
 setup.py
 test.ini
 docs=docs {
  index.txt
 }
 schedule_box=schedule_box {
  __init__.py
  websetup.py
  config=config {
   __init__.py
   deployment.ini_tmpl
   environment.py
   middleware.py
   routing.py
  }
  controllers=controllers {
   __init__.py
   edit.py
   error.py
  }
  forms=forms{
   __init__.py
   edit.py
  }
  lib=lib {
   __init__.py
   app_globals.py
   base.py
   helpers.py
  }
  model=model {
   __init__.py
   meta.py
  }
  public=public {
   bg.png
   favicon.ico
   index.html
   pylons-logo.gif
  }
  templates=templates {
   algorithm.mako
  }
  tests=tests {
   __init__.py
   test_models.py
   functional=functional {
    __init__.py
   }
  }
 }
 schedule_box.egg-info=schedule_box.egg-info {
  PKG-INFO
  SOURCES.txt
  dependency_links.txt
  entry_points.txt
  not-zip-safe
  paster_plugins.txt
  requires.txt
  top_level.txt
 }
}
