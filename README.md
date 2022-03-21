# Multi Coverage Demo

This repository was made to identify if [codecov](https://app.codecov.io) could handle different coverage reports and merge them all together (It turns out it can!)

This was a test to check whether or not we could merge this PR https://github.com/oamg/convert2rhel/pull/465 to actually collect coverage from the tests we ran in CentOS 7 and CentOS 8.

The code is basically pretty simple, it's just a couple of `if` statements to use different code to run in different systems (Linux and Windows). With that, we have a workflow that runs our test suite using both systems (Linux and Windows) and in the end, they upload the coverage to the codecov application.

In the first run, codecov only collected 50% of the coverage, because the Windows workflow finished and uploaded its own coverage report to codecov, then, the Linux workflow finished and uploaded its own view of the coverage report, which was about 66% of the code. After all of the finished workflows, codecov updated itself with the coverage of 100% merging all of its reports.
