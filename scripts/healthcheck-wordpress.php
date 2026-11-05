<?php
require '/var/www/html/wp-load.php';
exit(function_exists('mee_production_plan') && (int)$wpdb->get_var('SELECT 1')===1 ? 0 : 1);
