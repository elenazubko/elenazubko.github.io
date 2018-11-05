#!/usr/bin/perl
use CGI':standard';
use strict;
print "Content-type: text/html\n\n";

print qq{
<html>
	<head>
	<style>
	.font {
		font-family: 'Press Start 2P', cursive;
		color: white;
		text-Align: center;
	}
	.background{
		background-color: rgb(28, 48, 81);
	}
.white {
    color: white;
}
	
	</style>
	</head>
	<body class="background">
		
		<h1 class="font">This is my first Perl program</h1>
	</body>
</html>	
};