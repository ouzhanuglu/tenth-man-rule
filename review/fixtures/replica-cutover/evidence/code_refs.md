read paths, as of this branch

MerchantDashboardController@index   -> ReadConnection, product-approved tolerance 5 s staleness; the view shows no spendable balance   [app/Http/Controllers/MerchantDashboardController.php:34]
BalanceController@show              -> pins to WriteConnection   [app/Pinning.php:41]
PayoutStatusController@show         -> ReadConnection, 3 s staleness allowed by the product spec
LedgerExportJob                     -> WriteConnection           [app/Jobs/LedgerExportJob.php:22]
read retry middleware               -> 2 attempts on QueryException 08006/57P01, 150 ms backoff, then the statement is retried on the write connection; standby conflict 40001 is retried once before failing over  [app/Http/Middleware/RetryReads.php:12-30]
