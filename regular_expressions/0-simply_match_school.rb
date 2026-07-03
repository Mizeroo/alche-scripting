#!/usr/bin/env ruby
arg = ARGV[0]
puts "DEBUG: arg is #{arg.inspect}"
regex = /School/
puts arg.scan(regex)
