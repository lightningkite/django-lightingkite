
## 1.2.0
- add args and kwargs support to notifications via and send methods. for additional information.
- fix issue with twilio channel checking sms to and from numbers. 

## 1.1.5
- Bump version

## 1.1.4
- Attempt to bump version

## 1.1.3
- add test environment check

## 1.1.2
- bumped version no changes. 

## 1.1.1
- fix from email bug

## 1.1.0
- added email_from_template and pynliner dependency

## 1.0.1
- added migrations for notifications module
- added a default app config to notifications module
- added an admin view to notifications module 

## 1.0.0
- set twilio setting defaults to None
- raise exception if twilio settings are missing
- refactor notification exceptions
(breaking)
- filter settings results by isupper

## 0.4.6
- support both SENTRY_DSN and DJANGO_SENTRY_DSN
- add USE_X_FORWARDED_HOST and SECURE_PROXY_SSL_HEADER defaults

## 0.4.5
- add AWS_STATIC_LOCATION env setting
- add AWS_MEDIA_LOCATION env setting
- set defaults for non dev STATIC_ROOT and MEDIA_ROOT

## 0.4.4
- add email validation to serializers

## 0.4.3
- fix Aws variable defaults
- add env variables and settings to configure docs module.
- add changelog.
