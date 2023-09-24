#!usr/bin/env bash
# This script uses puppet to set up our client SSH configuration file so that we can connect to a server without typing a password.

file { 'etc/ssh/ssh_config':
        ensure => 'present',
  content =>
  # SSh configuration
  Host *
  PasswordAuthentication no
  IdentityFile ~/.ssh/school
}
