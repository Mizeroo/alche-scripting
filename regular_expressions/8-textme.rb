#!/usr/bin/env ruby

STDIN.each_line do |line|
  result = line.scan(/(?<=from:|to:|flags:).+?(?=\])/)
  puts result.join(',') unless result.empty?
end
