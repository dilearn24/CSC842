use strict;
use warnings;
use Storable;
use Storable qw(thaw freeze);

# Single-line comment: unsafe calls below
=begin comment
Block comment:
eval $code;
system("rm -rf /");
=cut

print "Enter code> ";
my $code = <STDIN>;

# vulnerable: eval()
eval $code;

# vulnerable: system()
system("ls -la");

# vulnerable: backticks
my $dir = `pwd`;

# vulnerable: qx()
my $uptime = qx(uptime);

# vulnerable: open with pipe
open(my $fh, "|-", "sort") or die $!;

# vulnerable: regex eval with /e
my $str = "abc";
$str =~ s/(a)/uc($1)/e;

# vulnerable: require (dynamic module load)
require "Some/Module.pm";

# vulnerable: use (dynamic module load)
eval 'use Some::Other::Module';

# vulnerable: Storable::thaw (unsafe deserialization)
my $frozen = read_file("store.dat");
my $thawed = Storable::thaw($frozen);

# vulnerable: Storable::freeze (serialization)
my $dump = Storable::freeze({ key => 'value' });

sub read_file {
    my ($file) = @_;
    open(my $rf, "<", $file) or return "";
    local $/;
    my $c = <$rf>;
    close $rf;
    return $c;
}

print "Done.\n";
