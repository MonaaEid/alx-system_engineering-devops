#!/usr/bin/env ruby
# Ruby script that accepts one argument and pass it to a regular expression matching method
string = ARGV[0]
regex = /^\d{10}$/
matches = string.scan(regex)
puts matches.join

