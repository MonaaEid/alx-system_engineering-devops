#!/usr/bin/env ruby
# Ruby script that accepts one argument and pass it to a regular expression matching method
string = ARGV[0]
regex = /School/
if string.match(regex)
  puts "Match found!"
else
  puts "No match found."
end
