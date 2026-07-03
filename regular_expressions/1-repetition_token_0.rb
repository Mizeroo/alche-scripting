#!/usr/bin/env ruby
arg = ARGV[0]
regex = /hbt[1,5]/
puts arg.scan(regex)