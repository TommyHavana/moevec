<?php
defined('ABSPATH') || exit;
function mee_smtp_config() {
    static $config;
    if (isset($config)) return $config;
    $path = defined('MEE_SMTP_CONFIG_FILE') ? MEE_SMTP_CONFIG_FILE : '/run/mee-secrets/contact-smtp.json';
    $config = is_readable($path) ? json_decode(file_get_contents($path), true) : [];
    return is_array($config) ? $config : [];
}
add_action('phpmailer_init', function($mail) {
    $c = mee_smtp_config();
    if (empty($c['password']) || empty($c['username'])) return;
    $mail->isSMTP(); $mail->Host = $c['host'] ?? 'smtp.dondominio.com';
    $mail->Port = (int)($c['port'] ?? 465); $mail->SMTPSecure = 'ssl';
    $mail->SMTPAuth = true; $mail->Username = $c['username']; $mail->Password = $c['password'];
    $mail->Timeout = 15; $mail->SMTPDebug = 0;
    $mail->setFrom('contacto@moevec.org', 'MEE · Movimiento de Evolución Económica', false);
});
function mee_client_hash() {
    // Nginx replaces this header with the proxy's verified client address.
    $ip = $_SERVER['HTTP_X_REAL_IP'] ?? ($_SERVER['REMOTE_ADDR'] ?? 'unknown');
    if (!filter_var($ip, FILTER_VALIDATE_IP)) $ip = 'unknown';
    return hash_hmac('sha256', $ip, wp_salt('auth'));
}
function mee_mail_html($title, $intro, $body, $reference) {
    return '<!doctype html><html lang="es"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1"></head><body style="margin:0;background:#f7f6f2;color:#15171b;font-family:Arial,Helvetica,sans-serif"><table role="presentation" width="100%" cellspacing="0" cellpadding="0"><tr><td style="padding:32px 16px"><table role="presentation" width="600" cellspacing="0" cellpadding="0" style="width:100%;max-width:600px;margin:auto"><tr><td style="padding:24px 28px;background:#1547bb"><img src="https://moevec.org/brand/mee-logo-blanco-rojo-640.webp" width="130" alt="MEE" style="display:block;width:130px;height:auto"></td></tr><tr><td style="background:#ffffff;padding:36px 28px"><p style="font-size:13px;color:#55595f">Movimiento de Evolución Económica</p><h1 style="font-size:34px;line-height:1.1;letter-spacing:-1px;margin:20px 0">'.esc_html($title).'</h1><p style="font-size:17px;line-height:1.6">'.esc_html($intro).'</p>'.$body.'<p style="font-size:12px;color:#55595f;margin-top:32px">Referencia: '.esc_html($reference).'</p></td></tr><tr><td style="padding:24px 28px;background:#15171b;color:#ffffff"><p style="margin:0;font-size:14px;line-height:1.6">La próxima idea puede empezar contigo.</p><p style="margin:16px 0 0;font-size:12px"><a href="https://moevec.org" style="color:#ffffff">moevec.org</a> &nbsp; <a href="https://moevec.org/privacidad/" style="color:#ffffff">Privacidad</a></p></td></tr></table></td></tr></table></body></html>';
}
function mee_send_confirmation($email, $name, $reference) {
    $body = '<p style="font-size:16px;line-height:1.7">Hemos recibido tu mensaje y podremos continuar la conversación por este correo. Este acuse confirma la recepción; no indica un plazo de respuesta.</p><p style="font-size:16px;line-height:1.7">Si necesitas añadir algo, responde a este correo e incluye la referencia.</p><p style="font-size:13px;line-height:1.6;color:#55595f">Si no has enviado un mensaje a MEE, puedes ignorar este correo o avisarnos en contacto@moevec.org.</p>';
    return wp_mail($email, 'Hemos recibido tu mensaje · MEE ['.$reference.']', mee_mail_html('Ya hemos dado el primer paso.', 'Hola, '.$name.'. Gracias por escribir a MEE.', $body, $reference), ['Content-Type: text/html; charset=UTF-8', 'Reply-To: MEE <contacto@moevec.org>']);
}
add_action('mee_confirmation_retry', function($email, $name, $reference) { mee_send_confirmation($email,$name,$reference); }, 10, 3);
function mee_contact_error($code,$message,$status=400){return new WP_Error($code,$message,['status'=>$status]);}
function mee_contact_token() {
    $nonce = bin2hex(random_bytes(16)); $issued = time();
    $payload = $issued.'.'.$nonce;
    $token = $payload.'.'.hash_hmac('sha256', $payload.'.'.mee_client_hash(), wp_salt('nonce'));
    return new WP_REST_Response(['token'=>$token],200,['Cache-Control'=>'no-store, private']);
}
function mee_contact_submit(WP_REST_Request $request) {
    if (!empty($_SERVER['HTTP_ORIGIN']) && $_SERVER['HTTP_ORIGIN'] !== 'https://moevec.org') return mee_contact_error('origin','El origen de la solicitud no es válido.',403);
    if (strlen($request->get_body()) > 18000) return mee_contact_error('size','El mensaje supera el tamaño permitido.',413);
    $p = $request->get_json_params(); if (!is_array($p)) return mee_contact_error('json','Revisa los datos del formulario.');
    $token = (string)($p['token']??''); $parts=explode('.',$token);
    if(count($parts)!==3 || !ctype_digit($parts[0]) || !preg_match('/^[a-f0-9]{32}$/',$parts[1])) return mee_contact_error('token','Recarga la página e intenta enviar el mensaje de nuevo.',403);
    [$issued,$nonce,$signature]=$parts;
    $age=time()-(int)$issued;
    $expected=hash_hmac('sha256',$issued.'.'.$nonce.'.'.mee_client_hash(),wp_salt('nonce'));
    if($age<2 || $age>1800 || !hash_equals($expected,$signature)) return mee_contact_error('expired','La sesión de envío ha caducado. Inténtalo de nuevo.',403);
    $used='mee_contact_used_'.hash('sha256',$nonce);
    $accepted=get_transient($used); if($accepted) return new WP_REST_Response(['ok'=>true,'reference'=>$accepted,'message'=>'Tu mensaje ya ha sido recibido.'],200,['Cache-Control'=>'no-store']);
    if(!empty($p['website'])) return new WP_REST_Response(['ok'=>true,'message'=>'Mensaje recibido.'],200,['Cache-Control'=>'no-store']);
    $name=trim(sanitize_text_field($p['name']??''));$email=trim((string)($p['email']??''));$message=trim(sanitize_textarea_field($p['message']??''));$subject=sanitize_text_field($p['subject']??'Consulta general');
    if(mb_strlen($name)<2 || mb_strlen($name)>100 || !is_email($email) || strlen($email)>254 || preg_match('/[\r\n]/',$email) || mb_strlen($message)<30 || mb_strlen($message)>6000 || empty($p['privacy'])) return mee_contact_error('validation','Revisa el nombre, el correo, el mensaje y la información de privacidad.');
    $allowed=['Participar en MEE','Proponer una colaboración','Consulta editorial','Otra consulta',''];
    if(!in_array($subject,$allowed,true))$subject='Consulta general';
    $keys=['mee_contact_ip_'.mee_client_hash()=>3,'mee_contact_email_'.hash_hmac('sha256',strtolower($email),wp_salt('auth'))=>2,'mee_contact_global'=>30];
    foreach($keys as $key=>$limit){if((int)get_transient($key)>=$limit)return mee_contact_error('rate','Has alcanzado el límite temporal de envíos. Espera 15 minutos o escribe a contacto@moevec.org.',429);}
    if(empty(mee_smtp_config()['password']))return mee_contact_error('unavailable','El envío no está disponible ahora. Puedes escribir a contacto@moevec.org.',503);
    foreach($keys as $key=>$limit)set_transient($key,(int)get_transient($key)+1,15*MINUTE_IN_SECONDS);
    $reference='MEE-'.gmdate('Ymd').'-'.strtoupper(substr(bin2hex(random_bytes(5)),0,8));
    $body='<table role="presentation" style="width:100%;font-size:14px;line-height:1.6"><tr><td><strong>Nombre</strong><br>'.esc_html($name).'</td></tr><tr><td style="padding-top:16px"><strong>Correo</strong><br>'.esc_html($email).'</td></tr><tr><td style="padding-top:16px"><strong>Tema</strong><br>'.esc_html($subject?:'Consulta general').'</td></tr></table><div style="font-size:16px;line-height:1.7;margin-top:28px;padding-top:24px;border-top:1px solid #d0d0ce">'.nl2br(esc_html($message)).'</div>';
    $ok=wp_mail('contacto@moevec.org','Nueva consulta · MEE ['.$reference.']',mee_mail_html('Una nueva conversación.', 'Ha llegado una consulta desde moevec.org.', $body, $reference),['Content-Type: text/html; charset=UTF-8','Reply-To: '.$email]);
    if(!$ok)return mee_contact_error('delivery','No se ha podido entregar el mensaje. Inténtalo más tarde o escribe a contacto@moevec.org.',502);
    set_transient($used,$reference,30*MINUTE_IN_SECONDS);
    $confirmed=mee_send_confirmation($email,$name,$reference);
    if(!$confirmed)wp_schedule_single_event(time()+120,'mee_confirmation_retry',[$email,$name,$reference]);
    return new WP_REST_Response(['ok'=>true,'reference'=>$reference,'message'=>$confirmed?'Tu mensaje ha llegado a MEE. Hemos enviado una confirmación a tu correo.':'Tu mensaje ha llegado a MEE. El acuse por correo está pendiente de reenvío.'],200,['Cache-Control'=>'no-store, private']);
}
add_action('rest_api_init',function(){register_rest_route('mee/v1','/contact/token',['methods'=>'GET','callback'=>'mee_contact_token','permission_callback'=>'__return_true']);register_rest_route('mee/v1','/contact',['methods'=>'POST','callback'=>'mee_contact_submit','permission_callback'=>'__return_true']);});
