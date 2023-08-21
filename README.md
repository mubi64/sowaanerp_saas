## SowaanERP SaaS

App to Manage SowaanERP SaaS model

#### How to Install
```
bench get-app https://github.com/mubi64/sowaanerp_saas
bench --site *site_name* install-app sowaanerp_saas
```

### Usage
Install the app. It will add quota.json file in parallel of site_config.json file
Contents will look similar:

```json
{
 "valid_till": "2023-03-19"
}
```
at the time of installation it will set the valid_till date to 1 year (today + 1year)

Once the valid_till date is passed, at the time of login it will throw this error:

<img width="1432" alt="image" src="https://github.com/mubi64/sowaanerp_saas/assets/17858365/ab8a32f8-3861-4f98-9762-c287e4681201">


#### License

MIT
