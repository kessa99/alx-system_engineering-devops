#!/usr/bin/env ruby
input_string = ARGV[0]

if input_string.match(/School/)
  puts input_string.scan(/School/)
end
