#!/usr/bin/env ruby
# Ruby script that accepts one argument and pass it to a regular expression matching method
string = ARGV[0]
regex = /hb?tn/
matches = string.scan(regex)
puts matches.join
