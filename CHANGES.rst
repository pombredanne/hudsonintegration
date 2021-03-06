Changelog of hudsonintegration
===================================================


0.1 (unreleased)
----------------

- Using the default (2.7) python again now that we've updated to 12.04 on the
  buildbot. We use 2.7 everywhere.

- Compensating for the newer sites that have no buildout.cfg anymore. You need
  to symlink development.cfg to buildout.cfg there.

- Running bootstrap with python2.6 (jenkins' machine now has python 2.7 as the
  default and we mostly use 2.6).

- Compensating for possible git checkouts.

- Added jshint instead of jslint for nicer javascript checking.

- Excluding generated django south migration files from pep8 and pyflakes.

- Showing and counting all pep8 errors, not just the first instance of an
  error. This new behaviour is prevented if you pass 'NOREPEAT' (without the
  quotes) as a command line option.

- Added documentation.

- Added jslint checker.

- Added basic run_test and create_reports scripts that basically mimic the
  bash scripts used in hudson.

- Initial library skeleton created by thaskel.  [Reinout]
