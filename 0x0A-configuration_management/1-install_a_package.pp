# Inception all over again, install Puppet using puppet-lint

package { 'puppet-lint':
    ensure   => '2.1.1',
    provider => 'gem'
}
