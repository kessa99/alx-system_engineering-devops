#!/usr/bin/env ruby

def check_lile(test1.txt)
  unless File.exist?(test1.txt)
    puts "existe pas"
    return
  end

  file_content = File.read(test1.txt)
  if file_content.match(/Holberton/)
    puts "Le ichier contient Holberton"
  else
    puts "aucun"
  end
end
