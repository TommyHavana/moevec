<?php
// Recurso editorial único. Ejecutar con PHP CLI dentro de WordPress.
if (PHP_SAPI !== 'cli' || empty($argv[1])) { exit(1); }
require '/var/www/html/wp-load.php';
require_once ABSPATH . 'wp-admin/includes/file.php';
$path = $argv[1];
$name = 'e1-6-15-plantilla-12-semanas.csv';
if (basename($path) !== $name || !is_file($path)) { throw new RuntimeException('Recurso inesperado'); }
$rows = array_map(fn($line) => str_getcsv($line, ';'), file($path, FILE_IGNORE_NEW_LINES));
if (count($rows) !== 13 || count($rows[0]) !== 8) { throw new RuntimeException('CSV incompleto'); }
$key = 'E1.6.15-plan-12-semanas-v1';
$hash = hash_file('sha256', $path);
$existing = get_posts(['post_type'=>'attachment','post_status'=>'any','posts_per_page'=>2,'meta_key'=>'_mee_support_asset','meta_value'=>$key]);
if ($existing) {
    if (count($existing) !== 1 || get_post_meta($existing[0]->ID, '_mee_resource_sha256', true) !== $hash) { throw new RuntimeException('Revisar recurso existente'); }
    echo json_encode(['created'=>false,'existing'=>true,'attachment_id'=>$existing[0]->ID,'url'=>wp_get_attachment_url($existing[0]->ID),'sha256'=>$hash]);
    exit;
}
$upload = wp_upload_bits($name, null, file_get_contents($path));
if ($upload['error']) { throw new RuntimeException($upload['error']); }
$id = wp_insert_attachment(['post_mime_type'=>'text/csv','post_title'=>'MEE · Plantilla de proyecto de 12 semanas','post_status'=>'inherit','post_content'=>'Plan educativo adaptable; no garantiza una venta.'], $upload['file'], 0, true);
if (is_wp_error($id)) { throw new RuntimeException($id->get_error_message()); }
update_post_meta($id, '_mee_support_asset', $key);
update_post_meta($id, '_mee_resource_sha256', $hash);
echo json_encode(['created'=>true,'attachment_id'=>$id,'url'=>wp_get_attachment_url($id),'sha256'=>$hash], JSON_UNESCAPED_SLASHES|JSON_UNESCAPED_UNICODE);
