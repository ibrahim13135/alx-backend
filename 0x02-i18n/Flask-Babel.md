## Introduction to i18n in Python with Flask-Babel

Internationalization (i18n) and localization (l10n) are essential for creating applications that cater to a global audience. Flask-Babel is an extension for Flask that simplifies adding i18n and l10n support. It leverages Babel, pytz, and speaklater libraries to provide comprehensive support for date formatting, time zones, and translations.

### Installation

First, install Flask-Babel using pip:

```bash
$ pip install Flask-Babel
```

### Configuration

After installing, you need to configure Flask-Babel in your Flask application. Here's how to get started:

```python
from flask import Flask
from flask_babel import Babel

app = Flask(__name__)
app.config.from_pyfile('mysettings.cfg')
babel = Babel(app)
```

To disable Jinja support, use:

```python
babel = Babel(app, configure_jinja=False)
```

#### Configuration Values

- `BABEL_DEFAULT_LOCALE`: Default locale, e.g., `'en'`.
- `BABEL_DEFAULT_TIMEZONE`: Default timezone, e.g., `'UTC'`.
- `BABEL_TRANSLATION_DIRECTORIES`: Paths to translation folders, e.g., `'translations'`.
- `BABEL_DOMAIN`: Message domain, e.g., `'messages'`.

### Locale and Timezone Selectors

You can define custom functions to select the locale and timezone for the user:

```python
from flask import g, request

@babel.localeselector
def get_locale():
    user = getattr(g, 'user', None)
    if user is not None:
        return user.locale
    return request.accept_languages.best_match(['de', 'fr', 'en'])

@babel.timezoneselector
def get_timezone():
    user = getattr(g, 'user', None)
    if user is not None:
        return user.timezone
```

### Formatting Dates

Flask-Babel provides functions for date formatting:

```python
from flask_babel import format_datetime
from datetime import datetime

app.test_request_context().push()

print(format_datetime(datetime(1987, 3, 5, 17, 12)))
# Output: 'Mar 5, 1987 5:12:00 PM'
```

Change the locale:

```python
app.config['BABEL_DEFAULT_LOCALE'] = 'de'
from flask_babel import refresh; refresh()

print(format_datetime(datetime(1987, 3, 5, 17, 12), 'EEEE, d. MMMM yyyy H:mm'))
# Output: 'Donnerstag, 5. März 1987 17:12'
```

### Formatting Numbers

Flask-Babel also supports number formatting:

```python
from flask_babel import format_number, format_decimal, format_currency, format_percent, format_scientific

print(format_number(1099))  # Output: '1,099'
print(format_decimal(1.2346))  # Output: '1.235'
print(format_currency(1099.98, 'USD'))  # Output: '$1,099.98'
print(format_percent(0.34))  # Output: '34%'
print(format_scientific(10000))  # Output: '1E4'
```

Change the locale:

```python
app.config['BABEL_DEFAULT_LOCALE'] = 'de'
from flask_babel import refresh; refresh()

print(format_number(1099))  # Output: '1.099'
print(format_decimal(1.2346))  # Output: '1,235'
print(format_currency(1099.98, 'USD'))  # Output: '1.099,98\xa0$'
print(format_percent(0.34))  # Output: '34\xa0%'
print(format_scientific(10000))  # Output: '1E4'
```

### Using Translations

Mark strings for translation using `gettext` and `ngettext`:

```python
from flask_babel import gettext, ngettext

print(gettext(u'A simple string'))  # Output: 'A simple string'
print(gettext(u'Value: %(value)s', value=42))  # Output: 'Value: 42'
print(ngettext(u'%(num)s Apple', u'%(num)s Apples', number_of_apples))
```

For constant strings outside of a request, use `lazy_gettext`:

```python
from flask_babel import lazy_gettext

class MyForm(formlibrary.FormBase):
    success_message = lazy_gettext(u'The form was successfully saved.')
```

### Translating Applications

1. Mark strings with `gettext` or `ngettext`.
2. Create a `babel.cfg` file:

```ini
[python: **.py]
[jinja2: **/templates/**.html]
extensions=jinja2.ext.autoescape,jinja2.ext.with_
```

3. Extract messages:

```bash
$ pybabel extract -F babel.cfg -o messages.pot .
$ pybabel extract -F babel.cfg -k lazy_gettext -o messages.pot .
```

4. Initialize translations:

```bash
$ pybabel init -i messages.pot -d translations -l de
```

5. Edit `translations/de/LC_MESSAGES/messages.po` file.
6. Compile translations:

```bash
$ pybabel compile -d translations
```

7. Update translations when strings change:

```bash
$ pybabel update -i messages.pot -d translations
```

### Troubleshooting

On macOS, ensure `LC_CTYPE` is set to UTF-8:

```bash
$ echo $LC_CTYPE
UTF-8
```

If not, add to `~/.profile`:

```bash
export LC_CTYPE=en_US.utf-8
```

Restart your terminal.

This guide should give you a comprehensive overview of using Flask-Babel for i18n and l10n in your Flask application.



### Flask-Babel API

#### Configuration

- **`Babel` Class**

  The `Babel` class is the central controller for configuring Flask-Babel. You must create or initialize an instance of this class for each application.

  ```python
  from flask_babel import Babel

  babel = Babel(app, default_locale='en', default_timezone='UTC', default_domain='messages', configure_jinja=True)
  ```

  - **Properties:**
    - `default_locale`: The default locale (e.g., `en`).
    - `default_timezone`: The default timezone (e.g., `UTC`).
    - `domain`: The message domain for translations.
  - **Methods:**
    - `init_app(app)`: Sets up the instance for use with `app`.
    - `list_translations()`: Lists all available locales for translations.
    - `localeselector(f)`: Registers a callback function for locale selection.
    - `timezoneselector(f)`: Registers a callback function for timezone selection.

#### Context Functions

- **`get_translations()`**

  Returns the correct gettext translations for the request.

  ```python
  from flask_babel import get_translations

  translations = get_translations()
  ```

- **`get_locale()`**

  Returns the locale for the current request as a `babel.Locale` object.

  ```python
  from flask_babel import get_locale

  locale = get_locale()
  ```

- **`get_timezone()`**

  Returns the timezone for the current request as a `pytz.timezone` object.

  ```python
  from flask_babel import get_timezone

  timezone = get_timezone()
  ```

#### Datetime Functions

- **`to_user_timezone(datetime)`**

  Converts a `datetime` object to the user's timezone.

  ```python
  from flask_babel import to_user_timezone
  from datetime import datetime

  user_time = to_user_timezone(datetime.utcnow())
  ```

- **`to_utc(datetime)`**

  Converts a `datetime` object to UTC and drops the `tzinfo`.

  ```python
  from flask_babel import to_utc
  from datetime import datetime

  utc_time = to_utc(datetime.utcnow())
  ```

- **`format_datetime(datetime=None, format=None, rebase=True)`**

  Formats a `datetime` object according to the given pattern. Defaults to the current time if no `datetime` is provided.

  ```python
  from flask_babel import format_datetime
  from datetime import datetime

  formatted_datetime = format_datetime(datetime.utcnow(), format='full')
  ```

- **`format_date(date=None, format=None, rebase=True)`**

  Formats a `date` object according to the given pattern. Defaults to the current time if no `date` is provided.

  ```python
  from flask_babel import format_date
  from datetime import datetime

  formatted_date = format_date(datetime.utcnow(), format='short')
  ```

- **`format_time(time=None, format=None, rebase=True)`**

  Formats a `time` object according to the given pattern. Defaults to the current time if no `time` is provided.

  ```python
  from flask_babel import format_time
  from datetime import datetime

  formatted_time = format_time(datetime.utcnow(), format='medium')
  ```

- **`format_timedelta(datetime_or_timedelta, granularity='second', add_direction=False, threshold=0.85)`**

  Formats the elapsed time from the given date to now or the given `timedelta`.

  ```python
  from flask_babel import format_timedelta
  from datetime import timedelta

  formatted_timedelta = format_timedelta(timedelta(days=2), granularity='day')
  ```

#### Number Functions

- **`format_number(number)`**

  Formats the given number for the locale in the request.

  ```python
  from flask_babel import format_number

  formatted_number = format_number(12345)
  ```

- **`format_decimal(number, format=None)`**

  Formats the given decimal number for the locale in the request.

  ```python
  from flask_babel import format_decimal

  formatted_decimal = format_decimal(12345.678)
  ```

- **`format_currency(number, currency, format=None, currency_digits=True, format_type='standard')`**

  Formats the given number as currency for the locale in the request.

  ```python
  from flask_babel import format_currency

  formatted_currency = format_currency(12345.67, 'USD')
  ```

- **`format_percent(number, format=None)`**

  Formats the given number as a percentage for the locale in the request.

  ```python
  from flask_babel import format_percent

  formatted_percent = format_percent(0.1234)
  ```

- **`format_scientific(number, format=None)`**

  Formats the given number in scientific notation for the locale in the request.

  ```python
  from flask_babel import format_scientific

  formatted_scientific = format_scientific(12345.6789)
  ```

#### Gettext Functions

- **`gettext(*args, **kwargs)`**

  Translates a single string.

  ```python
  from flask_babel import gettext

  translated_string = gettext('Hello, World!')
  ```

- **`ngettext(*args, **kwargs)`**

  Translates a string that can be singular or plural.

  ```python
  from flask_babel import ngettext

  translated_string = ngettext('%(num)d apple', '%(num)d apples', 3)
  ```

- **`pgettext(*args, **kwargs)`**

  Translates a string with a context.

  ```python
  from flask_babel import pgettext

  translated_string = pgettext('greeting', 'Hello, World!')
  ```

- **`npgettext(*args, **kwargs)`**

  Translates a string that can be singular or plural with a context.

  ```python
  from flask_babel import npgettext

  translated_string = npgettext('fruit', '%(num)d apple', '%(num)d apples', 2)
  ```

- **`lazy_gettext(*args, **kwargs)`**

  Returns a lazy-evaluated translation string.

  ```python
  from flask_babel import lazy_gettext

  lazy_string = lazy_gettext('This will be translated later')
  ```

- **`lazy_pgettext(*args, **kwargs)`**

  Returns a lazy-evaluated translation string with a context.

  ```python
  from flask_babel import lazy_pgettext

  lazy_string = lazy_pgettext('greeting', 'This will be translated later')
  ```

#### Low-Level API

- **`refresh()`**

  Refreshes cached timezone and locale information.

  ```python
  from flask_babel import refresh

  refresh()
  ```

- **`force_locale(locale)`**

  Temporarily overrides the current locale within a context manager.

  ```python
  from flask_babel import force_locale

  with force_locale('de_DE'):
      print(gettext('Hello, World!'))
  ```

This comprehensive overview of the Flask-Babel API should help you implement internationalization and localization in your Flask applications effectively.




### Introduction to `pytz`

`pytz` is a Python library designed to provide accurate and cross-platform timezone calculations by incorporating the Olson tz database. It enables developers to manage timezone-aware datetime objects effectively, making it particularly useful for handling daylight saving time changes and performing timezone conversions.

By integrating the Olson tz database, `pytz` ensures precise and consistent timezone calculations across different platforms. It addresses the challenges of ambiguous times during daylight saving time transitions. While `pytz` supports nearly all Olson timezones, it is especially valuable for Python versions prior to 3.9, as newer versions have incorporated similar functionality within the standard library, supplemented by third-party packages like `tzdata`.


### Installation

You can install `pytz` using pip:
```sh
pip install pytz
```

Or from a tarball:
```sh
python setup.py install
```

### Basic Usage

#### Importing and Initialization
```python
from datetime import datetime, timedelta
from pytz import timezone
import pytz

# Getting timezone objects
utc = pytz.utc
eastern = timezone('US/Eastern')
amsterdam = timezone('Europe/Amsterdam')
```

### Timezone Localization

#### Localizing Naive Datetime Objects
You can localize a naive datetime (a datetime without timezone information) using the `localize` method:
```python
fmt = '%Y-%m-%d %H:%M:%S %Z%z'
loc_dt = eastern.localize(datetime(2002, 10, 27, 6, 0, 0))
print(loc_dt.strftime(fmt))
# Output: 2002-10-27 06:00:00 EST-0500
```

#### Converting Localized Times
You can convert an existing localized datetime to another timezone using the `astimezone` method:
```python
ams_dt = loc_dt.astimezone(amsterdam)
print(ams_dt.strftime(fmt))
# Output: 2002-10-27 12:00:00 CET+0100
```

### Timezone Conversion

#### Working with UTC
It's recommended to work with UTC and convert to local time when needed:
```python
utc_dt = datetime(2002, 10, 27, 6, 0, 0, tzinfo=utc)
loc_dt = utc_dt.astimezone(eastern)
print(loc_dt.strftime(fmt))
# Output: 2002-10-27 01:00:00 EST-0500
```

### Date Arithmetic with Timezones

#### Handling Daylight Saving Time
When performing date arithmetic, use the `normalize` method to handle DST transitions:
```python
before = loc_dt - timedelta(minutes=10)
print(before.strftime(fmt))
# Output: 2002-10-27 00:50:00 EST-0500

normalized_before = eastern.normalize(before)
print(normalized_before.strftime(fmt))
# Output: 2002-10-27 01:50:00 EDT-0400

after = eastern.normalize(before + timedelta(minutes=20))
print(after.strftime(fmt))
# Output: 2002-10-27 01:10:00 EST-0500
```

### Creating Local Times

#### Handling Ambiguous Times
Creating local times directly with `tzinfo` is not recommended due to ambiguities:
```python
dt = datetime(2002, 10, 27, 1, 30, 0)
dt1 = eastern.localize(dt, is_dst=True)
print(dt1.strftime(fmt))
# Output: 2002-10-27 01:30:00 EDT-0400

dt2 = eastern.localize(dt, is_dst=False)
print(dt2.strftime(fmt))
# Output: 2002-10-27 01:30:00 EST-0500
```

### Converting Between Timezones

#### Example of Timezone Conversion
```python
utc_dt = datetime.fromtimestamp(1143408899, tz=utc)
print(utc_dt.strftime(fmt))
# Output: 2006-03-26 21:34:59 UTC+0000

au_tz = timezone('Australia/Sydney')
au_dt = utc_dt.astimezone(au_tz)
print(au_dt.strftime(fmt))
# Output: 2006-03-27 08:34:59 AEDT+1100

utc_dt2 = au_dt.astimezone(utc)
print(utc_dt2.strftime(fmt))
# Output: 2006-03-26 21:34:59 UTC+0000

print(utc_dt == utc_dt2)
# Output: True
```

### Handling Ambiguous Times

#### Using `is_dst` Parameter
The `is_dst` parameter resolves ambiguities during DST transitions:
```python
tz = timezone('America/St_Johns')
normal = datetime(2009, 9, 1)
ambiguous = datetime(2009, 10, 31, 23, 30)

print(tz.utcoffset(normal, is_dst=True))
# Output: -1 day, 21:30:00

print(tz.dst(normal, is_dst=True))
# Output: 1:00:00

print(tz.tzname(normal, is_dst=True))
# Output: NDT

print(tz.utcoffset(ambiguous, is_dst=True))
# Output: -1 day, 21:30:00

print(tz.dst(ambiguous, is_dst=True))
# Output: 1:00:00

print(tz.tzname(ambiguous, is_dst=True))
# Output: NDT

print(tz.utcoffset(normal, is_dst=False))
# Output: -1 day, 21:30:00

print(tz.dst(normal, is_dst=False).seconds)
# Output: 3600

print(tz.tzname(normal, is_dst=False))
# Output: NDT

print(tz.utcoffset(ambiguous, is_dst=False))
# Output: -1 day, 20:30:00

print(tz.dst(ambiguous, is_dst=False))
# Output: 0:00:00

print(tz.tzname(ambiguous, is_dst=False))
# Output: NST
```

### Handling AmbiguousTimeError

If `is_dst` is not specified, ambiguous timestamps raise an `AmbiguousTimeError`:
```python
import pytz.exceptions

try:
    tz.utcoffset(ambiguous)
except pytz.exceptions.AmbiguousTimeError:
    print('pytz.exceptions.AmbiguousTimeError: %s' % ambiguous)
# Output: pytz.exceptions.AmbiguousTimeError: 2009-10-31 23:30:00
```

By using `pytz`, you can manage timezones effectively, handle daylight saving transitions, and perform accurate datetime calculations in your Python applications.






## Installation

You can install `pytz` using `pip`:

```sh
pip install pytz
```

Alternatively, you can install from a tarball:

```sh
python setup.py install
```

## Example & Usage

### Localized Times and Date Arithmetic

To work with localized times, use `localize()` and `astimezone()` methods:

```python
from datetime import datetime, timedelta
from pytz import timezone
import pytz

utc = pytz.utc
eastern = timezone('US/Eastern')
amsterdam = timezone('Europe/Amsterdam')
fmt = '%Y-%m-%d %H:%M:%S %Z%z'

# Localize naive datetime
loc_dt = eastern.localize(datetime(2002, 10, 27, 6, 0, 0))
print(loc_dt.strftime(fmt))  # 2002-10-27 06:00:00 EST-0500

# Convert to another timezone
ams_dt = loc_dt.astimezone(amsterdam)
print(ams_dt.strftime(fmt))  # 2002-10-27 12:00:00 CET+0100

# Work in UTC and convert to localtime
utc_dt = datetime(2002, 10, 27, 6, 0, 0, tzinfo=utc)
loc_dt = utc_dt.astimezone(eastern)
print(loc_dt.strftime(fmt))  # 2002-10-27 01:00:00 EST-0500

# Date arithmetic with local times
before = loc_dt - timedelta(minutes=10)
print(before.strftime(fmt))  # 2002-10-27 00:50:00 EST-0500
print(eastern.normalize(before).strftime(fmt))  # 2002-10-27 01:50:00 EDT-0400

# Handle daylight saving transitions
dt = datetime(2002, 10, 27, 1, 30, 0)
dt1 = eastern.localize(dt, is_dst=True)
print(dt1.strftime(fmt))  # 2002-10-27 01:30:00 EDT-0400
dt2 = eastern.localize(dt, is_dst=False)
print(dt2.strftime(fmt))  # 2002-10-27 01:30:00 EST-0500

# Convert between timezones
utc_dt = datetime.fromtimestamp(1143408899, tz=utc)
au_tz = timezone('Australia/Sydney')
au_dt = utc_dt.astimezone(au_tz)
print(au_dt.strftime(fmt))  # 2006-03-27 08:34:59 AEDT+1100
```

### Problems with Localtime

Ambiguous datetimes occur during DST transitions. For example, in `US/Eastern`:

```python
loc_dt = eastern.localize(datetime(2002, 10, 27, 1, 30, 0))
print(loc_dt.strftime(fmt))  # 2002-10-27 01:30:00 EST-0500
```

To avoid ambiguity, stick with UTC:

```python
import pickle, pytz

dt = datetime(2005, 3, 1, 14, 13, 21, tzinfo=utc)
naive = dt.replace(tzinfo=None)
p = pickle.dumps(dt, 1)
new = pickle.loads(p)
print(new == dt)  # True
print(pytz.utc is pytz.UTC is pytz.timezone('UTC'))  # True
```

For unambiguous local times:

```python
dt = datetime(2002, 10, 27, 1, 30, 0)
est_dt = eastern.localize(dt, is_dst=True)
edt_dt = eastern.localize(dt, is_dst=False)
print(est_dt.strftime(fmt) + ' / ' + edt_dt.strftime(fmt))
# 2002-10-27 01:30:00 EDT-0400 / 2002-10-27 01:30:00 EST-0500

try:
    eastern.localize(dt, is_dst=None)
except pytz.exceptions.AmbiguousTimeError:
    print('pytz.exceptions.AmbiguousTimeError: %s' % dt)
# pytz.exceptions.AmbiguousTimeError: 2002-10-27 01:30:00

# Handle non-existent times
dt = datetime(2002, 4, 7, 2, 30, 0)
try:
    eastern.localize(dt, is_dst=None)
except pytz.exceptions.NonExistentTimeError:
    print('pytz.exceptions.NonExistentTimeError: %s' % dt)
# pytz.exceptions.NonExistentTimeError: 2002-04-07 02:30:00
```

### Handling Historical Timezone Transitions

```python
warsaw = pytz.timezone('Europe/Warsaw')
amb_dt1 = warsaw.localize(datetime(1915, 8, 4, 23, 59, 59), is_dst=True)
amb_dt2 = warsaw.localize(datetime(1915, 8, 4, 23, 59, 59), is_dst=False)
switch_dt = warsaw.localize(datetime(1915, 8, 5, 0, 0, 0), is_dst=False)

print(amb_dt1.strftime(fmt))  # '1915-08-04 23:59:59 WMT+0124'
print(amb_dt2.strftime(fmt))  # '1915-08-04 23:59:59 CET+0100'
print(switch_dt.strftime(fmt))  # '1915-08-05 00:00:00 CET+0100'
```

### Timezone Conversion

```python
utc_dt = datetime(1915, 8, 4, 22, 36, tzinfo=pytz.utc)
print(utc_dt.astimezone(warsaw).strftime(fmt))  # '1915-08-04 23:36:00 CET+0100'
```

## Country Information

Get timezones for a country using ISO 3166 codes:

```python
print(' '.join(pytz.country_timezones['nz']))  # Pacific/Auckland Pacific/Chatham
print(pytz.country_names['nz'])  # New Zealand
```

## Helpers

Lists of timezones:

```python
from pytz import all_timezones, common_timezones

print(len(all_timezones) >= 500)  # True
print('Etc/Greenwich' in all_timezones)  # True

print(len(common_timezones) < len(all_timezones))  # True
print('Etc/Greenwich' in common_timezones)  # False
```

## What is UTC?

UTC is the standard for regulating clocks and time measurement. No daylight saving time occurs in UTC, making it ideal for date arithmetic.

## Further Reading

For more information about timezones: [IANA Time Zone Database](https://data.iana.org/time-zones/tz-link.html)
