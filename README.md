# Export extended data

This little script can be used to extract extended data from Decidim's `decidim_users` column and export flat tables with statistics to Excel.

It can be useful when gathering extended data through modules such as [decidim-module-extended_socio_demographic_authorization_handler](https://github.com/OpenSourcePolitics/decidim-module-extended_socio_demographic_authorization_handler) or [decidim-module-extra_user_fields](https://github.com/PopulateTools/decidim-module-extra_user_fields).

## Install

```bash
pip install -r requirements.txt
```

## Use

Export the required data from your Decidim instance's database with the following command:

```sql
SELECT type, extended_data FROM decidim_users;
```

Export the file to CSV as *decidim_users.csv* and put it in the same folder as the script.

Then just run:

```python
python create_statistics.py
```

In the same folder, an excel file named *statistics.xlsx* will be created with one tab per category of extended data.

## LICENSE

Feel free to reuse this code, it is published under AGPLv3.
