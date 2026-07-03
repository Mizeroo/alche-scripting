#!/usr/bin/env ruby

arg = ARGV[0]
regex = /School/

puts arg.scan(regex)
