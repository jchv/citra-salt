<?php
//     ____     _     _       ___      ____
//   .   _ /  ._ /  .  /    /  _ /  .  _   /
//  /  /_    /  /  /  . /  /  /   /  /_/  /
//  ' __ /  '_ /  '_ /    '_ /    \__.   |
//
//  This file is managed by SaltStack.
//  Do not modify on-server.
//

// Admin
$config['super_admins'] = '1';
$config['admin_dir'] = 'admin';
$config['hide_admin_links'] = 0;

// Database
$config['db_encoding'] = 'utf8';
$config['database']['type'] = 'pgsql';
$config['database']['hostname'] = '{{ salt['pillar.get']('db:host') }}';
$config['database']['username'] = '{{ salt['pillar.get']('db:username') }}';
$config['database']['password'] = '{{ salt['pillar.get']('db:password') }}';
$config['database']['database'] = '{{ salt['pillar.get']('db:name') }}';
$config['database']['table_prefix'] = 'mybb_';

// Memcache
$config['cache_store'] = 'memcached';
$config['memcached']['host'] = 'localhost';
$config['memcached']['port'] = 11211;

// Logging
$config['log_pruning'] = array(
    'admin_logs' => 365,
    'mod_logs' => 365,
    'task_logs' => 30,
    'mail_logs' => 180,
    'user_mail_logs' => 180,
    'promotion_logs' => 180
);
?>
